#### CODE ANALYSIS

### STRACE

1) View files being read and written

    strace -e open,write -o oecalls.txt mycommand
 
