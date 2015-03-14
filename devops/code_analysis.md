### CODE ANALYSIS

#### STRACE

1) View files being read and written

    strace -e open,write -o oecalls.txt mycommand
 
#### GREP 

2) Search directories for string except for dir.

   -r search recursively.

   -n include line number.

   -w match line with whole word only.

    grep -rnw -e 'sudo' ./* --exclude-dir=./v2
