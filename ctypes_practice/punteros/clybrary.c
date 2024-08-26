#include<stdio.h>
#include<string.h>
#include<stdlib.h>

//char* el asterisco indica aqui que se entrega un puntero
char* alloc_memory(){
    char* str = strdup("Hello world");  //Esta es una forma de declarar datos dinamicos
    printf("Memory Allocation\n"); //Agrego \n para que el retorno se escriba en la linea siguiente
    return str;
}   

void free_memory(char* ptr){
    printf("Memory Deallocated");
    free(ptr);

}