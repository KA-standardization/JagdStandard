package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"net/url"
)

var base_url = "http://whosecard.com:8081/api/msg/ext?key=86050c5b8eac1ca0ad4abdac8a2778861b2d12e91ad78b90196b7627&url="

var w = map[string]string{
	"a": base_url + url.QueryEscape("http://mp.weixin.qq.com/s?__biz=Mzg4OTU4ODA1Ng==&amp;mid=2247490180&amp;idx=7&amp;sn=c4e29cd90791d745f508e86f0750d49d&amp;chksm=cfe8cab3f89f43a5983c91a7b9b8f1866e817054fd72ad62b921ab925dfec3b00a970316f0a4#rd"),
	"b": base_url + url.QueryEscape("http://mp.weixin.qq.com/s?__biz=Mzk0MDI0ODAwMw==&amp;mid=2247484036&amp;idx=1&amp;sn=d48ec97719b77728d9c7736d309e0bcd&amp;chksm=c2e5dc28f592553ee9f1b5dfbd88344871e03a94e386ab6eb74a074f94f566a0a354a97d1bf5#rd"),
	"c": base_url + url.QueryEscape("http://mp.weixin.qq.com/s?__biz=MzkzMDIyODc1OA==&amp;mid=2247486912&amp;idx=5&amp;sn=1b166ba8ecb911a7f8d1988bd8eafcd8&amp;chksm=c27c32b9f50bbbaf65d57654e37bae25d9f6cd1b4355c457fb4e47fcda9d027a0430e641ccc7#rd"),
}

type iww struct {
	AdvertisementInfo []interface{} `json:"advertisementInfo"`
	AdvertisementNum  interface{}   `json:"advertisementNum"`
	CanReward         int           `json:"canReward"`
	ClicksCount       int           `json:"clicksCount"`
	Cost              bool          `json:"cost"`
	LikeCount         int           `json:"likeCount"`
	Ok                bool          `json:"ok"`
	OldLikeCount      int           `json:"oldLikeCount"`
	RetCode           int           `json:"retCode"`
	RewardTotalCount  interface{}   `json:"rewardTotalCount"`
	Top               int           `json:"top"`
	UserCanReward     interface{}   `json:"userCanReward"`
}
var iii iww
func main() {
	ch := make(chan string)
	for _, url_ := range w {
		go fetch_weixin(url_, ch)
	}
	for range w {
		tmp := <-ch
		fmt.Println(tmp)
		data  := []byte(tmp)
		json.Unmarshal(data,&iii)
		//fmt.Println(iii)
		fmt.Println(iii.ClicksCount)
		fmt.Println(iii.LikeCount)
		fmt.Println(iii.OldLikeCount)
		//fmt.Println(d)
	}
}

func fetch_weixin(url string, ch chan<- string) {
	resp, err := http.Get(url)
	if err != nil {
		ch <- fmt.Sprint(err)
		return
	}
	body, err := ioutil.ReadAll(resp.Body)
	resp.Body.Close()
	if err != nil {
		ch <- fmt.Sprint("while reading %s: %v", url, err)
	}
	ch <- fmt.Sprintf("%v", string(body))
	//ch <- fmt.Sprintf("%v", body)
}
