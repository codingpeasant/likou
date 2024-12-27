package DP;

import java.util.Arrays;

// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/1505263/Single-pass-O(n)-time-and-O(1)-space-solution-with-detailed-explanation
public class CountUniqueCharactersAllSubstringsGivenString {
    public int uniqueLetterString(String s) {
        int sum = 0, curr = 0, n = s.length();

        int[] last = new int[26]; // last time saw this char
        int[] prev = new int[26];

        Arrays.fill(last, -1);
        Arrays.fill(prev, -1);

        char[] chars = s.toCharArray();
        for (int i = 0; i < n; i++) {
            char c = chars[i];
            // curr = curr + q - r + 1 , where
            // q = i - lastIndex - 1
            // r  = lastIndex - previndex
            curr += (i - last[c - 65] - 1) - (last[c - 65] - prev[c - 65]) + 1;
            prev[c - 65] = last[c - 65];
            last[c - 65] = i;
            sum += curr;
        }

        return sum;
    }

    public static void main(String[] args) {
        CountUniqueCharactersAllSubstringsGivenString c = new CountUniqueCharactersAllSubstringsGivenString();
        System.out.println(c.uniqueLetterString("ABABB"));
    }
}
