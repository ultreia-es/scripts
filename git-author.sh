#!/bin/bash

for s in "${BASH_SOURCE[@]}"
do
  if [ "${s}" = "$0" ]
  then
    echo "You should call this script with source:" >&2
    echo "  source $0" >&2
    exit
  fi
done

n=""
while [ -z "$n" ]
do
  echo -n "Your name: "
  read n
  test -z "$n" && echo "Name cannot be empty"
done
e=""
while [ -z "$e" ]
do
  echo -n "Your e-mail: "
  read e
  test -z "$e" && echo "E-mail cannot be empty"
done

export GIT_AUTHOR_NAME="${n}"
export GIT_COMITTER_NAME="${n}"
export GIT_AUTHOR_EMAIL="${e}"
export GIT_COMITTER_EMAIL="${e}"
