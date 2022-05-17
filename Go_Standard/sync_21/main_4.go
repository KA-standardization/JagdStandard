package main

import (
	"sync"
	"time"
)

var done bool

var mu sync.Mutex

func main(){
	time.Sleep(1*time.Second)
	println("start")
	go periodict()
	time.Sleep(5*time.Second)
	mu.Lock()
	done=true
	mu.Unlock()
	println("cancelled")
	//time.Sleep(3*time.Second)
}

func periodict(){
	for{
		println("tick")
		time.Sleep(1*time.Second)
		mu.Lock()
		if done{
			return
		}
		mu.Unlock()
	}
}