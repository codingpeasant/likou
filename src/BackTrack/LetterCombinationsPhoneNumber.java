package BackTrack;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// https://leetcode.com/problems/letter-combinations-of-a-phone-number/
public class LetterCombinationsPhoneNumber {
    Map<Character, String> numLetters = new HashMap<>();

    public List<String> letterCombinations(String digits) {
        numLetters.put('2', "abc");
        numLetters.put('3', "def");
        numLetters.put('4', "ghi");
        numLetters.put('5', "jkl");
        numLetters.put('6', "mno");
        numLetters.put('7', "pqrs");
        numLetters.put('8', "tuv");
        numLetters.put('9', "wxyz");

        List<String> res = new ArrayList<>();
        if (digits.isEmpty()) return res;
        backtrack(0, digits.toCharArray(),"", res);
        return res;
    }

    private void backtrack(int index, char[] digits, String current, List<String> res) {
        if (current.length() == digits.length) {
            res.add(current);
            return;
        }

        for (int i = 0; i < numLetters.get(digits[index]).length(); i++) {
            //current += numLetters.get(digits[index]).charAt(i);
            backtrack(index + 1, digits, current + numLetters.get(digits[index]).charAt(i), res);
           // current = current.substring(0, current.length() - 1);
        }
    }

    public static void main(String[] args) {
        LetterCombinationsPhoneNumber l = new LetterCombinationsPhoneNumber();
        l.letterCombinations("234").forEach((combination) -> System.out.print(combination + ", "));
    }
}
