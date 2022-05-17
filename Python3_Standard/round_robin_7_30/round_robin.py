import roundrobin

'''
>>> import roundrobin
>>> get_roundrobin = roundrobin.basic(["A", "B", "C"])
>>> ''.join([get_roundrobin() for _ in range(7)])
'ABCABCA'
>>> # weighted round-robin balancing algorithm as seen in LVS
>>> get_weighted = roundrobin.weighted([("A", 5), ("B", 1), ("C", 1)])
>>> ''.join([get_weighted() for _ in range(7)])
'AAAAABC'
>>> # smooth weighted round-robin balancing algorithm as seen in Nginx
>>> get_weighted_smooth = roundrobin.smooth([("A", 5), ("B", 1), ("C", 1)])
>>> ''.join([get_weighted_smooth() for _ in range(7)])
'AABACAA'
'''

services = ['A', 'B', 'C', 'D']
g = roundrobin.basic(services)
for _ in range(7):
    print(g())
print('=' * 88)
# get_weighted_smooth = roundrobin.smooth([("A", 5), ("B", 1), ("C", 1)])
#
# for _ in range(7):
#     print(get_weighted_smooth())
