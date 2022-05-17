#include <iostream>
#include <vector>
#include <algorithm>
#include <list>

using namespace std;


int lambda_mutable() {
	list<int> l_i = { 1,2,3,4,5,6,7 };
	list<int>::iterator pos;
	int sum = 0;
	pos = remove_if(l_i.begin(), l_i.end(), [sum](int)mutable {return ++sum == 3;});
	l_i.erase(pos, l_i.end());
	for (int e : l_i) {
		cout << e << endl;
	}
	return 1;
}