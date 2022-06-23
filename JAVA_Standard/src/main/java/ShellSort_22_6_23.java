import java.util.LinkedList;
import java.util.List;

public class ShellSort_22_6_23 {

    public int[] array;

    public ShellSort_22_6_23(int[] a) {
        array = a;
    }

    public void sort() {
        List<Integer> stepSequence = sedgewickStepSequence();
        for (Integer step : stepSequence) {
            sort(step);
        }

        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + "_");
        }
    }

    public void sort(int step) {
        for (int col = 0; col < step; col++) {

            for (int begin = col + step; begin < array.length; begin += step) {
                int cur = begin;
                while (cur > col && cmp(cur, cur - step) < 0) {
                    swap(cur, cur - step);
                    cur -= step;
                }
            }
        }
    }

    public void swap(int i1, int i2) {
        Integer tmp = array[i1];
        array[i1] = array[i2];
        array[i2] = tmp;
    }

    public int cmp(int v1, int v2) {
        return array[v1] - array[v2];
    }

    public List<Integer> sedgewickStepSequence() {
        List<Integer> stepSequence = new LinkedList<>();
        int k = 0, step = 0;
        while (true) {
            if (k % 2 == 0) {
                int pow = (int) Math.pow(2, k >> 1);
                step = 1 + 9 * (pow * pow - pow);
            } else {
                int pow1 = (int) Math.pow(2, (k - 1) >> 1);
                int pow2 = (int) Math.pow(2, (k + 1) >> 1);
                step = 1 + 8 * pow1 * pow2 - 6 * pow2;
            }
            if (step >= array.length) break;
            stepSequence.add(0, step);
            k++;
        }
        return stepSequence;
    }

    public static void main(String[] args) {
        int[] array = {0, 16, 77, 54, 1, 2, 99, 15};
        ShellSort_22_6_23 s = new ShellSort_22_6_23(array);
        s.sort();
    }
}
