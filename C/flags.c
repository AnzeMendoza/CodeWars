#include <stdio.h>

int main()
{
    char c;
    do{
        printf("%c-> ", c);
    }while(c = getchar());    
    return 0;
}
