package Other;

import java.util.HashSet;
import java.util.Set;

public class ReverseVowelsString {
    public String reverseVowels(String s) {
        Set<Character> vowels = new HashSet<>();
        vowels.add('a');
        vowels.add('A');
        vowels.add('i');
        vowels.add('I');
        vowels.add('e');
        vowels.add('E');
        vowels.add('o');
        vowels.add('O');
        vowels.add('u');
        vowels.add('U');

        char[] charsOfInput = s.toCharArray();
        int i = 0;
        int j = s.length() - 1;

        while (i < j) {
            while (i < j && !vowels.contains(charsOfInput[i])) {
                i++;
            }

            while (i < j && !vowels.contains(charsOfInput[j])) {
                j--;
            }

            if (i != j && vowels.contains(charsOfInput[j]) && vowels.contains(charsOfInput[i])) {
                char temp = charsOfInput[i];
                charsOfInput[i++] = charsOfInput[j];
                charsOfInput[j--] = temp;
            }
        }

        return new String(charsOfInput);
    }

    public static void main(String[] args) {
        ReverseVowelsString r = new ReverseVowelsString();
        String input = "helllloo";
        System.out.println("Reversed vowel: " + r.reverseVowels(input));
    }
}
