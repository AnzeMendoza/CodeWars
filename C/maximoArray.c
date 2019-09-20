#include <stdio.h>
#define LEN(x) sizeof(x)/sizeof(int)

int obtenerMaximo(int [], int[], int);

int main()
{
    int array[]={1,5,4,9,41,2,6,400,-1,3,12,3,3,101,1,3,13,300};
    int aMax[3]={};
    printf("maximo: %d\n", obtenerMaximo(array, aMax, LEN(array)));
    for (int i = 0; i < 3; i++)
    {
        printf("%d->", aMax[i]);
    }
    
    return 0;
}

int obtenerMaximo(int *a, int *m, int len){
    int maxValor;
    int index=0;

    for (size_t i = 0; i < len; i++){
        if(!i){
            maxValor = *a;
            m[index%=3] = maxValor;
            index++;
        }
        if(*(a+i) > maxValor){
            maxValor = *(a+i);
            m[index%=3] = maxValor;
            index++;
        }  
    } 
    return maxValor; 
}

