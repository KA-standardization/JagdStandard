#include <iostream>
#include <string>
#include <queue>
#include <WinSock2.h>
//#include <Windows.h>

#pragma comment(lib, "ws2_32.lib")
#pragma warning(disable:4996)

using namespace std;


bool StartCrawl(std::string url);

struct RequestHttp
{
private:
	SOCKET m_socket;
	string m_host;
	string m_object;
public:
	RequestHttp();
	~RequestHttp();

	bool InitNet();
	bool AnalyseUrl(string url);
	bool Connect();
	bool GetHtml(string& html);

};

RequestHttp::RequestHttp() {

}

RequestHttp::~RequestHttp() {

}

bool RequestHttp::AnalyseUrl(string url) {
	
	if (std::string::npos == url.find("http://")) {
		return false;
	}

	int pos = url.find('/', 7);
	if (std::string::npos == pos) {
		m_host = url.substr(7);
		m_object = '/';
	}
	else
	{
		m_host = url.substr(7, pos - 7);
		m_object = url.substr(pos);
	}

	if (m_host.empty()) {
		return false;
	}
	return true;
}

bool RequestHttp::Connect() {
	//hostent *p = gethostbyname(m_host.c_str());
	hostent *p = gethostbyname(m_host.c_str());
	if (p == NULL) {
		return false;
	}
	sockaddr_in sa2;
	memcpy(&sa2.sin_addr, p->h_addr, 4);
	sa2.sin_family = AF_INET;
	sa2.sin_port = htons(80);

	if (SOCKET_ERROR == connect(m_socket, (sockaddr*)&sa2, sizeof(sockaddr))) {
		return false;
	}
	return true;
}

bool RequestHttp::InitNet() {

	WSADATA wd;
	if (0 != WSAStartup(MAKEWORD(2, 2), &wd)) {
		return false;
	}
	if (LOBYTE(wd.wVersion) != 2 || HIBYTE(wd.wVersion) != 2) {
		return false;
	}
	m_socket = socket(AF_INET, SOCK_STREAM, 0);
	if (m_socket == INVALID_SOCKET) {
		return false;
	}
	return true;
}

bool RequestHttp::GetHtml(string& html) {
	string info;
	info = info + "GET " + m_object+" HTTP/1.1\r\n";
	info = info + "Host: " + m_host + "\r\n";
	info = info + "Connection: close\r\n";
	info = info + "User-Agent: " + "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36\r\n";
	info = info + "\r\n";

	if (SOCKET_ERROR == send(m_socket, info.c_str(), info.length(), 0))
		return false;

	char ch = 0;
	while (recv(m_socket, &ch, sizeof(char), 0)) {
		html += ch;
	}


	return true;
}

int main() {



	// 创建文件夹
	// CreateDirectory(L"aaa", NULL);

	string url;
	url = "http://www.baidu.com/s?wd=123456";
	StartCrawl(url);

	getchar();
	return 0;
}

bool StartCrawl(std::string url) {
	//queue<std::string> q;
	//q.push(url);

	//while (!q.empty()) {
	//	string c_url = q.front();
	//	q.pop();
	//	RequestHttp http;
	//	http.InitNet();
	//	http.AnalyseUrl(c_url);
	//}
	string html;

	RequestHttp http;
	http.InitNet();
	http.AnalyseUrl(url);
	http.Connect();
	http.GetHtml(html);
	cout << html << endl;
	return true;
}


