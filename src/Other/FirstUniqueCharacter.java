package Other;

// https://leetcode.com/problems/first-unique-character-in-a-string/
public class FirstUniqueCharacter {
    public int firstUniqChar(String s) {
        int[] charsCount = new int[26];

        for (int i = 0; i < s.length(); i++) {
            charsCount[s.charAt(i) - 'a']++;
        }

        for (int j  = 0; j < s.length(); j++) {
            if (charsCount[s.charAt(j) - 'a'] == 1) {
                return j;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        FirstUniqueCharacter f = new FirstUniqueCharacter();
        String input = "leetcode";
        System.out.println("First unique char: " + f.firstUniqChar(input));
    }
}
