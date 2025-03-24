#!/usr/bin/env bash
read -p "Enter python virtual env name: "  ENV_NAME
PATH1="./$ENV_NAME/lib/python3.7/site-packages/packaging/version.py"
PATH2="./$ENV_NAME/lib/python3.7/site-packages/packaging/version.py"
if test -f "$PATH1"; then
    sed -i 's/match = self._regex.search(version)/match = self._regex.search(str(version))/g' $PATH1
fi

if test -f "$PATH2"; then
    sed -i 's/match = self._regex.search(version)/match = self._regex.search(str(version))/g' $PATH1
fi

echo Done.
