import numpy
from mpi4py import MPI as mpi_

comm = mpi_.COMM_WORLD
size = comm.size
rank = comm.rank

array_size = 10

recvdata = numpy.zeros(array_size, dtype=numpy.int)
senddata = (rank + 1) * numpy.arange(array_size, dtype=numpy.int)

print('process {} sending {}'.format(rank, senddata))
# MAX MIN SUM PROD LAND MAXLOC MINLOC
comm.Reduce(senddata, recvdata, root=0, op=mpi_.SUM)
print(rank, recvdata)
