public class BubbleSort_22_6_16 {
    public static void main(String[] args) {
        int[] array = {0, 19, 4, 88, 14, 77, 36};

//        for (int end = array.length - 1; end > 0; end--) {
//            boolean flag = true;
//            for (int begin = 1; begin <= end; begin++) {
//                if (array[begin] < array[begin - 1]) {
//                    int tmp = array[begin];
//                    array[begin] = array[begin - 1];
//                    array[begin - 1] = tmp;
//                    flag = false;
//                }
//            }
//            if (flag) break;
//        }
        for (int end = array.length - 1; end > 0; end--) {
            int flag = 1;
            for (int begin = 1; begin <= end; begin++) {
                if (array[begin] < array[begin - 1]) {
                    int tmp = array[begin];
                    array[begin] = array[begin - 1];
                    array[begin - 1] = tmp;
                    flag = begin;
                }
            }
            end = flag;
        }
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + "_");
        }

    }
}
