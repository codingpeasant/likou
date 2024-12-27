package BFS;

import java.util.*;

// https://leetcode.ca/2016-10-09-314-Binary-Tree-Vertical-Order-Traversal/
public class BinaryTreeVerticalOrderTraversal {
    class TreeNode {
        int val;
        int code; // to indicate the sequence
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public List<List<Integer>> verticalOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Map<Integer, List<Integer>> dict = new TreeMap<>(); // sort from low to high for code
        Queue<TreeNode> queue = new LinkedList<>();

        root.code = 0;
        queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode front = queue.poll();
            if (!dict.containsKey(front.code)) {
                dict.put(front.code, new ArrayList<>());
            }
            dict.get(front.code).add(front.val);
            if (front.left != null) {
                front.left.code = front.code - 1; // left node -1
                queue.offer(front.left);
            }
            if (front.right != null) {
                front.right.code = front.code + 1; // right node +1
                queue.offer(front.right);
            }
        }
        res.addAll(dict.values());
        return res;

    }

    public void initialize() {
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(5);
        TreeNode node4 = new TreeNode(4);
        TreeNode node5 = new TreeNode(7);
        TreeNode node6 = new TreeNode(10);

        node1.left = node2;
        node1.right = node3;
        node3.left = node4;
        node3.right = node5;
        node5.right = node6;

        verticalOrder(node1).forEach(System.out::println);
    }

    public static void main(String[] args) {
        BinaryTreeVerticalOrderTraversal mdt = new BinaryTreeVerticalOrderTraversal();
        mdt.initialize();
    }
}
