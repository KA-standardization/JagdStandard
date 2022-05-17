from mpi4py import MPI as mpi_

comm = mpi_.COMM_WORLD
rank = comm.rank

print('RANK num: {}'.format(rank))

if rank == 0:
    data = 24000
    destination_process = 4
    comm.send(data, dest=destination_process)

if rank == 1:
    data = 'jagd'
    destination_process = 8
    comm.send(data, dest=destination_process)

if rank == 4:
    recv_data = comm.recv(source=0)
    print('received 0:', recv_data)

if rank == 8:
    recv_data2 = comm.recv(source=1)
    print('received 1:', recv_data2)
