public class CountingSort_22_6_23 {
    public int[] array;

    private static class Person {
        int age;
        String name;

        Person(int age, String name) {
            this.age = age;
            this.name = name;
        }

        @Override
        public String toString() {
            return "Person{" +
                    "age=" + age +
                    ", name='" + name + '\'' +
                    '}';
        }
    }

    public CountingSort_22_6_23(int[] a) {
        this.array = a;
    }


    public void sort() {
        int max = array[0];
        int min = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i] > max) {
                max = array[i];
            }
            if (array[i] < min) {
                min = array[i];
            }
        }

        int[] counts = new int[max - min + 1];
        for (int i = 0; i < array.length; i++) {
            counts[array[i] - min]++;
        }

        for (int i = 1; i < counts.length; i++) {
            counts[i] += counts[i - 1];
        }

        int[] newArray = new int[array.length];
        for (int i = array.length - 1; i >= 0; i--) {
            newArray[--counts[array[i] - min]] = array[i];
        }

        for (int i = 0; i < newArray.length; i++) {
            array[i] = newArray[i];
        }
    }

    public void sort1() {
        int max = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }

        int[] counts = new int[1 + max];
        for (int i = 0; i < array.length; i++) {
            counts[array[i]]++;
        }

        int index = 0;
        for (int i = 0; i < array.length; i++) {
            while (counts[i]-- > 0) {
                array[index++] = i;
            }
        }
    }


    public static void main(String[] args) {
        Person[] persons = new Person[] {
                new Person(20, "A"),
                new Person(-13, "B"),
                new Person(17, "C"),
                new Person(12, "D"),
                new Person(-13, "E"),
                new Person(20, "F")
        };

        // 找出最值
        int max = persons[0].age;
        int min = persons[0].age;
        for (int i = 1; i < persons.length; i++) {
            if (persons[i].age > max) {
                max = persons[i].age;
            }
            if (persons[i].age < min) {
                min = persons[i].age;
            }
        }

        // 开辟内存空间，存储次数
        int[] counts = new int[max - min + 1];
        // 统计每个整数出现的次数
        for (int i = 0; i < persons.length; i++) {
            counts[persons[i].age - min]++;
        }
        // 累加次数
        for (int i = 1; i < counts.length; i++) {
            counts[i] += counts[i - 1];
        }

        // 从后往前遍历元素，将它放到有序数组中的合适位置
        Person[] newArray = new Person[persons.length];
        for (int i = persons.length - 1; i >= 0; i--) {
            newArray[--counts[persons[i].age - min]] = persons[i];
        }

        // 将有序数组赋值到array
        for (int i = 0; i < newArray.length; i++) {
            persons[i] = newArray[i];
        }

        for (int i = 0; i < persons.length; i++) {
            System.out.println(persons[i]);
        }
    }
}
