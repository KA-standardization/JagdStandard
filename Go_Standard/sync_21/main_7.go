package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	hong := 10000
	ming := 10000
	var mu sync.Mutex

	total := hong + ming
	go func() {
		for i := 0; i < 1000; i++ {
			mu.Lock()
			hong -= 1
			mu.Unlock()
			mu.Lock()
			ming += 1
			mu.Unlock()
		}
	}()
	go func() {
		for i := 0; i < 1000; i++ {
			mu.Lock()
			ming -= 1
			mu.Unlock()
			mu.Lock()
			hong += 1
			mu.Unlock()
		}
	}()
	//time.Sleep(50 * time.Millisecond)
	start := time.Now()
	for time.Since(start) < 1*time.Second {
		mu.Lock()

		if hong+ming != total {
			fmt.Printf("hong = %v\n ming = %v\nsum = %v\n", hong, ming, hong+ming)
		}
		mu.Unlock()
		time.Sleep(50 * time.Millisecond)
	}

}
