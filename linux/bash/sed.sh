#!/bin/bash

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

}

printcmd
