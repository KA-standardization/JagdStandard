package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

var m = map[int]string{
	1: "http://www.baidu.com",
	2: "http://www.zhihu.com",
	3: "http://www.weibo.com",
}

func main() {
	for _, url := range m {
		resq, err := http.Get(url)
		if err != nil {
			fmt.Fprintf(os.Stderr, "error: %v\n", err)
			os.Exit(1)
		}
		body, err := ioutil.ReadAll(resq.Body)
		resq.Body.Close()
		if err != nil {
			fmt.Fprintf(os.Stderr, "error: %v\n", err)
			os.Exit(1)
		}
		fmt.Printf("%s\n", body)
	}
}
