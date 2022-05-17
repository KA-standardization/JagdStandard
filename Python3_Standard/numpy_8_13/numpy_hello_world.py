import time
import numpy as np


def used_time():
    tmp_ = []
    start_time = time.time()
    [x * 2 for x in np.arange(1000000)]
    # [x * 2 for x in range(1000000)]
    end_time = time.time()
    print('Used time: {}'.format(end_time - start_time))


if __name__ == '__main__':
    used_time()
    import pandas as pd
