# print(hex(0))

print(1>>1)
print(1<<1)

print(2>>1)

import time
print(time.time_ns())
time.sleep(0.01)
print(time.time_ns())
time.sleep(0.2)
print(time.time_ns())

print(time.time())
print(time.thread_time())
