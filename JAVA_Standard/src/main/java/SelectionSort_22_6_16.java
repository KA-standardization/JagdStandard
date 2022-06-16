public class SelectionSort_22_6_16 {

    public static void main(String[] args) {
        int[] array = {0, 15, 88, 8, 4, 45};

        for (int end = array.length - 1; end > 0; end--) {
            int maxIndex = 0;
            for (int begin = 1; begin <= end; begin++) {
                if (array[maxIndex] <= array[begin]) {
                    maxIndex = begin;
                }
            }
            int tmp = array[maxIndex];
            array[maxIndex] = array[end];
            array[end] = tmp;
        }

        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + "_");
        }
    }
}
