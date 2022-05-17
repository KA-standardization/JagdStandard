import numpy
from mpi4py import MPI as mpi_

comm = mpi_.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

senddata = (rank + 1) * numpy.arange(size, dtype=int)
recvdata = numpy.empty(size, dtype=int)

comm.Alltoall(senddata, recvdata)

print('process{}, sending{}, receiving{}'.format(rank, senddata, recvdata))
