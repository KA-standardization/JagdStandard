#include <iostream>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include "assoiter.hpp"

int main() {

	std::unordered_set<int> coll;
	asso_insert_iterator<decltype(coll)> iter(coll);
	*iter = 1;
	iter++;
	*iter = 2;
	iter++;
	*iter = 3;

	asso_inserter(coll) = 44;
	asso_inserter(coll) = 55;
	//std::vector<int> vals = { 11,22,33,44,55,66 };
	//std::copy(vals.begin(), vals.end(), asso_inserter(coll));
	for (auto item : coll) {
		std::cout << "coll:  " << item << std::endl;
	}
	//for (auto item_ : vals) {
	//	std::cout << "vals:  " << item_ << std::endl;
	//}

	return 0;
}