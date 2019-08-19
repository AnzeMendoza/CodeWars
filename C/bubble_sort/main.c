#include <stdio.h>
#define TRUE    1
#define FALSE   0
#define LEN(x)  sizeof(x)/sizeof(int)
#define ENDLN   printf("\n")
/*---------------------------------------------------*/
void printArray(int* array, int lenght);
void bubblesort(int* array, int lenght);
void intercambio(int* a, int* b);
/*---------------------------------------------------*/
int main()
{   int a[]={4, 8, 0,11,1,66,-1,0};

    printArray(a, LEN(a));
    bubblesort(a, LEN(a));
    printArray(a, LEN(a));
    return 0;
}
/*---------------------------------------------------*/
void printArray(int* array, int lenght){
    for(int i=0;i < lenght;i++){
        printf("%d ", *(array+i));
    }
    ENDLN;
}
/*---------------------------------------------------*/
void bubblesort(int* array, int lenght){

    for(int i = 0 ;i < lenght-1; i++){
        for(int j=0;j < lenght-1;j++){
            if(array[j] >= array[j+1]){
                intercambio(&array[j], &array[j+1]);
            }
        }
    }
}
/*---------------------------------------------------*/
void intercambio(int* a, int* b){
    int swap;

    swap = *a;
    *a = *b;
    *b = swap;
}
/*---------------------------------------------------*/
