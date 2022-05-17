package main

import "sync"

func main(){
	var wg sync.WaitGroup
	for i:=0;i<5;i++{
		wg.Add(i)
		go func(x int) {
			sendPrint(x)
			wg.Done()
		}(i)
	}
}

func sendPrint(i int){
	println(i)
}
