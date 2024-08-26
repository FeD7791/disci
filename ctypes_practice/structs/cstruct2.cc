#include <stdlib.h>  
#include <stdio.h>
#include <iostream>
using namespace std;

struct Point {
  float rad;
  float x[3];
  float y[3];
};

struct PointArray {
  struct Point points[1];
};

extern "C"{
    // Function to create and initialize a PointArray
    struct PointArray* createAndPrintPointArray() {
    // Allocate memory for the PointArray struct on the heap
    struct PointArray* pa = (struct PointArray*)malloc(sizeof(struct PointArray));
    

    if (pa == NULL) {
        // Handle memory allocation failure
        return NULL;
    }

    // Initialize the points within the allocated memory
    for (int i = 0; i < 7; i++) {
      pa->points[i].rad = 7.8;
      pa->points[i].x[0] = i+1.1;
      pa->points[i].x[1] = i+2.1;
      pa->points[i].x[2] = i+3.1;
      pa->points[i].y[0] = i+4.1;
      pa->points[i].y[1] = i+5.1;
      pa->points[i].y[2] = i+6.1;
    }

    // Return the pointer to the allocated memory
    return pa;
    }

    void write_points(struct PointArray* pa){
      float x;
      float y;
      for (int i = 0; i < 7; i++) {
        printf("rad: %2.1f", pa->points[i].rad);
        printf("x: %2.1lf", pa->points[i].x[0]);
        printf(" x: %2.1lf", pa->points[i].x[1]);
        printf(" x: %2.1lf", pa->points[i].x[2]);
        printf(" y: %2.1lf", pa->points[i].y[0]);
        printf(" y: %2.1lf", pa->points[i].y[1]);
        printf(" y: %2.1lf\n", pa->points[i].y[2]);
      }
    }

    void free_memory(struct PointArray* arr){
    printf("Memory Deallocated");
    free(arr);

    }
}

int main(){
  struct PointArray* pa;
  pa = createAndPrintPointArray() ;
  write_points(pa);
  return 0;
}