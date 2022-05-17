import multiprocessing


class Worker(multiprocessing.Process):

    def run(self):
        print('IN {} {}'.format(self.name, self.pid))
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = Worker()
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
