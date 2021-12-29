package SlidingWindow;

import java.util.ArrayList;
import java.util.List;

// https://leetcode.com/problems/partition-labels/
public class PartitionLabels {
    public List<Integer> partitionLabels(String S) {
        if (S == null || S.length() == 0) {
            return null;
        }
        List<Integer> list = new ArrayList<>();
        int[] charLastPosition = new int[26];

        for (int i = 0; i < S.length(); i++) {
            charLastPosition[S.charAt(i) - 'a'] = i;
        }

        int start = 0;
        int last = 0;
        for (int i = 0; i < S.length(); i++) {
            last = Math.max(last, charLastPosition[S.charAt(i) - 'a']);
            if (last == i) { // included all letters of previous occurrence at i
                list.add(i - start + 1);
                start = i + 1; // jump to current right pointer + 1
            }
        }
        return list;
    }

    // The partition is "ababcbaca", "defegde", "hijhklij".
    public static void main(String[] args) {
        PartitionLabels p = new PartitionLabels();
        String input = "ababcbacadefegdehijhklij";
        System.out.println("Parts: " + p.partitionLabels(input));
    }
}
