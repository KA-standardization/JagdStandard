import multiprocessing
import time
import pickle
import zmq


def foo(mun):
    sum = 0
    for i in range(1000000):
        sum += i
    for j in range(999999):
        sum -= j
    return mun * 10


def worker():
    context = zmq.Context()
    work_receiver = context.socket(zmq.PULL)
    work_receiver.connect("tcp://10.0.17.100:9555")

    result_sender = context.socket(zmq.PUSH)
    result_sender.connect("tcp://10.0.17.100:9556")
    poller = zmq.Poller()
    poller.register(work_receiver, zmq.POLLIN)
    while True:
        socks = dict(poller.poll())
        if socks.get(work_receiver) == zmq.POLLIN:
            obj = work_receiver.recv_pyobj()
            result_sender.send_pyobj(obj[0](obj[1]))


def sender(ip, megs):
    context = zmq.Context()
    work_sender = context.socket(zmq.PUSH)
    work_sender.bind("tcp://" + ip + ":9555")
    result_receiver = context.socket(zmq.PULL)
    result_receiver.bind("tcp://" + ip + ":9556")
    for x in megs:
        work_sender.send_pyobj((foo, x + 1))

    res = []
    for _ in range(len(megs)):
        res.append(result_receiver.recv())
    print([pickle.loads(r) for r in res])


if __name__ == '__main__':
    # nohup /alidata/server/imfaker/.venv/bin/python /partita/zhihu/zhihu/task_es/z_slave.py > z_slave.log 2>&1&
    start_time = time.time()
    processes = []
    for x in range(30):
        p = multiprocessing.Process(target=worker)
        p.start()
        processes.append(p)

    ms = [0, 0, 0, 11, 14, 222, 111, 333, 4444, 556, 78, 123, 134, 123, 698, 11, 12, 11, 11, 14, 222, 111, 333, 4444,
          556, 78, 123, 134, 123, 698]
    sender('10.0.17.100', ms)

    # while 1:
    #     pass
    for p in processes:
        # p.join()
        p.terminate()
    end_time = time.time()
    print("Used-->{}".format(end_time - start_time))
