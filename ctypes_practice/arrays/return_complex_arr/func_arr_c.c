#include<stdio.h>
#include<string.h>
#include<stdlib.h>
double *inc_array(double *arr, int size){
    
    double *arr2 = malloc(50*sizeof(double));
    for (int i = 0; i < size; i++){
        arr[i]++;
        arr2[i] = arr[i] + 1.1;
    }
    for (int j = 0; j < size; j++){
        printf("%.6f\n",arr2[j]);
    }
    return arr2;
    // for (int i = 0; i < size; i++){
    //     printf("%.6f\n",arr2[i]);
    // }
    
   

}