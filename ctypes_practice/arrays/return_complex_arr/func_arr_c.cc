
#include<stdio.h>
#include<string.h>
#include<stdlib.h>

using namespace std;
//Esta funcion retorna un array

extern "C"{
    
    float *inc_array(double *arr, int size){
    
    float *arr2;
    for (int i = 0; i < size; i++){
        arr2[i] = arr[i] + 1.1;
    }
    for (int i = 0; i < size; i++){
        printf("%.6f\n",arr2[i]);
    }
    
    return arr2;

    

}
    float *create_arr(){
            // float *arr = (float*)malloc(50*sizeof(float));
            float *arr;
            for (int i = 0; i < 50; i++){
                arr[i] = i + 50.0;
                
            }
            return arr;

        }
}

