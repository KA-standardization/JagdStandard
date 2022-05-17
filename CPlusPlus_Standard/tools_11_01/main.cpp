#include <algorithm>
#include <iostream>

using namespace std;


bool int_ptr_less(int* a, int* b) {
	return *a < *b;
}

int main() {

	int x = 11;
	int y = 12;
	int z = 13;
	int* px = &x;
	int* py = &y;
	int* pz = &z;

	//int* pxy = std::max(px, py, int_ptr_less);
	std::max(px, py, int_ptr_less);
	//cout << pxy << endl;

	std::pair<int*, int*> extremes = std::minmax({ px,py,pz }, int_ptr_less);
	//cout << extremes.first << endl;
	//cout << extremes.second << endl;

	std::minmax({ px,py,pz }, [](int* a, int* b) {
		return *a < *b;
		});

	int i;
	long l;

	// 要求两个实参类型必须一致
	//std::max(i,l);
	std::max<long>({ i,l });






	getchar();
	return 0;
}
