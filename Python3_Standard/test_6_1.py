# s = input().strip()
#
# tmp = dict()
#
# for item in s:
#     if tmp.get(item):
#         tmp.pop(item)
#     else:
#         tmp[item] = 1
#
# print(len(tmp.keys()))

"""
2
01:41:8.9
1:1:09.211
"""

# import sys
#
# if __name__ == "__main__":
#     n = int(sys.stdin.readline().strip())
#     tmp = []
#     for i in range(n):
#         line = sys.stdin.readline().strip()
#         t_h, t_m, t_s = line.split(':')
#         time_ = int(t_h) * 3600 + int(t_m) * 60 + float(t_s)
#         tmp.append(line + '/' + str(time_))
#
#     res = sorted(tmp, key=lambda x: float(x.split('/')[-1]))
#     for item in res:
#         print(item.split('/')[0])


import sys

if __name__ == "__main__":
    for i in range(2):
        line = sys.stdin.readline().strip()
        if i == 0:
            s_list = "[" + line + "]"
        else:
            t = int(line)

    task_list = eval(s_list)
    task_dict = dict()
    for item in task_list:
        if not task_dict.get(item):
            task_dict[item] = 1
        else:
            task_dict[item] += 1
    a = dict(sorted(task_dict.items(), key=lambda x: x[-1], reverse=True))
    tmp = 0
    keys = list(a.keys())
    for i in range(len(task_list)):
        if a.get(keys[0]) == 0:
            a.pop(keys[0])

        if a.get(keys[0]):
            if i == 0:
                tmp += 1
                a[keys[0]] -= 1
            else:
                if a.get(keys[-1]) and (keys[-1] != keys[0]):
                    a[keys[-1]] -= 1
                tmp += 3
                a[keys[0]] -= 1

    print(tmp)
