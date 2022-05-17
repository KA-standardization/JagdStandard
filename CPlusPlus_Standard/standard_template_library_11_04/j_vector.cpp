#include <vector>
#include <iostream>

//using namespace std;

void jajdVector() {
	std::vector<int> m_cool;
	for (int i = 0;i <= 6;i++) {
		m_cool.push_back(i);
	}

	for (int i = 0;i < m_cool.size();i++) {
		std::cout << m_cool[i] << std::endl;
	}
}
