package main

import "sync"
import "time"

func main() {
	total := 0
	var mu sync.Mutex
	for i := 0; i < 1000; i++ {
		go func() {
			mu.Lock()
			defer mu.Unlock()
			total = total + 1
		}()
	}
	// ********
	time.Sleep(1 * time.Second)
	mu.Lock()
	println(total)
	mu.Unlock()

}
