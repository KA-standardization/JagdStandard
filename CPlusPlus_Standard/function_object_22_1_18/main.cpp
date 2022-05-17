#include "ByRef.hpp"



/*
*	仿函数
	function object: 拥有属于自己的独特类型
*/

//class Person {
//public:
//	string f_name() const;
//	string l_name() const;
//};
//
//class PersonSortCriterion {
//public:
//	bool operator()(const Person& p1, const Person& p2) const {
//		return p1.l_name() < p2.l_name() || (p1.l_name()==p2.l_name()&&p1.f_name()<p2.f_name());
//	}
//};

/*
	function object拥有内部状态 
		行为像个函数同时拥有多个状态
*/

//class IntSequence {
//private:
//	int value;
//public:
//	IntSequence(int initVal):value(initVal){}
//	int operator()() {
//		return ++value;
//	}
//};

// // passed by value不会改变a的状态
//int testByVal(int num) {
//	num = num * 3;
//	return num;
//}
//
//
//// passed by reference改变a的状态
//int testByRef(int& num) {
//	num = num * 3;
//	return num;
//}

// int& const num 不允许改变指针指向 可以改变指针指向的值
// const int& num 不允许改变指针指向的值,可以改变指针的指向
//int testByRefConst(int& const num) {
//	num = num * 3;
//	return num;
//}

int main() {
	FuncObjByRef();

	//int a = 2;

	//auto res1 = testByVal(a);
	//cout << "ByVal-->" << res1 << endl;

	////auto res3 = testByRefConst(a);
	////cout << "ByRefConst-->" << res3 << endl;

	//cout << "a-->" << a << endl;

	//auto res2 = testByRef(a);
	//cout << "ByRef-->" << res2 << endl;


	// function object: 拥有属于自己的独特类型
	//set<Person, PersonSortCriterion> coll;
	//// coll 构造函数会自动产生class PersonSortCriterion的一个实例,所有元素都将以此为排序准则进行排序
	//// 由于PersonSortCriterion是个class, template <class PersonSortCriterion>
	//for (auto pos = coll.begin();pos != coll.end();++pos) {

	//}

	// function object拥有内部状态
	//list<int> coll2;
	/*
		产生数值并写入容器
		generate_n(back_inserter(coll2), 9, IntSequence(1));
		IntSequence(1): 以1为初值产生这么一个function object
		generate_n 前后共写入9次元素值,产生2-10
		generate next(coll2.begin()), prev(coll2.end())改写了下标1-7
	*/

	/*
		默认情况下function object是passed by value不是passed by reference,因此算法不会改变function object的状态
	*/

	//generate_n(back_inserter(coll2), 9, IntSequence(1));
	//for (auto item : coll2) {
	//	cout << "func 内部状态 A-->" << item << endl;
	//}
	//cout<<endl;
	//generate(next(coll2.begin()), prev(coll2.end()), IntSequence(42));
	//for (auto item : coll2) {
	//	cout << "func 内部状态 B-->" << item << endl;
	//}

	return 0;
}