package main

import (
	"fmt"
	"net/http"
)

func main(){
	req,_:=http.Get("https://www.baidu.com")
	fmt.Println(req)
}
