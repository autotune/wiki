
# make uppercase or lowercase
function ulcase {

    TITLE="LSLHA"
    printf "$(printf $TITLE|awk '{print toupper($0)}')\n"
    printf "$(printf $TITLE|awk '{print tolower($0)}')\n"
 
}
ulcase
