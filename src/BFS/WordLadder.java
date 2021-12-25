package BFS;

import DFS.NumberOfIslands;

import java.lang.reflect.Array;
import java.util.*;

// https://leetcode.com/problems/word-ladder/
public class WordLadder {
    class Pair {
        String word;
        int step;

        public Pair(String word, int step) {
            this.word = word;
            this.step = step;
        }
    }

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        int steps = 0;
        if (!wordList.contains(endWord)) {
            return steps;
        }

        Queue<Pair> bfsQueue = new LinkedList<>();
        boolean[] visited = new boolean[wordList.size()];

        bfsQueue.add(new Pair(beginWord, 1));

        while (!bfsQueue.isEmpty()) {
            Pair wordStep = bfsQueue.poll();

            if (endWord.equals(wordStep.word)) {
                System.out.print(wordStep.word + "\n");
                steps = wordStep.step;
                break;
            }
            System.out.print(wordStep.word+" -> ");

            for (int i = 0; i < wordList.size(); i++) {
                if (!visited[i] && isNeighbor(wordStep.word, wordList.get(i))) {
                    bfsQueue.add(new Pair(wordList.get(i), wordStep.step + 1));
                    visited[i] = true;
                }
            }
        }

        return steps;
    }

    public int ladderLength1(String beginWord, String endWord, List<String> wordList) { // level
        int steps = 0;
        if (!wordList.contains(endWord)) {
            return steps;
        }

        Queue<String> bfsQueue = new LinkedList<>();
        boolean[] visited = new boolean[wordList.size()];

        bfsQueue.add(beginWord);

        while (!bfsQueue.isEmpty()) {
            int count = bfsQueue.size();
            for (int j = 0; j < count; j++) {
                String word = bfsQueue.poll();
                if (endWord.equals(word)) {
                    System.out.print(word + "\n");
                    return steps  + 1;
                }
                System.out.print(word+" -> ");

                for (int i = 0; i < wordList.size(); i++) {
                    if (!visited[i] && isNeighbor(word, wordList.get(i))) {
                        bfsQueue.add(wordList.get(i));
                        visited[i] = true;
                    }
                }
            }
            steps++;
        }

        return 0;
    }

    boolean isNeighbor(String word, String anotherWord) {
        int numberOfCommonLetters = 0;
        for (int i = 0; i < word.length(); i++) {
            if (word.charAt(i) == anotherWord.charAt(i)) {
                numberOfCommonLetters++;
            }
        }
        return word.length() - numberOfCommonLetters == 1;
    }

    // Driver method
    public static void main(String[] args) throws java.lang.Exception {
        ArrayList<String> wordList = new ArrayList<>(Arrays.asList("hot","dot","dog","lot","log","cog"));
        String beginWord = "hit";
        String endWord = "cog";

        WordLadder w = new WordLadder();
        System.out.println("Number of steps is: " + w.ladderLength(beginWord, endWord, wordList));
        System.out.println("Number of steps is: " + w.ladderLength1(beginWord, endWord, wordList));
    }
}
