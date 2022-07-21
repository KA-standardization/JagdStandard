#include <iostream>

using namespace std;

class AAA
{
public:
	AAA();
	~AAA();
};

AAA::AAA()
{
}

AAA::~AAA()
{
}

struct BBB
{
public:
	BBB();
	~BBB();
};

BBB::BBB()
{
}

BBB::~BBB()
{
}

int main() {
	AAA a;
	BBB b;

	getchar();
	return 0;
}