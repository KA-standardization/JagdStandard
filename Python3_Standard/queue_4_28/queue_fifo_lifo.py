import queue

q1 = queue.Queue()
for i in range(5):
    q1.put(i)

while not q1.empty():
    print(q1.get())
print('=' * 90)

q2 = queue.LifoQueue()
for i in range(5):
    q2.put(i)
while not q2.empty():
    print(q2.get())
