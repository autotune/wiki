### GREP USAGE

#### SEARCH FOR STRING

    grep "string" /my/file.txt


#### SEARCH FOR CONTENT

1) Search directories for string except for dir. 
   -r search recursively. 
   -n include line number. 
   -w match line with whole word only. 

    grep -rnw -e 'sudo' ./* --exclude-dir=./v2


