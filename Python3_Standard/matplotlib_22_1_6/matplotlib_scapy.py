import matplotlib.pyplot as plt
from scapy.all import *

a, b = sr(IP(dst="10.0.17.200") / TCP(sport=[RandShort()] * 10))
a.plot(lambda x: x[1].id)
