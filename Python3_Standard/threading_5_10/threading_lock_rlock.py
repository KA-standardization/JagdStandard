import threading

lock = threading.Lock()
print(lock.acquire())
print(lock.acquire(0))
print('=' * 88)
lock2 = threading.RLock()
print(lock2.acquire())
print(lock2.acquire(0))
