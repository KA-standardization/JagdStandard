import random
import multiprocessing

import zmq


def foo():
    sum = 0
    for i in range(1000000):
        sum += i
    return sum


def worker():
    context = zmq.Context()
    work_receiver = context.socket(zmq.PULL)
    work_receiver.connect("tcp://127.0.0.1:9555")

    result_sender = context.socket(zmq.PUSH)
    result_sender.connect("tcp://127.0.0.1:9556")
    poller = zmq.Poller()
    poller.register(work_receiver, zmq.POLLIN)
    while True:
        socks = dict(poller.poll())
        if socks.get(work_receiver) == zmq.POLLIN:
            obj = work_receiver.recv_pyobj()
            result_sender.send_pyobj(obj())


context = zmq.Context()
work_sender = context.socket(zmq.PUSH)
work_sender.bind("tcp://*:9555")
result_receiver = context.socket(zmq.PULL)
result_receiver.bind("tcp://*:9556")

processes = []
for x in range(8):
    p = multiprocessing.Process(target=worker, )
    p.start()
    processes.append(p)

for x in range(8):
    work_sender.send_pyobj(foo)

res = []
for x in range(8):
    res.append(result_receiver.recv())
for p in processes:
    p.terminate()
print(res)
