from mpi4py import MPI as mpi_

comm = mpi_.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    array_to_share = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
else:
    array_to_share = None

recvbuf = comm.scatter(array_to_share, root=0)
print("process={}, recvbuf={}".format(rank, recvbuf))

print('=' * 88)

recvbuf = comm.scatterv([array_to_share, len(array_to_share), int], root=0)
print("process={}, recvbuf={}".format(rank, recvbuf))
