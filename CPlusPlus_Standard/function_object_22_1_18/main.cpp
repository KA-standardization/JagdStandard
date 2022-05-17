#include "ByRef.hpp"



/*
*	�º���
	function object: ӵ�������Լ��Ķ�������
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
	function objectӵ���ڲ�״̬ 
		��Ϊ�������ͬʱӵ�ж��״̬
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

// // passed by value����ı�a��״̬
//int testByVal(int num) {
//	num = num * 3;
//	return num;
//}
//
//
//// passed by reference�ı�a��״̬
//int testByRef(int& num) {
//	num = num * 3;
//	return num;
//}

// int& const num ������ı�ָ��ָ�� ���Ըı�ָ��ָ���ֵ
// const int& num ������ı�ָ��ָ���ֵ,���Ըı�ָ���ָ��
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


	// function object: ӵ�������Լ��Ķ�������
	//set<Person, PersonSortCriterion> coll;
	//// coll ���캯�����Զ�����class PersonSortCriterion��һ��ʵ��,����Ԫ�ض����Դ�Ϊ����׼���������
	//// ����PersonSortCriterion�Ǹ�class, template <class PersonSortCriterion>
	//for (auto pos = coll.begin();pos != coll.end();++pos) {

	//}

	// function objectӵ���ڲ�״̬
	//list<int> coll2;
	/*
		������ֵ��д������
		generate_n(back_inserter(coll2), 9, IntSequence(1));
		IntSequence(1): ��1Ϊ��ֵ������ôһ��function object
		generate_n ǰ��д��9��Ԫ��ֵ,����2-10
		generate next(coll2.begin()), prev(coll2.end())��д���±�1-7
	*/

	/*
		Ĭ�������function object��passed by value����passed by reference,����㷨����ı�function object��״̬
	*/

	//generate_n(back_inserter(coll2), 9, IntSequence(1));
	//for (auto item : coll2) {
	//	cout << "func �ڲ�״̬ A-->" << item << endl;
	//}
	//cout<<endl;
	//generate(next(coll2.begin()), prev(coll2.end()), IntSequence(42));
	//for (auto item : coll2) {
	//	cout << "func �ڲ�״̬ B-->" << item << endl;
	//}

	return 0;
}