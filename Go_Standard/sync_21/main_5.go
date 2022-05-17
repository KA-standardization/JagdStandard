package main

func main() {
	total := 0
	for i := 0; i < 1000; i++ {
		go func() {
			total = total + 1
		}()
	}
	println(total)
}
