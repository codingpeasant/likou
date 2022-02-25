package Other;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

// https://leetcode.ca/2019-01-26-1153-String-Transforms-Into-Another-String/
public class StringTransformsIntoAnotherString {
    public boolean canConvert(String str1, String str2) {
        if (str1.equals(str2)) {
            return true;
        }
        Map<Character, Character> map = new HashMap<>();
        for (int i = 0; i < str1.length(); i++) {
            char c1 = str1.charAt(i);
            char c2 = str2.charAt(i);
            if (map.containsKey(c1) && map.get(c1) != c2) {
                return false;
            }
            map.put(c1, c2);
        }
        // if all 26 letters, there is no extra space to assign a temp transform, like abc->cba, a could be transformed to d first
        return new HashSet<>(map.values()).size() < 26;
    }

    public static void main(String[] args) {
        StringTransformsIntoAnotherString s = new StringTransformsIntoAnotherString();
        String a = "abc";
        String b = "cba";
        System.out.println(s.canConvert(a, b));
    }
}
