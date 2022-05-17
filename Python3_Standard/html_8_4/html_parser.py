# -*- coding:utf-8 -*-
from html.parser import HTMLParser
from html.entities import name2codepoint

data = '<p>我个人观感挺差的，全程都很尴尬，忍不住想吐槽。</p><p>最大的一点在于，明明是一部主旋律，是用来弘扬铁道兵的电影，我看完最大的感受却是一句很公知的名言，请等等你的人民。所以说为什么我们国家被称为基建狂魔，土木工程却被称为提桶跑路专业呢？就是在电影里，明明只是一份工作，却总是在无限拔高牺牲奉献。在激动人心的宏大叙事下，又有谁会来关心每一个受苦的个体呢？</p><p>几处不合理的点：</p><p>男主角一个人去山上给传感器换电池。就算你家装个空调外机，都要两个人吧，这样真的附和安全操作嘛？</p><p>男主他爸，有点过于刻意的塑造死板不讲理的性格，救人前段还让人感动，后来不听劝阻，对消防队指指点点，私自下去救人，就开始让我讨厌了。</p><p>张国立演的大领导我也没看出来他体现出来的作用，完全是个啥也不懂的外行，也许领导是用来下重要决定的，担责任的，但是电影完全没有提现这一点。他的镜头全是浪费时间。</p><p>我一直不太清楚大家为什么会对炸高铁隧道那么反感，如果我是包工头，大家都是为了赚钱的。只要政府给钱，炸了再造，只要有活做不就是最开心的事情。</p>'
data2 = '<p></p><figure data-size="normal"><noscript><img src="https://pic1.zhimg.com/v2-29247d198905aea0271532b84078810d_b.jpg" data-caption="" data-size="normal" data-rawwidth="1080" data-rawheight="719" data-default-watermark-src="https://pic4.zhimg.com/v2-560fb59b51d6b59ddda451c3796ca178_b.jpg" class="origin_image zh-lightbox-thumb" width="1080" data-original="https://pic1.zhimg.com/v2-29247d198905aea0271532b84078810d_r.jpg"/></noscript><img src="data:image/svg+xml;utf8,&lt;svg xmlns=&#39;http://www.w3.org/2000/svg&#39; width=&#39;1080&#39; height=&#39;719&#39;&gt;&lt;/svg&gt;" data-caption="" data-size="normal" data-rawwidth="1080" data-rawheight="719" data-default-watermark-src="https://pic4.zhimg.com/v2-560fb59b51d6b59ddda451c3796ca178_b.jpg" class="origin_image zh-lightbox-thumb lazy" width="1080" data-original="https://pic1.zhimg.com/v2-29247d198905aea0271532b84078810d_r.jpg" data-actualsrc="https://pic1.zhimg.com/v2-29247d198905aea0271532b84078810d_b.jpg"/></figure><p>《逃离》这本短篇小说集还是我在成都的时候种草的，直到现在也没拔干净，只看了第一篇小说，最初看的时候，并不觉得如何，历经岁月才觉得告别过去真的不是一件容易的事儿。</p><p>五一的时候，把我弟叫来上海，那天我们俩坐在江边城外吃烤鱼，聊着聊着，终于问到了这三年来我一直想问的问题，这似乎已经成了我的一个心病了。</p><p>14年的时候，我弟高考，成绩还算不错，虽说够不着电子科大，但去北京交大之类还是没问题的。我在家琢磨了好半天，填报志愿的时候，什么因素都考虑了，该冲一冲的，该保守的，万没想到，他在临结束的一刻，改了太原理工这么个学校，我觉得特别地惋惜。</p><p>在面对十字路口的时候，无论别人如何劝谏，你我大概都有着自己的想法和判断，这并不重要，重要的是能够在选择之后享受自己得到的，坦然放下自己失去的。</p><p>在那之后，很多次我都问过他为什么要这样做，可都没有得到回答。</p><p>那天吃烤鱼，或许是多年未见吧，终于能够坦然说说这件事儿了。</p><p>老弟在高中的时候喜欢上一个女生，那女生的一句玩笑话“瞧瞧那某某成绩那么好”，让他心里的嫉妒作祟，再也没有让自己从年级第一的位置掉下来，他自己都觉得考这么高的成绩是该感谢这女孩子的。</p><p>我也这样觉得。</p><p>爱情，在年轻人心里是崇高的，所以，他义无反顾的报考了和她仅有一墙之隔的太原理工。</p><p>纯粹的爱情很脆弱，脆弱地经不起一丁点儿不算波折的波折。看着弟坐在对面流着泪诉说往事，我没有感到忧伤，人生总得经历爱情和失去爱情。</p><p>他比我幸运。</p><p>距离那段感情已经快二个年头了，我总感觉他还没放下，大概，等他把昵称改了，那就是真的从这段感情里走出来了。</p><p>离别，是伤感的。</p><figure data-size="normal"><noscript><img src="https://pic1.zhimg.com/v2-39c8c67232cf8cb9791f1707ac8996e7_b.jpg" data-caption="" data-size="normal" data-rawwidth="1080" data-rawheight="613" data-default-watermark-src="https://pic2.zhimg.com/v2-fff49092bf761e6c0d54a6d8af205bfa_b.jpg" class="origin_image zh-lightbox-thumb" width="1080" data-original="https://pic1.zhimg.com/v2-39c8c67232cf8cb9791f1707ac8996e7_r.jpg"/></noscript><img src="data:image/svg+xml;utf8,&lt;svg xmlns=&#39;http://www.w3.org/2000/svg&#39; width=&#39;1080&#39; height=&#39;613&#39;&gt;&lt;/svg&gt;" data-caption="" data-size="normal" data-rawwidth="1080" data-rawheight="613" data-default-watermark-src="https://pic2.zhimg.com/v2-fff49092bf761e6c0d54a6d8af205bfa_b.jpg" class="origin_image zh-lightbox-thumb lazy" width="1080" data-original="https://pic1.zhimg.com/v2-39c8c67232cf8cb9791f1707ac8996e7_r.jpg" data-actualsrc="https://pic1.zhimg.com/v2-39c8c67232cf8cb9791f1707ac8996e7_b.jpg"/></figure><p>我大概遇到过很多很多人，深陷泥潭而无法自拔。</p><p>手里攥着的那份感情已然不是自己喜欢的了，很长时间不说话，不打招呼，不联系，可就是不愿意把那句“分手”说出口，冷着别人，也冷着自己的心。</p><p>《再见，南屏晚钟》里的那位母亲把这样的“离别”发挥到了极致，心里的执念那样深，深到宁可相信邪教，也不愿打破这死水一样的婚姻，把自己满腔的委屈怨恨一股脑儿发泄到自己女儿身上。</p><p>那位父亲也是，打着为女儿好的幌子不愿破镜，可这样的强扭大概只会让自己女儿更难受。</p><p>这些人还留着幻象，以为一切都还能够变回原来初恋的样子。或许，对他们来说，爱情原不是生活的必需品。</p><p>《逃离》的女主人公就要踏上远去的火车了，临门一脚改了主意。</p><p>人，是害怕未知的，现在的生活固然艰辛，如果自己迈出了这一步，迎面而来的又将会是怎样的狂风暴雨呢？</p><p>习惯是可怕的；离别，是艰难的。</p><figure data-size="normal"><noscript><img src="https://pic2.zhimg.com/v2-b2f04cae89e92a59b4f86c2bd909776c_b.jpg" data-caption="" data-size="normal" data-rawwidth="1080" data-rawheight="719" data-default-watermark-src="https://pic1.zhimg.com/v2-18e4b8dc8aa74b8651baf0b774045970_b.jpg" class="origin_image zh-lightbox-thumb" width="1080" data-original="https://pic2.zhimg.com/v2-b2f04cae89e92a59b4f86c2bd909776c_r.jpg"/></noscript><img src="data:image/svg+xml;utf8,&lt;svg xmlns=&#39;http://www.w3.org/2000/svg&#39; width=&#39;1080&#39; height=&#39;719&#39;&gt;&lt;/svg&gt;" data-caption="" data-size="normal" data-rawwidth="1080" data-rawheight="719" data-default-watermark-src="https://pic1.zhimg.com/v2-18e4b8dc8aa74b8651baf0b774045970_b.jpg" class="origin_image zh-lightbox-thumb lazy" width="1080" data-original="https://pic2.zhimg.com/v2-b2f04cae89e92a59b4f86c2bd909776c_r.jpg" data-actualsrc="https://pic2.zhimg.com/v2-b2f04cae89e92a59b4f86c2bd909776c_b.jpg"/></figure><p>Elliot就生活在一个《再见，南屏晚钟》式的家庭，爸爸是同性恋，婚姻是母亲的一切。</p><p>十多年里，他们在一起勉强着生活，母亲为了挽留这份婚姻，做了自己能做的所有的事情。爱情自始至终都是无法勉强的，Elliot的父亲无论如何都不会也不可能爱上她。</p><p>那年夏天，Elliot和母亲来到他们每年都会来的法国小镇，经过这么多年的挣扎，他们终于决定要分离，就以售卖这栋曾经纪念着美好的小别墅为起点，开始自己全新的生活。</p><p>影片有一种淡淡的忧伤。爱情一开始的时候都是那么动人心魄，我们被容貌、谈吐、学识亦或那份勇气所吸引，爱上的时候，我们甚至可以放弃生命。不论结局，曾经的时光岁月永远都是那么美好。</p><p>Elliot的父母要告别过去，这确实是件伤感的事，可是，他们能够面对自己已经破碎的婚姻，决定与这些悲伤诀别，不得不说又是件值得高兴的事。</p><p>大抵生活原应如此吧，当爱情来临的时候，敞开胸怀尽情享受；如果有一天爱情不在了，那就鼓足勇气坦然放下。或许不只爱情，其他的也是如此。沉浸在过去的美好亦或悲伤，并不能让生活变得更好。把过去的所有拾掇拾掇，装在盒子里，藏在记忆深处，才能让自己迎接下一份幸福和快乐。</p><p>《离别是美丽的》；离别，是美丽的。</p>'
data3 = '<a>这是莱昂纳多演哪个？</a>'

