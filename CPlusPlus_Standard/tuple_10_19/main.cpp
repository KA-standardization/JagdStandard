#include <iostream>
#include <tuple>
#include <functional>
#include <vector>
#include <memory>
#include <string>

using namespace std;

class Person : public std::enable_shared_from_this<Person> {
public:
	string name;
	shared_ptr<Person> mother;
	shared_ptr<Person> father;
	vector<shared_ptr<Person>> kids;

	Person(const string& n, shared_ptr<Person> m = nullptr, shared_ptr<Person> f = nullptr) :name(n), mother(m), father(f) {}
	~Person() {
		cout << "~Person()  " << name << endl;
	}

	// 0x7B91F3BE (ucrtbased.dll)处(位于 5_1_2_Tuple_10_19.exe 中)引发的异常: 0xC0000005: 读取位置 0xDDDDDDDD 时发生访问冲突
	//void setParents(shared_ptr<Person> m = nullptr, shared_ptr<Person> f = nullptr) {
	//	mother = m;
	//	father = f;
	//	if (m != nullptr) {
	//		m->kids.push_back(shared_ptr<Person>(this));
	//	}
	//	if (f != nullptr) {
	//		f->kids.push_back(shared_ptr<Person>(this));
	//	}
	//}

	// shared_from_this() 建立起一个源自this的正确shared_ptr
	void setParents(shared_ptr<Person> m = nullptr, shared_ptr<Person> f = nullptr) {
		mother = m;
		father = f;
		if (m != nullptr) {
			m->kids.push_back(shared_from_this());
		}
		if (f != nullptr) {
			f->kids.push_back(shared_from_this());
		}
	}
};


int main() {

	//string s;
	//tuple<string&> t(s);
	//get<0>(t) = "hello";
	//cout << s << endl;
	//auto p = make_tuple(22, 33.3, "buch");
	//// get<i>(p) 运行期传入索引值是不允许的
	//cout << get<0>(p) << endl;
	//cout << &p << endl;
	//tuple<int, int, string> t2(11, 22, "buch");
	//int i;
	//int j;
	//string ss;
	//std::tie(i, j, ss) = t2;
	//cout << i << j << ss << endl;
	//std::vector<int> m_i{ 1,2,3 };
	//cout << m_i[0] << endl;
	//cout << sizeof(m_i[0]) << endl;
	//cout << m_i.size() << endl;
	//cout << m_i.max_size() << endl;
	//try {
	//	shared_ptr<string> sp(new string("Kaiser"));
	//	weak_ptr<string> wp = sp;
	//	sp.reset();
	//	cout << wp.use_count() << endl;
	//	cout << boolalpha << wp.expired() << endl;
	//	shared_ptr<string> p(wp);
	//}
	//catch (const std::exception& e) {
	//	cout << "Exception: " << e.what() << endl;
	//}
	// 空荡指针(dangling pointer) 
	// class weak_ptr 允许共享但不拥有某对象, 这个class会建立起一个shared pointer,一旦最末一个拥有该对象的shared pointer失去了拥有权
	// 任何weak pointer 都会自动成空

	// 90 std::enable_shared_from_this<> 

	string name = "expired";
	shared_ptr<Person> mom(new Person(name + "'s mom"));
	shared_ptr<Person> fat(new Person(name + "'s fat"));
	shared_ptr<Person> kid(new Person(name));
	kid->setParents(mom, fat);
	// mom.reset()
	// make_shared()
	// allocate_shared()

	// 返回储存的pointer 通常是被拥有物的地址,若不拥有对象则返回nullptr
	cout << mom.get() << endl;

	// 返回共享对象的拥有者数量
	cout << mom.use_count() << endl;

	// 返回mom是否为唯一拥有者 等价于 mom.use_count()==1
	cout << mom.unique() << endl;

	// lambda表达式 unique自定义删除
	std::unique_ptr<int, void(*)(int*)> up(new int[10], [](int* p) {
		delete[] p;
		});

	auto dl = [](int* p) {
		delete[] p;
	};

	std::unique_ptr<int, decltype(dl)> up2(new int[10], dl);




	getchar();
	return 0;
}
