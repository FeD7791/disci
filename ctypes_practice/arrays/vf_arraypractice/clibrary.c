#include<stdio.h>
#include<string.h>
#include<stdlib.h>

void printer_arr(double *arr, int size){
    for (int i = 0; i < size; i++){
        printf("%.6f\n",arr[i]);
    }

}

//Si queremos retornar un array tenemos que hacer una alocacion dinamica puesto que si no, no es posible sacarlo
//del scope local de la funcion

float* return_array(){
    float* arr = malloc(10*sizeof(int));
    for (int i = 0; i < 10; i++){
        arr[i]=i;
    }
    return arr;
} 

// Cuando creas un array de forma dinamica tenes que liberar la memoria
void free_memory(float* arr, int size){
    
    printf("Memory Deallocated");
    free(arr);
}
