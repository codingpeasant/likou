package Heap;

import java.util.*;

// https://leetcode.com/problems/top-k-frequent-words/
public class TopKFrequentWords {
    public List<String> topKFrequent(String[] words, int k) {
        List<String> result = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            if (map.containsKey(words[i]))
                map.put(words[i], map.get(words[i]) + 1);
            else
                map.put(words[i], 1);
        }

        PriorityQueue<Map.Entry<String, Integer>> minHeap = new PriorityQueue<>(
                (a, b) -> a.getValue() == b.getValue() ? b.getKey().compareTo(a.getKey()) : a.getValue() - b.getValue()
        );

        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            minHeap.offer(entry);
            if (minHeap.size() > k)
                minHeap.poll();
        }

        while (!minHeap.isEmpty())
            result.add(0, minHeap.poll().getKey());

        return result;
    }

    public static void main(String[] args) {
        TopKFrequentWords t = new TopKFrequentWords();
        String[] input = {"i", "love", "leetcode", "i", "love", "coding"};
        System.out.println(t.topKFrequent(input, 2));
    }
}
