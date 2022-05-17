package main

import "time"

func main() {
	time.Sleep(1 * time.Second)
	println("start")
	go periodic()
	time.Sleep((5 * time.Second))

}

func periodic() {
	for {
		println("tick")
		time.Sleep(1 * time.Second)
	}
}