d = '<p style="text-align: justify;">首先在平时的日常生活当中，我们要去保持一个规律的生活作息习惯，其次，我们要有一个健康的饮食习惯，但是和你的血压长时间处于一个升高的状态，得不到我们的控制的时候，那么就需要合理的去利用降压药来把血压降下去，其次再选择降压药的这一个方面，一定要去根据医生的治疗来进行吃药，不能够自己盲目的去选择药物，这样的话，不仅会对血压起不到一个很好的控制，还很可能会引发更严重的一些疾病。</p><p style="margin-top: -40em;margin-right: 100em;margin-bottom: -4em;font-size: 1em;font-weight: inherit;white-space: normal;width: 10em;height: 2em;line-height: 2em;text-align: center;text-decoration: inherit;color: rgb(255, 255, 255);border-color: rgb(255, 255, 255);float: right;background-color: rgb(197, 63, 70);transform: rotate(45deg);-webkit-transform: rotate(45deg);-moz-transform: rotate(45deg);-ms-transform: rotate(45deg);-o-transform: rotate(45deg);">总结的来说, 这是不可避免的. 既然如此, 我们一般认为, 抓住了问题的关键, 其他一切则会迎刃而解.</p>'


class MyHTMLParser(HTMLParser):
    s = ''
    ps = ''

    #
    # def handle_starttag(self, tag, attrs):
    #     print(self.rawdata)
    #     if tag == 'p':
    #         for attr in attrs:
    #             if attr[1].startswith('margin'):
    #                 break
    #             print(attr,'---',tag)
    #             if tag == 'img' and attr[1].endswith('jpg'):
    #                 self.ps += (attr[1] + ' ')
    #                 break

    def handle_data(self, data):
        if self.get_starttag_text().find('margin') == -1:
            self.s += data

    def __call__(self):
        tmp = self.s + ' ' + self.ps
        self.s = ''
        self.ps = ''
        return tmp


parser = MyHTMLParser()

parser.feed(d)
print(parser.__call__())
parser.feed(data3)
print(parser.__call__())
