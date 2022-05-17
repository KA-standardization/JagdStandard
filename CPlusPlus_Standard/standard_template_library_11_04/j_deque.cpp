#include <deque>
#include <iostream>

void jagdDeque() {
	std::deque<float> m_coll;
	for (int i = 1;i <= 6;++i) {
		m_coll.push_front(i * 1.1);
		// 末尾添加
		//m_coll.push_back(i * 1.2);
	}

	for (int i = 0;i < m_coll.size();++i) {
		std::cout << m_coll[i] << std::endl;
	}


}
