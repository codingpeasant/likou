package Other;

// https://leetcode.com/problems/add-binary/
public class AddBinary {
    public String addBinary(String a, String b) {
        StringBuilder builder = new StringBuilder();
        int i = a.length() - 1, j = b.length() - 1, carry = 0;
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (i >= 0) {
                sum += a.charAt(i--) - '0';
            }
            if (j >= 0) {
                sum += b.charAt(j--) - '0';
            }
            builder.append(sum % 2);
            carry = sum / 2;
        }
        if (carry > 0) {
            builder.append(carry);
        }

        return builder.reverse().toString();
    }

    public static void main(String[] args) {
        AddBinary add = new AddBinary();
        String a = "1010";
        String b = "1011";
        System.out.println("Sum of binary: " + add.addBinary(a, b));
    }
}
