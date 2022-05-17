#include <iostream>
#include <string>
#include <memory>
#include <dirent.h>
#include <cstring>
#include <cerrno>


using namespace std;


class DirCloser {
public:
	void operator () (DIR* dp) {
		if (closedir(dp) != 0) {
			std::cerr << "OOPS: closedir() failed" << std::endl;
		}
	}

};

int main() {


	//extent "C" typedef int(*DirCloser)(DIR*);
	unique_ptr<DIR, DirCloser> pDir(opendir("."));
	struct dirent* dp;
	while ((dp = (dirent*)readdir(pDir.get())) != nullptr) {
		string filename(dp->d_name);
		cout << filename << endl;
	}
	// 为一个被拥有的对象调用deleter
	// pDir.~unique_ptr()

	// 对一个被拥有物调用deleter 并重新初始化shared pointer 使它拥有*ptr
	// pDir.reset(ptr)
	getchar();
	return 0;
}
