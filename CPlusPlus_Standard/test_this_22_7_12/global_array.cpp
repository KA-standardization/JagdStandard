#include <array>

using namespace std;

int g_array[3];

int main() {
	int index = 2;
	g_array[0] = 10;
	g_array[1] = 20;
	g_array[3] = 30;
	g_array[index] = 100;

	return 0;
}
