//
//  main.cpp
//  STL_11_12
//
//  Created by 王煜 on 2021/11/12.
//

#include <iostream>
#include <array>

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    
    array<int, 10> x ={1,2,3,4,5,6,7,8,9,0};
    for (const auto i:x) {
        cout << i << endl;
    }
    
    cout<< x.front()<<endl;
    cout << x.back()<<endl;
    return 0;
}
