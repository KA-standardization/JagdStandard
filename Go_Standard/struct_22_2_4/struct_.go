package main

import (
	"fmt"
	"time"
)

/*



 */

type Element struct {
	ID   int
	Name string
	Dob  time.Time
}

func main() {
	var elem Element
	var elem2 Element
	elem.ID = 1001
	elem2.ID = 2001
	elem.Name = "abc"
	elem.Dob = time.Now()
	fmt.Printf("%d--%s--%f\n", elem.ID, elem.Name, elem.Dob)
	fmt.Printf("%T\n",elem)
}
