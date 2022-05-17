#include <functional>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
// 避免重复的写出命名空间
using namespace std::placeholders;

void incr(int& i) {
	++i;
}

/*
	调用成员函数 492
		bind(&P::print,_1) 
			定义一个function obj,其内针对传入的P调用paraml.print()
			也就是说,第一实参是个成员函数,下一个实参讲定义用以调用成员函数的对象
		bind(&P::print_2,_1,_2)
			_2成员函数的参数
			P n("haha")
			bind(&P::print_2,_1,"abc")(n)
	调用具有改动能力的成员函数 modifying member function

	对于成员函数,改用mem_fn()adapter 就不需要占位符表示调用者
		std::mem_fn(&P::print)
		std::mem_fn(&P::print)(n,"abc"); // calls n.print("abc");

	绑定至数据成员
		容器是个map, 其元素是key/value pair, 为了得到对元素的value的访问权必须这样做&map
		std::bind(std::plus<int>(),_1,bind(&map<string, int>::value_type::second,_2))

	Adapter
		
*/



int main() {
	auto plus11 = std::bind(std::plus<int>(), std::placeholders::_1, 11);
	std::cout << "plus11  " << plus11(1) << std::endl;

	auto plus11multi = std::bind(std::multiplies<int>(), std::bind(std::plus<int>(), std::placeholders::_1, 10), 2);
	std::cout << "plus multiplies  " << plus11multi(2) << std::endl;

	// placeholders::_1 指第一个参数
	auto pow3 = std::bind(std::multiplies<int>(), std::bind(std::multiplies<int>(), std::placeholders::_1, std::placeholders::_1), std::placeholders::_1);
	std::cout << "pow3  " << pow3(2) << std::endl;

	auto divide = std::bind(std::divides<double>(), std::placeholders::_2, std::placeholders::_1);
	std::cout << "divide  "<<divide(2,4) << std::endl;

	// 如果把binder或function object传给算法,后者会把它作用于所操作的每一个元素 
	// 算法 by reference
	

	vector<int> coll = { 1,2,3,4,5 };
	auto s = std::transform(coll.begin(), coll.end(), coll.begin(), std::bind(std::plus<int>(), _1, 100));
	for (int i = 0;i < size(coll);i++) {
		cout << "coll  " << coll[i] << endl;
	}
	
	// bind内部会复制被传入的实参 可以利用 ref()\cref()
	int i = 0;
	std::bind(incr, i)();
	cout << "i=" << i << endl;
	//std::bind(incr, std::ref(i))();
	//cout << "i=" << i << endl;

	string coll2 = "abcdef";
	auto index = std::find_if(coll2.begin(), coll2.end(), std::bind2nd(std::ptr_fun(std::strcmp), "c"));
	/*cout << "index-->" << index << endl;*/


	getchar();
	return 0;
}