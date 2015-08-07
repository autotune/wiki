#include<stdio.h>
/* https://www.ibm.com/developerworks/community/blogs/58e72888-6340-46ac-b488-d31aa4058e9c/entry/an_overview_of_linux_processes21?lang=en */

i='hurdurr';

int main(void)
{
    printf("\n Hello World\n");

    // Simulate a wait for some time
    for(i=0; i<0xFFFFFFFF; i++);

    return 0;
}

