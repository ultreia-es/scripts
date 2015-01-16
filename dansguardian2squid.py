#!/usr/bin/env python

# Print a Squid log to stdout converted from Dansguardian log received in stdin or as argument

import datetime, re, fileinput

for line in fileinput.input():

	if re.match("TCP_", re.sub(r" +", " ", line).split(" ")[3]):
		# This line is already in Squid format
		print line,
		continue

	logdate, logtime, user, ip, url, action, method, size, _ = line.split(" ", 8)
	_, httpstatus, mime, _, _, _ = line.rsplit(" ", 5)
	timestamp = datetime.datetime.strptime(' '.join([logdate, logtime]), "%Y.%m.%d %H:%M:%S").strftime("%s.000")

	if not action:
		status = "TCP_MISS/" + httpstatus
	else:
		status = "TCP_DENIED/" + httpstatus
		# "Reason" column not empty, no realiable way to get method and size
		# We are faking them
		method = "GET"
		size = 0

	# Not available
	time = 0
	hierarchy = "DIRECT/" + ip

	print timestamp, time, ip, status, size, method, url, user, hierarchy, mime
