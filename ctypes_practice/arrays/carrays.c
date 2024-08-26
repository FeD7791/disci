#include<stdio.h>
#include<string.h>
#include<stdlib.h>


// Esta funcion retorna un entero
int sumarray(int *arr, int size){
    int sum = 0;
    for (int i = 0; i < size; i++){
        sum += arr[i];
    }
    return sum;
}

//Esta funcion retorna un array

int *inc_array(int *arr, int size){
    for (int i = 0; i < size; i++){
        arr[i]++;
    }
    return arr;

}