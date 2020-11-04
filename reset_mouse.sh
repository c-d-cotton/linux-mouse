#!/usr/bin/env bash
# BASH_PREAMBLE_START_STANDARD:{{{

# Christopher David Cotton (c)
# http://www.cdcotton.com

# Get full real filename
__fullrealfile__="$(readlink -f "$0")"

# Function to get git directory containing this file
getprojectdir () {
    curlevel="$1"
    projectdir=0
    while [ "$curlevel" != "/" ]; do
        curlevel="$(dirname "$curlevel")"
        if [ -d "$curlevel""/.git/" ]; then
            projectdir="$curlevel""/"
            break
        fi
    done
    echo "$projectdir"
}

# Directory of project
__projectdir__="$(getprojectdir "$__fullrealfile__")"

# BASH_PREAMBLE_END:}}}

sudo modprobe -r psmouse
sudo modprobe psmouse
