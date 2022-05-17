import signal

signal_to_name = {getattr(signal, n): n for n in dir(signal) if n.startswith('SIG') and '_' not in n}

for k, v in sorted(signal_to_name.items()):
    handler = signal.getsignal(k)
    print('{:<10} {:2d}:'.format(v, k), handler)
