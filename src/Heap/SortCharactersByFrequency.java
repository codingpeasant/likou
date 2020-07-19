package Heap;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

public class SortCharactersByFrequency {
    public String frequencySort(String s) {
        Map<Character, Integer> charFreqMap = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            charFreqMap.put(s.charAt(i), charFreqMap.getOrDefault(s.charAt(i), 0) + 1);
        }

        PriorityQueue<Map.Entry<Character, Integer>> maxHeap = new PriorityQueue<>((a,b) -> b.getValue() - a.getValue());
        maxHeap.addAll(charFreqMap.entrySet());

        StringBuilder builder = new StringBuilder();
        while (!maxHeap.isEmpty()) {
            Map.Entry<Character, Integer> e = maxHeap.poll();

            for (int i = 0; i < e.getValue(); i++) {
                builder.append(e.getKey());
            }
        }
        return builder.toString();
    }

    public static void main(String[] args) {
        SortCharactersByFrequency s = new SortCharactersByFrequency();
        String input = "woegijwoihehhhhh";
        System.out.println("Sorted by freq: " + s.frequencySort(input));
    }
}
