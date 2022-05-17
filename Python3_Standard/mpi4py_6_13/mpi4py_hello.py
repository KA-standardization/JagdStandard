from mpi4py import MPI as mpi_

comm = mpi_.COMM_WORLD

rank = comm.Get_rank()

node_name = mpi_.Get_processor_name()

print('hello world from process:', rank)

print(node_name)