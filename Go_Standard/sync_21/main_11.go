package main

import "sync"

func main() {
	var wg sync.WaitGroup
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func(x int) {
			sendRPC2(x)
			wg.Done()
		}(i)
	}
	wg.Wait()

}

func sendRPC2(i int) {
	println(i)
}
