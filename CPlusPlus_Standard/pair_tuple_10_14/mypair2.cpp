#include <utility>
#include <functional>
using namespace std;

int my_ref_pair() {
	int i = 0;
	auto p = make_pair(ref(i), ref(i));
	++p.first;
	return i;
};
