#include <array>
#include <string>
#include <iostream>

void jagdArray() {
	std::array<std::string, 5> m_coll = { "hello","world" };
	for (int i = 0;i < m_coll.size(); ++i) {
		std::cout << i << ": " << m_coll[i] << std::endl;
	}
}
