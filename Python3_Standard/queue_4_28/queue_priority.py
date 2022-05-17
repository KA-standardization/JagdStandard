import queue
import functools
import threading


@functools.total_ordering
class Job(object):
    def __init__(self, priority, desc):
        self.priority = priority
        self.desc = desc
        print('New ', desc)
        return

    def __eq__(self, other):
        try:
            return self.priority == other.priority
        except AttributeError:
            return NotImplemented

    def __lt__(self, other):
        try:
            return self.priority < other.priority
        except AttributeError:
            return NotImplemented


q = queue.PriorityQueue()
q.put(Job(3, 'affe'))
q.put(Job(11, 'Idee'))
q.put(Job(1, 'Boot'))
q.put(Job(5, 'ohne'))
q.put(Job(7, 'toll'))


def process_jop(q):
    while True:
        next_job = q.get()
        print(next_job.desc)
        q.task_done()


workers = [
    threading.Thread(target=process_jop, args=(q,)),
    threading.Thread(target=process_jop, args=(q,)),
]

for w in workers:
    w.setDaemon(True)
    w.start()

q.join()
