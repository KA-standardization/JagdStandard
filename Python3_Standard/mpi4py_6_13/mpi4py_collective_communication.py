from mpi4py import MPI as mpi_

comm = mpi_.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    variable_to_share = 100
else:
    variable_to_share = None

variable_to_share = comm.bcast(variable_to_share, root=0)
print('process={}, variable={}'.format(rank, variable_to_share))
