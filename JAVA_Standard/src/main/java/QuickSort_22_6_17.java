public class QuickSort_22_6_17 {

    int[] array;

    public QuickSort_22_6_17(int[] a) {
        array = a;
    }

    private void sort() {
        sort(0, array.length);

    }

    private void sort(int begin, int end) {
        if (end - begin < 2) return;






    }


    public static void main(String[] args) {
        int[] a = {1, 11, 4, 3, 5, 17, 188, 1000};
        QuickSort_22_6_17 q = new QuickSort_22_6_17(a);
        q.sort();

    }
}

