package Other;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

// https://leetcode.com/problems/reorganize-string/
// greedy - insert the current second frequent between most frequents
public class ReorganizeString {
    public String reorganizeString(String S) {
        Map<Character, Integer> charCount = new HashMap<>();
        for (char c : S.toCharArray()) {
            int count = charCount.getOrDefault(c, 0) + 1;
            // Impossible to form a solution
            if (count > (S.length() + 1) / 2) return "";
            charCount.put(c, count);
        }

        // Greedy: fetch char of max count as next char in the result.
        // Use PriorityQueue to store pairs of (char, count) and sort by count DESC.
        PriorityQueue<Character> maxHeap = new PriorityQueue<>((a, b) -> charCount.get(b) - charCount.get(a));
        maxHeap.addAll(charCount.keySet());

        StringBuilder result = new StringBuilder();
        while (maxHeap.size() > 1) {
            char first = maxHeap.poll();
            char second = maxHeap.poll();

            result.append(first);
            result.append(second);

            charCount.put(first, charCount.get(first) - 1);
            charCount.put(second, charCount.get(second) - 1);

            if (charCount.get(first) > 0) {
                maxHeap.add(first);
            }
            if (charCount.get(second) > 0) {
                maxHeap.add(second);
            }
        }

        // if more than 1 left, there is no way to keep different adjacent chars
        if (!maxHeap.isEmpty()) {
            char last = maxHeap.poll();
            if (charCount.get(last) > 1) {
                return "";
            }
            result.append(last);
        }

        return result.toString();
    }

    public static void main(String[] args) {
        ReorganizeString r = new ReorganizeString();
        String input = "aasssbccc";
        System.out.println("Reordered: " + r.reorganizeString(input));
    }
}
