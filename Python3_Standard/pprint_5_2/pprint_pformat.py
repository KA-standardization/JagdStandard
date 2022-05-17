import logging
from pprint import pformat

data = [
    (1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
    (2, {'e': 'E'}),
]

logging.basicConfig(level=logging.DEBUG, format='%(levelname) -8s %(message)s')

logging.debug('Logging pformatted data')
formatted = pformat(data)
print(formatted)
for line in formatted.splitlines():
    logging.debug(line.rstrip())
