from scapy.all import *

p = sr1(IP(dst='114.114.114.114') / UDP() / DNS(rd=1, qd=DNSQR(qname="www.baidu.com")))
print(p)
