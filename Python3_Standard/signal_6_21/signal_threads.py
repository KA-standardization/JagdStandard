import os
import time
import signal
import threading


def signal_handler(num, stack):
    print('Received signal {} in {}'.format(
        num, threading.currentThread().name))


signal.signal(signal.SIGUSR1, signal_handler)


# 只有进程的主线程可以接收信号, 子线程pause()只会无线阻塞
def wait_for_signal():
    print('Waiting for signal in', threading.currentThread().name)
    signal.pause()
    print('Done waiting')


receiver = threading.Thread(
    target=wait_for_signal,
    name='receiver',
)
receiver.start()
time.sleep(0.1)


def send_signal():
    print('Sending signal in', threading.currentThread().name)
    os.kill(os.getpid(), signal.SIGUSR1)


sender = threading.Thread(target=send_signal, name='sender')
sender.start()
sender.join()

print('Waiting for', receiver.name)
signal.alarm(2)
receiver.join()
