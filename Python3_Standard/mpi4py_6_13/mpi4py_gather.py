from mpi4py import MPI as mpi_

comm = mpi_.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = (rank + 1) ** 2

data = comm.gather(data, root=0)

if rank == 0:
    print('rank={}'.format(rank))
    for i in range(1, size):
        value = data[i]
        print('process {} receiving {} from process {}'.format(rank, value, i))
