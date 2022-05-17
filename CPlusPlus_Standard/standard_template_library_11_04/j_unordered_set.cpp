#include <unordered_set>
#include <iostream>
#include <string>

void jagdUnorderSet() {
	std::unordered_set<std::string> m_coll{ "bush","Kaiser","Laden" };
	for (const auto& elem : m_coll) {
		std::cout << "f: " << elem << std::endl;
	}
	m_coll.insert({ "buckets" });
	for (const auto& elem : m_coll) {
		std::cout << "e: " << elem << std::endl;
	}




}
