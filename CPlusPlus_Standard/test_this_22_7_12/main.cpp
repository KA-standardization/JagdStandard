#include <iostream>

using namespace std;

struct Person {
    int m_age;
    Person() {
        m_age = 0;
        cout << "Person()" << endl;
    }
    // 构造函数重载
    Person(int age) {
        m_age = age;
        cout << "Person(int age)" << endl;
    }
};


int main() {

    Person person;
    Person person2(1);
    Person person3;


    getchar();
    return 0;
}