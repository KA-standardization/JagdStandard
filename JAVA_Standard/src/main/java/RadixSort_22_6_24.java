public class RadixSort_22_6_24 {
    public int[] array;

    public RadixSort_22_6_24(int[] a) {
        array = a;
    }

    public void sort() {
        int max = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }
        for (int divider = 1; divider <= max; divider *= 10) {
            countingSort(divider);
        }

        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + "_");
        }
    }

    public void countingSort(int divider) {
        int[] counts = new int[10];

        for (int i = 0; i < array.length; i++) {
            counts[array[i] / divider % 10]++;
        }

        for (int i = 1; i < counts.length; i++) {
            counts[i] += counts[i - 1];
        }

        int[] newArray = new int[array.length];
        for (int i = array.length - 1; i >= 0; i--) {
            newArray[--counts[array[i] / divider % 10]] = array[i];
        }

        for (int i = 0; i < newArray.length; i++) {
            array[i] = newArray[i];
        }

    }

    public static void main(String[] args) {
        int[] array = {0, 16, 77, 54, 1, 2, 99, 15};
        RadixSort_22_6_24 r = new RadixSort_22_6_24(array);
        r.sort();
    }
}
