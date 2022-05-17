import pickle
import random
import multiprocessing

import zmq


def foo(i):
    pass


context = zmq.Context()
work_sender = context.socket(zmq.PUSH)
work_sender.bind("tcp://*:9555")
result_receiver = context.socket(zmq.PULL)
result_receiver.bind("tcp://*:9556")
for x in range(8):
    work_sender.send_pyobj((foo, x))

res = []
for x in range(8):
    res.append(result_receiver.recv())
print([pickle.loads(r) for r in res])
