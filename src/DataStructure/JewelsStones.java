package DataStructure;

import java.util.HashSet;
import java.util.Set;

// https://leetcode.com/problems/jewels-and-stones/
public class JewelsStones {
    public int numJewelsInStones(String J, String S) {
        Set<Character> jSet = new HashSet<>();
        for (char j : J.toCharArray()) {
            jSet.add(j);
        }

        int res = 0;
        for (char s : S.toCharArray()) {
            if (jSet.contains(s)) {
                res++;
            }
        }

        return res;
    }

    public static void main(String[] args) {
        JewelsStones j = new JewelsStones();
        String jewels = "aA";
        String stones = "aAAbbbb";
        System.out.println("Num of jewel: " + j.numJewelsInStones(jewels, stones));
    }
}
