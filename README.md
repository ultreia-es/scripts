# Ultreia Scripts

Scripts used by [Ultreia Comunicaciones](http://www.ultreia.es) in its daily work.

## git-author.sh

Sets git author and committer variables to be used in following commits.

In order to make it work with current shell, it should be called with source:

```bash
source git-author.sh
```

or

```bash
. git-author.sh
```

Actually, it will fail if called otherwise:

```
# bash git-author.sh 
You should call this script with source:
  source git-author.sh
```
