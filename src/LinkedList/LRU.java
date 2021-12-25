package LinkedList;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;

// https://leetcode.com/problems/lru-cache/
public class LRU {
    private class Node {
        int key, value;
        Node prev, next;

        Node(int k, int v) {
            this.key = k;
            this.value = v;
        }

        Node() {
            this(0, 0);
        }
    }

    private int capacity, count;
    private Map<Integer, Node> map;
    private Node head, tail;

    public LRU(int capacity) {
        this.capacity = capacity;
        this.count = 0;
        map = new HashMap<>();
        head = new Node();
        tail = new Node();
        head.next = tail;
        tail.prev = head;
    }

    public int get(int key) {
        Node n = map.get(key);
        if (null == n) {
            return -1;
        }
        update(n);
        return n.value;
    }

    public void set(int key, int value) {
        Node n = map.get(key);
        if (null == n) {
            n = new Node(key, value);
            map.put(key, n);
            add(n);
            ++count;
        } else {
            n.value = value;
            update(n);
        }
        if (count > capacity) {
            Node toDel = tail.prev;
            remove(toDel);
            map.remove(toDel.key);
            --count;
        }
    }

    private void update(Node node) {
        remove(node);
        add(node);
    }

    private void add(Node node) {
        Node after = head.next;
        head.next = node;
        node.prev = head;
        node.next = after;
        after.prev = node;
    }

    private void remove(Node node) {
        Node before = node.prev, after = node.next;
        before.next = after;
        after.prev = before;
    }

    // using LinkedHashMap
    class LRULinkedHashMap {
        int cap;
        Map<Integer, Integer> cache = new LinkedHashMap<>();

        public LRULinkedHashMap(int capacity) {
            cap = capacity;
        }

        public int get(int key) {
            if (!cache.containsKey(key)) {
                return -1;
            }

            makeNewest(key);
            return cache.get(key);
        }

        public void put(int key, int val) {
            if (cache.containsKey(key)) {
                cache.put(key, val);
                makeNewest(key);
                return;
            }

            if (cache.size() >= this.cap) {
                cache.remove(cache.keySet().iterator().next()); // first element in the
            }

            cache.put(key, val); // automatically becomes head (most recent)
        }

        private void makeNewest(int key) {
            int val = cache.get(key);
            cache.remove(key);
            cache.put(key, val);
        }
    }
}
