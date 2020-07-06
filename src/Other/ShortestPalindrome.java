package Other;

public class ShortestPalindrome {
    public String shortestPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return s;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = s.length() - 1; i >= 0; i--) {
            sb.append(s.charAt(i));
        }
        String t = sb.toString();
        for (int i = 0; i <= t.length(); i++) {
            String cur = t.substring(i);
            if (s.startsWith(cur)) { // Palindrome : reversed == original
                return t.substring(0, i) + s;
            }
        }
        return t + s;
    }

    public static void main(String args[]) {
        ShortestPalindrome s = new ShortestPalindrome();
        String input = "dedcba";
        System.out.println("shortest is: " + s.shortestPalindrome(input));
    }

}
