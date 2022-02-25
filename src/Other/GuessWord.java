package Other;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

// https://leetcode.com/problems/guess-the-word/
public class GuessWord {
    interface Master {
        int guess(String word);
    }

    public int match(String a, String b) {
        int matches = 0;
        for (int i = 0; i < a.length(); ++i)
            if (a.charAt(i) == b.charAt(i))
                matches++;
        return matches;
    }

    // secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]
    public void findSecretWord(String[] wordlist, Master master) {
        for (int i = 0, x = 0; i < 10 && x < 6; ++i) {
            String guess = wordlist[new Random().nextInt(wordlist.length)];
            x = master.guess(guess);
            List<String> wordlist2 = new ArrayList<>();
            for (String w : wordlist) // Update our wordlist and keep only the same matches to our guess
                if (match(guess, w) == x)
                    wordlist2.add(w);
            wordlist = wordlist2.toArray(new String[wordlist2.size()]);
        }
    }
}
