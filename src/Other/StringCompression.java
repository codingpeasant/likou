package Other;

import java.util.Arrays;

// https://leetcode.com/problems/string-compression/
// Great example about when you cannot use for loop easily / set elements in array as empty easily
public class StringCompression {
    public int compress(char[] chars) {
        int indexAns = 0, index = 0;
        while (index < chars.length) {
            char currentChar = chars[index];
            int count = 0;
            while (index < chars.length && chars[index] == currentChar) {
                index++;
                count++;
            }
            chars[indexAns++] = currentChar;

            if (count != 1)
                for (char c : String.valueOf(count).toCharArray())
                    chars[indexAns++] = c;
        }
        return indexAns;
    }

    public String compress2(char[] chars) {
        int cur = 0, index = 0;
        while (index < chars.length) {
            char curChar = chars[index];
            int count = 0;
            while (index < chars.length && chars[index] == curChar) {
                index++;
                count++;
            }
            chars[cur++] = curChar;
            if (count != 1) {
                for (char countChar : Integer.toString(count).toCharArray()) {
                    chars[cur++] = countChar;
                }
            }
        }

        return new String(Arrays.copyOfRange(chars, 0, cur));
    }

    public static void main(String[] args) {
        StringCompression s = new StringCompression();
        String input = "aaabbbbbbbc";
        System.out.println("Compressed length: " + s.compress(input.toCharArray()));
        System.out.println(s.compress2(input.toCharArray()));
    }
}
