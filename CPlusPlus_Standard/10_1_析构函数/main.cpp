#include <iostream>
using namespace std;

struct Person
{
    int m_id;
    Person(){
        cout << "P" << endl;
    }

    ~Person(){
        cout << "~P" << endl;
    }

};


int main(){
    {
        Person person;
        
    }
    Person *p = new Person;

    // 栈空间
    cout << p << endl;
    // 堆空间
    cout << &p << endl;
    getchar();
    return 0;
}