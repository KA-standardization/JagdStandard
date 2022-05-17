import time
import multiprocessing

import zmq


def foo(mun):
    # sum = 0
    # for i in range(1000000):
    #     sum += i
    return mun


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

            result_sender.send_pyobj(obj[0](obj[1]))


if __name__ == '__main__':
    processes = []
    for x in range(8):
        p = multiprocessing.Process(target=worker, daemon=True)
        p.start()
        processes.append(p)

    print(processes)

    while 1:
        pass
    for p in processes:
        p.terminate()
