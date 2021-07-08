package Other;

public class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        int[] charsMap = new int['z'-'a' + 1];

        for(char c: s.toCharArray()) {
            int pos = c - 'a';
            charsMap[pos]++;
        }

        for(char c: t.toCharArray()) {
            int pos = c - 'a';
            charsMap[pos]--;
        }

        for(int count: charsMap) {
            if(count != 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        ValidAnagram v = new ValidAnagram();
        String s = "anagram";
        String t = "nagaram";
        System.out.println("is anagram: " + v.isAnagram(s, t));
    }
}
