#!/bin/bash

# add TITLE to output command [COMMENT]
# for example ls -lha [LSLHA] [COMMENT]
# and make it easy for python to parse [COMMENT]
# or to parse in grep [COMMENT]
# grep COMMENT [COMMENT].

function printcmd {
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    TITLE="LSLHA"
    ### <!-- BOF LSLHA --> ###

    LSLHA=()
    for OUTPUT in "$(ls -lha)"
    do
      LSLHA+=("$OUTPUT")
    done

echo "$(echo "$LSLHA"|sed "s/$/ [$TITLE]/g")"
    ### <!-- EOF LSLHA --> ### 
}

printcmd
