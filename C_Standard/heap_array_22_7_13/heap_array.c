//
// Created by root on 2022/7/13.
//

#include <stdlib.h>

int main() {
    int *heapArray = (int *) malloc(3 * sizeof(int));
    int index = 2;
    heapArray[0] = 10;
    heapArray[1] = 20;
    heapArray[2] = 30;
    heapArray[index] = 100;
}

