import numpy as np
from mpi4py import MPI as mpi_

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

neighbour_processes = [0, 0, 0, 0]

if __name__ == '__main__':
    comm = mpi_.COMM_WORLD
    rank = comm.rank
    size = comm.size

    grid_rows = int(np.floor(np.sqrt(comm.size)))
    grid_column = comm.size // grid_rows

    if grid_rows * grid_column > size:
        grid_column -= 1
    if grid_rows * grid_column > size:
        grid_rows -= 1

    if rank == 0:
        print('Building a %d x %d grid topology:' % (grid_rows, grid_column))
    cartesian_communicator = comm.Create_cart((grid_rows, grid_column), periods=(False, False), reorder=True)

    my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(cartesian_communicator.rank)
    neighbour_processes[UP], neighbour_processes[DOWN] = cartesian_communicator.Shift(0, 1)
    neighbour_processes[LEFT], neighbour_processes[RIGHT] = cartesian_communicator.Shift(1, 1)

    print(
        'Process {}, row {}, column {}--> neighbour_process[UP]={}, neighbour_process[DOWN]={}, neighbour_process[LEFT]={}, neighbour_process[RIGHT]={}'.format(
            rank, my_mpi_row, my_mpi_col, neighbour_processes[UP], neighbour_processes[DOWN], neighbour_processes[LEFT],
            neighbour_processes[RIGHT]))
