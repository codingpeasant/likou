package SlidingWindow;

// https://leetcode.com/problems/longest-repeating-character-replacement/
public class LongestRepeatingCharacterReplacement {
    public int characterReplacement(String s, int k) {
        int[] freq = new int[26];
        int mostFreqLetter = 0;
        int left = 0;
        int max = 0;

        for (int right = 0; right < s.length(); right++) {
            freq[s.charAt(right) - 'A']++;
            mostFreqLetter = Math.max(mostFreqLetter, freq[s.charAt(right) - 'A']);

            int lettersToChange = (right - left + 1) - mostFreqLetter; // change other letters to most freq letter
            // We are looking for the maximum window, so we should not be too conservative and shrink the window too much.
            // For example, if you find the longest window of 5, there is no need to check window of size 4, 3, 2, 1.
            // So we are never decreasing the maximum window - its size either increases or stays the same.
            if (lettersToChange > k) {
                freq[s.charAt(left) - 'A']--;
                left++;
            } else {
                max = Math.max(max, right - left + 1);
            }
        }

        return max;
    }

    public static void main(String[] args) {
        LongestRepeatingCharacterReplacement l = new LongestRepeatingCharacterReplacement();
        String input = "AABABCA";
        System.out.println(l.characterReplacement(input, 1));
    }
}
