public class InsertionSort_22_6_16 {

    public int[] array;

    public InsertionSort_22_6_16(int[] a) {
        array = a;
    }

    public void swap(int i1, int i2) {
        Integer tmp = array[i1];
        array[i1] = array[i2];
        array[i2] = tmp;
    }

    public int cmp(int v1, int v2) {
        return array[v1] - array[v2];
    }

    public int cmp2(Integer v1, Integer v2) {
        return v1 - v2;
    }

    public void sort() {
        for (int begin = 1; begin < array.length; begin++) {
            int cur = begin;
            while (cur > 0 && cmp(cur, cur - 1) < 0) {
                swap(cur, cur - 1);
                cur--;
            }
        }

        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + "_");
        }
    }

    public void sort2() {
        for (int begin = 1; begin < array.length; begin++) {
            int cur = begin;
            Integer v = array[cur];
            while (cur > 0 && cmp2(v, array[cur - 1]) < 0) {
                array[cur] = array[cur - 1];
                cur--;
            }
        }

        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + "_");
        }
    }

    public void sort3() {
        for (int begin = 1; begin < array.length; begin++) {
            insert(begin, search(begin));
        }

        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + "_");
        }
    }

    public void insert(int src, int dst) {
        Integer v = array[src];
        for (int i = src; i > dst; i--) {
            array[i] = array[i - 1];
        }
        array[dst] = v;
    }

    public int search(int index) {
        int begin = 0;
        int end = index;
        while (begin < end) {
            int mid = (begin + end) >> 1;
            if (cmp2(array[index], array[mid]) < 0) {
                end = mid;
            } else {
                begin = mid + 1;
            }
        }
        return begin;
    }

    public static void main(String[] args) {
        int[] array = {0, 16, 77, 54, 1, 2, 99, 15};
        InsertionSort_22_6_16 i = new InsertionSort_22_6_16(array);
//        i.sort();
//        i.sort2();
        i.sort3();
    }
}


