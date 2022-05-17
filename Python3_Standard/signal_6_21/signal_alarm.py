import time
import signal


def recv_alarm(signum, stack):
    print('Alarm : ', time.ctime())


signal.signal(signal.SIGALRM, recv_alarm)
signal.alarm(2)

print('Before', time.ctime())
time.sleep(4)
print('After', time.ctime())
