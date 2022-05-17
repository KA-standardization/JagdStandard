import multiprocessing


def do_calculation(data):
    return data * 2


def start_process():
    print('Starting', multiprocessing.current_process().name)


if __name__ == '__main__':
    inputs = list(range(10))

    builtin_outputs = list(map(do_calculation, inputs))
    print(builtin_outputs)

    pool_size = multiprocessing.cpu_count() * 2
    # pool = multiprocessing.Pool(processes=pool_size, initializer=start_process)
    pool = multiprocessing.Pool(processes=pool_size, initializer=start_process, maxtasksperchild=2)

    pool_outputs = pool.map(do_calculation, inputs)

    # 使任务进程与主进程同步
    pool.close()
    pool.join()

    print(pool_outputs)
