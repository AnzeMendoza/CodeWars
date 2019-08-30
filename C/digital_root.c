#include <stdio.h>
#include <stdlib.h>

int digital_root(int n);

int main(int argc, char const *argv[])
{
    printf("%d\n", digital_root(195));
    
    return 0;
}

int digital_root(int n){
    int acum=0;
    int resto;
    int divisor=n;
    
    while (divisor>=1 || acum==0 )
    {
        resto = divisor % 10;
        divisor = divisor / 10;
        acum+=resto;
    }
    return acum;   
}
