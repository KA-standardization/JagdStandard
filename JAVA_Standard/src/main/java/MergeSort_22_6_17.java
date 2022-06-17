@SuppressWarnings("unchecked")
public class MergeSort_22_6_17 {
    int[] array;
    int[] leftArray;

    public MergeSort_22_6_17(int[] a) {
        array = a;
    }

    public int cmp2(Integer v1, Integer v2) {
        return v1 - v2;
    }

    public void merge(int begin, int mid, int end) {
        int li = 0, le = mid - begin;
        int ri = mid, re = end;
        int ai = begin;

        for (int i = li; i < le; i++) {
            leftArray[i] = array[begin + i];
        }

        while (li < le) {
//            if (ri < re && cmp2(array[ri], leftArray[li]) <= 0) {  //失去稳定性
            if (ri < re && cmp2(array[ri], leftArray[li]) < 0) {
                array[ai++] = array[ri++];
            } else {
                array[ai++] = leftArray[li++];
            }
        }

    }

    public void sort() {
//        leftArray = new Comparable[array.length >> 1];
        leftArray = new int[array.length >> 1];
        sort(0, array.length);

        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + "_");
        }
    }

    public void sort(int begin, int end) {
        if (end - begin < 2) return;
        int mid = (begin + end) >> 1;
        sort(begin, mid);
        sort(mid, end);
        merge(begin, mid, end);
    }


    public static void main(String[] args) {
        int[] array = {0, 16, 77, 54, 1, 2, 99, 15};
        MergeSort_22_6_17 m = new MergeSort_22_6_17(array);
        m.sort();
    }
}
