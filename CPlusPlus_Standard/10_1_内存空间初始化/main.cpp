#include <iostream>
#include <memory.h>
using namespace std;



class Person{
public:
    int m_id;
    int m_age;
    int m_height;
    void r(){
        run();
    };

private:
    void run(){
        cout << m_id << m_age << m_height << endl;
    }
};


int main(){
    // malloc 不会初始化堆空间
    // int *p=(int *) malloc(4);
    // *p=20;

    // cout << *p << endl;

    // int *p =(int *) malloc(sizeof(int) * 10);
    // // 将40个字节设置为0
    // memset(p,0,40);

    // cout << *p << endl;

    // // 未初始化
    // int *p0 =new int;
    // // 被初始化为0
    // int *p1=new int();
    // // 被初始化为5
    // int *p1=new int(5);
    // // 数组元素未被初始化
    // int *p4=new int[3];
    // // 数组元素都被初始化为0
    // int *p5 =new int[3]();
    // int *p6=new int[3]{};
    // // 数组受元素被初始化为5 其他元素被初始化为0
    // int *p7=new int[3]{5};

    // memset 函数是将较大的数据结构内存清零比较快的方法

    Person persion;
    Person *p = &persion;
    p->m_age=1;
    p->m_height=111;
    p->m_id=7;
    p->r();

    memset(p,0,sizeof(persion));
    p->r();

    Person pp[]={{1,2,3},{4,5,6},{7,8,9}};
    pp->r();
    (pp+1)->r();
    memset(pp,0,sizeof(pp));
    pp->r();

    // 对象内存
    // 全局区（数据段）全局变量 
    // 栈空间 函数里面的局部变量
    // 堆空间 动态申请内存 malloc new

    // Person *p = new Person;
    // 栈空间       堆空间
    
    

    getchar();
    return 0;
}