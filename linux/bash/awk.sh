
# make uppercase or lowercase
function ulcase {

    TITLE="LSLHA"
    printf "$(printf $TITLE|awk '{print toupper($0)}')\n"
    printf "$(printf $TITLE|awk '{print tolower($0)}')\n"
 
}
# ulcase

# function columns {

column="$(sar -r | grep '%commit' | awk '{ for(i;i<=NF;i++){\
    if ($i ~ /commit/) { print i } } \
}')"

#printf $column
# num="1"
# printf "$(sar -r|awk "{print $column}")"

ulcase
