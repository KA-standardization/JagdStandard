#include <iostream>

using namespace std;

struct Persion
{
    int m_age;
    int m_id;
    int m_height;
    void run(){
        // 指针想访问成员变量只能 -> 不能用. 因为this是指针
        cout << "void run()" << this->m_age << endl;
    }
    void run2(Persion *persion){
        cout << "void run2(Persion *persion)" << persion->m_age << endl;
    }
    void display(){
        cout << "void display()" << m_id << " " << m_age<< " " << m_height << endl;
    }
};

void func(){

}


int main(){
    func();
    Persion persion;
    persion.m_age=10;
    persion.run();
    persion.run2(&persion);

    Persion *p = &persion;
    p->m_age =10;
    p->m_height =173;
    p->m_id=1890;
    p->display();

    Persion *p2=(Persion *)&persion.m_age;
    // cc->int3 int硬件中断 3中断码 
    // eax == &persion.m_age == &persion + 4
    // mov eax, dword ptr [p2]
    // mov dword ptr [eax + 0],40
    // mov dword ptr [&persion + 4 + 0],40
    p2->m_id=40;
    // mov eax, dword ptr [eax + 4],50
    // mov eax, dword ptr [&persion + 4 +4],50
    p2->m_age=50;
    persion.display();

    getchar();
    return 0;
}