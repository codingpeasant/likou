package Other;

public class SortArrayByParity {
    public int[] sortArrayByParity(int[] A) {
        int end = A.length - 1;
        int begin = 0;

        while (begin < end) {
            if (A[begin] % 2 != 0 && A[end] % 2 == 0) {
                int temp = A[begin];
                A[begin++] = A[end];
                A[end--] = temp;
            } else if (A[begin] % 2 != 0) {
                end--;
            } else {
                begin++;
            }
        }

        return A;
    }

    public static void main(String args[]) {
        SortArrayByParity a = new SortArrayByParity();
        int[] input = {3,2,1,4,5,8,1,0,9,2};
        for (int el: a.sortArrayByParity(input)) {
            System.out.print(el + ", ");
        }
    }
}
