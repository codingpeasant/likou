package Other;

// https://leetcode.com/problems/reverse-string/
public class ReverseString {
    public void reverseString(char[] s) {
        int i = 0, j = s.length - 1;
        char temp;
        while (i < j) {
            temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            i++;
            j--;
        }
    }

    public static void main(String[] args) {
        ReverseString r = new ReverseString();
        char[] input = new char[]{'h', 'e', 'l', 'o'};
        r.reverseString(input);
        System.out.println(input);
    }
}
