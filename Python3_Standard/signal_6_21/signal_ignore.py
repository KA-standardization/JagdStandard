import os
import time
import signal


def do_exit(signum, stack):
    raise SystemExit('Exiting')


# 将SIGINT的默认处理器替换为SIG_IGN
signal.signal(signal.SIGINT, signal.SIG_IGN)

signal.signal(signal.SIGUSR1, do_exit)

print('My PID:', os.getpid())
signal.pause()
