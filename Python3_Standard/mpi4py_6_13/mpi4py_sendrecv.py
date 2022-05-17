from mpi4py import MPI as mpi_

comm = mpi_.COMM_WORLD

rank = comm.rank

if rank == 1:
    data_send = "abcde"
    destination_process = 5
    source_process = 5
    data_sendrecv = comm.sendrecv(data_send, dest=destination_process, source=source_process)

if rank == 5:
    data_send = 'qwertyui'
    destination_process = 1
    source_process = 1
    data_sendrecv = comm.sendrecv(data_send, dest=destination_process, source=source_process)


