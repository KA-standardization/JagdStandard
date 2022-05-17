#include <map>
#include <string>
#include <iostream>

// key/value pair pair<const key,value>
void jagdMap() {
	std::multimap<int, std::string> m_coll;
	m_coll = {
		{1,"buch"},
		{2,"Kaiser"},
		{3,"Kaiserin"},
		{3,"holle"}
	};
	m_coll.insert({ 1,"null" });
	// 仅当建不存在时才进行插入
	m_coll.emplace(2, "map");
	// 删除 全部键为3的key
	m_coll.erase(3);

	//std::cout << m_coll.at(1) << std::endl;
	for (auto elem : m_coll) {
		std::cout << elem.first << ": " << elem.second << std::endl;
	}
}
