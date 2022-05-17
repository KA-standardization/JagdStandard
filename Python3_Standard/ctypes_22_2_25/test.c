#include <stdio.h>
#include <math.h>

int foo(int a){
    int c;
    for(c=2;c<=sqrt(a);c++){
        if(a%c==0){
            return 0;
        }
    }
    return 1;
}