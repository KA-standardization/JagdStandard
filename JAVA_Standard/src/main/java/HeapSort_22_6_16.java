@SuppressWarnings({"rawtypes","unchecked"})
public class HeapSort_22_6_16 {

    public int heapSize;
    public int[] array;

    public HeapSort_22_6_16(int[] a) {
        array = a;
    }

    public void swap(int i1, int i2) {
        Integer tmp = array[i1];
        array[i1] = array[i2];
        array[i2] = tmp;
    }

    public int cmp(Integer v1, Integer v2) {
        return v1 - v2;
    }

    public void siftDown(int index) {
        Integer element = array[index];
        int half = heapSize >> 1;
        while (index < half) {
            int childIndex = (index << 1) + 1;
            Integer child = array[childIndex];
            int rightIndex = childIndex + 1;
            if (rightIndex < heapSize && cmp(array[rightIndex], child) > 0) {
                child = array[childIndex = rightIndex];
            }
            if (cmp(element, child) >= 0) break;
            array[index] = child;
            index = childIndex;
        }
        array[index] = element;
    }

    public void sort() {
        heapSize = array.length;
        for (int i = (heapSize >> 1) - 1; i >= 0; i--) {
            siftDown(i);
        }

        while (heapSize > 1) {
            // 交换堆顶元素和尾部元素
            swap(0, --heapSize);
            // 对0位置进行siftDown（恢复堆的性质）
            siftDown(0);
        }

        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + "_");
        }
    }

    public static void main(String[] args) {
        int[] array = {0, 16, 77, 54, 1, 2, 99, 15};
        HeapSort_22_6_16 h = new HeapSort_22_6_16(array);
        h.sort();
    }
}

