package BackTrack;

import java.util.*;

// https://leetcode.ca/2016-08-23-267-Palindrome-Permutation-II/
public class PalindromePermutationII {
    public List<String> generatePalindromes(String s) {
        int[] cha = new int[256];
        for (int i = 0; i < s.length(); i++) { // count each char
            cha[s.charAt(i)] += 1;
        }
        List<String> result = new LinkedList<>();
        boolean odd = false;
        int oddIndex = 0;
        for (int i = 0; i < 256; i++) {
            if (cha[i] % 2 == 1) {
                if (odd) { // as long as there are more than one odd, it cannot form a palindrome
                    return result;
                }
                oddIndex = i;
                odd = true;
            }
        }

        String base = "";
        if (odd) {
            base = (char) oddIndex + ""; // center char of all the palindrome
            cha[oddIndex] -= 1;
        }
        process(base, cha, s.length(), result);
        return result;
    }

    private void process(String base, int[] cha, int n, List<String> result) {
        if (base.length() == n) {
            result.add(base);
            return;
        }
        for (int i = 0; i < cha.length; i++) {
            if (cha[i] > 0) {
                cha[i] -= 2;
                process((char) i + base + (char) i, cha, n, result);
                cha[i] += 2;
            }
        }
    }

    public static void main(String[] args) {
        String input = "aabbc";
        PalindromePermutationII p = new PalindromePermutationII();
        System.out.println(p.generatePalindromes(input));
    }
}
