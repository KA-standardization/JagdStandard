#include <iostream>
using namespace std;



int main(){
    // 4个字节 返回第一个字节的首地址
    // int *p = (int *)malloc(4);
    // *p = 10;
    // free(p);

    // char *c = (char *)malloc(4);
    // *c =10;
    // // c[0]=10
    // *(c+1)=11;
    // // c[1]=11
    // free(c);
    // int *p = new int;
    // delete p;

    char *p = new char[4];
    delete[] p;


    getchar();
    return 0;
}