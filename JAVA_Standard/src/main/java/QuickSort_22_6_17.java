public class QuickSort_22_6_17 {

    int[] array;

    public QuickSort_22_6_17(int[] a) {
        array = a;
    }

    private void sort() {
        sort(0, array.length);

        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + "_");
        }
    }

    private void sort(int begin, int end) {
        if (end - begin < 2) return;
        int mid = pivoIndex(begin, end);
        sort(begin, mid);
        sort(mid + 1, end);
    }

    public int cmp2(Integer v1, Integer v2) {
        return v1 - v2;
    }

    public int pivoIndex(int begin, int end) {
        // 1.备份
        Integer v = array[begin];

        end--;

        while (begin < end) {
            while (begin < end) {
                if (cmp2(v, array[end]) < 0) {
                    // 右边元素>轴点元素
                    end--;
                } else {
                    // 轴点元素>右边元素
                    array[begin++] = array[end];
                    break;
                }
            }

            while (begin < end) {
                if (cmp2(v, array[begin]) > 0) {
                    // 左边元素<轴点元素
                    begin++;
                } else {
                    // 轴点元素<左边元素
                    array[end--] = array[begin];
                    break;
                }
            }
        }
        array[begin] = v;
        // 返回轴点
        return begin;
    }

    public static void main(String[] args) {
        int[] a = {1, 11, 4, 3, 5, 17, 188, 1000};
        QuickSort_22_6_17 q = new QuickSort_22_6_17(a);
        q.sort();
    }
}

