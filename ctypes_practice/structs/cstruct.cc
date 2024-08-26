#include <stdlib.h>  
#include <stdio.h>
#include <iostream>
using namespace std;

struct Point {
  float x;
  float y;
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
        pa->points[i].x = i+1.1;
        pa->points[i].y = i+2.1;
    }

    // Return the pointer to the allocated memory
    return pa;
    }

    void write_points(struct PointArray* pa){
      
      for (int i = 0; i < 7; i++) {
        printf("x: %6.4lf", pa->points[i].x);
        printf(" y: %6.4lf\n", pa->points[i].y);
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