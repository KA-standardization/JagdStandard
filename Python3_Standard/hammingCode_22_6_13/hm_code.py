# LDPC
import numpy as np
import numba as nb

zero_res = np.zeros((4, 4))


# @nb.jit(nopython=True)
def hm(array_):
    global_page = np.sum(array_)
    global_ = array_[0][0]

    tmp_2_0 = None
    tmp_2_1 = None
    tmp_2_2 = None
    tmp_2_3 = None

    if (global_page % 2 != 0 and global_ == 0) or (global_page % 2 == 0 and global_ == 1):
        print("[Error]:  global")
        # search 2^0
        s_2_0 = np.c_[array_[:, 1], array_[:, 3]]
        g_p_2_0 = np.sum(s_2_0)
        g_2_0 = s_2_0[0][0]
        if (g_p_2_0 % 2 != 0 and g_2_0 == 0) or (g_p_2_0 % 2 == 0 and g_2_0 == 1):
            print("[Error]: 2^0")
            # tmp_2_0 = s_2_0

        # search 2^1
        s_2_1 = np.c_[array_[:, 0], array_[:, 3]]
        g_p_2_1 = np.sum(s_2_1)
        g_2_1 = s_2_1[0][0]
        if (g_p_2_1 % 2 != 0 and g_2_1 == 0) or (g_p_2_1 % 2 == 0 and g_2_1 == 1):
            print("[Error]: 2^1")
            # tmp_2_1 = s_2_1

        # search 2^2
        s_2_2 = np.c_[array_[1, :], array_[3, :]]
        g_p_2_2 = np.sum(s_2_2)
        g_2_2 = s_2_2[0][0]
        if (g_p_2_2 % 2 != 0 and g_2_2 == 0) or (g_p_2_2 % 2 == 0 and g_2_2 == 1):
            print("[Error]: 2^2")
            # tmp_2_2 = s_2_2

        # search 2^3
        s_2_3 = np.c_[array_[0, :], array_[2, :]]
        g_p_2_3 = np.sum(s_2_3)
        g_2_3 = s_2_3[0][0]
        if (g_p_2_3 % 2 != 0 and g_2_3 == 0) or (g_p_2_3 % 2 == 0 and g_2_3 == 1):
            print("[Error]: 2^3")
            # tmp_2_3 = s_2_3

    return array_


if __name__ == '__main__':
    s = "0100100110100101"
    list_ = []
    for b in s:
        list_.append(int(b))
    n = np.array(list_, dtype=np.int32)
    n.shape = (4, 4)
    hm(n)
