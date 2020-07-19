package Other;

public class AddString {
    public String addStrings(String num1, String num2) {
        StringBuilder result = new StringBuilder();
        int i = num1.length() - 1;
        int j = num2.length() - 1;
        int carry = 0;

        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (i >= 0) {
                sum += num1.charAt(i--) - '0';
            }
            if (j >= 0) {
                sum += num2.charAt(j--) - '0';
            }

            carry = sum / 10;
            result.append(sum % 10);
        }

        if (carry > 0) {
            result.append(carry);
        }

        return result.reverse().toString();
    }

    public static void main(String[] args) {
        AddString a = new AddString();
        String num1 = "4654";
        String num2 = "8884";

        System.out.println("Sum of two numbers is: " + a.addStrings(num1, num2));
    }
}
