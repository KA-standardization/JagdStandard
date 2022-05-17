package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
)

var m = map[int]string{
	1: "http://www.baidu.com",
	2: "http://www.zhihu.com",
	3: "http://www.weibo.com",
}

func main() {
	ch := make(chan string)
	for _, url := range m {
		go fetch(url, ch)
	}
	for range m {
		fmt.Println(<-ch)
	}
}

func fetch(url string, ch chan<- string) {
	resp, err := http.Get(url)
	if err != nil {
		ch <- fmt.Sprint(err)
		return
	}
	nbytes, err := io.Copy(ioutil.Discard, resp.Body)
	resp.Body.Close()
	if err != nil {
		ch <- fmt.Sprint("while reading %s: %v", url, err)
	}
	ch <- fmt.Sprintf("%7d %s", nbytes, url)
}
