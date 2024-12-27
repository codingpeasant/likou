package BFS;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

// https://leetcode.com/problems/maximum-width-of-binary-tree/
public class MaximumWidthBinaryTree {
    class TreeNode {
        int val;
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

    class Pair {
        TreeNode node;
        int index;

        Pair(TreeNode node, int index) {
            this.node = node;
            this.index = index;
        }
    }

    // we don't really care about the value of the tree nodes but the index of them
    public int widthOfBinaryTree(TreeNode root) {
        Queue<Pair> queue = new LinkedList<>();
        queue.add(new Pair(root, 1));
        int maxWidth = 1;

        while (!queue.isEmpty()) {
            Pair leftMost = queue.peek();
            Pair right = leftMost;
            int count = queue.size();

            while (count > 0) {
                right = queue.poll();
                if (right.node.left != null) {
                    queue.add(new Pair(right.node.left, right.index * 2));
                }
                if (right.node.right != null) {
                    queue.add(new Pair(right.node.right, right.index * 2 + 1));
                }
                count--;
            }
            maxWidth = Math.max(maxWidth, right.index - leftMost.index + 1);
        }

        return maxWidth;
    }

    public int widthOfBinaryTreeDFS(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return helper(root, 0, 1, new ArrayList<>());

    }
    private int helper(TreeNode root, int depth, int index, List<Integer> list) {
        if (root == null) {
            return 0;
        }
        //add index of leftmost node to list, at depth'th position in list
        if (depth == list.size()) {
            list.add(index);
        }
        int currWidth = index - list.get(depth) + 1;
        int leftWidth = helper(root.left, depth + 1, index * 2, list);
        int rightWidth = helper(root.right, depth + 1, index * 2 + 1, list);
        return Math.max(currWidth, Math.max(leftWidth, rightWidth));
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(4);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(6);
        TreeNode node4 = new TreeNode(1);
        TreeNode node5 = new TreeNode(3);
        TreeNode node6 = new TreeNode(5);
        //TreeNode node7 = new TreeNode(7);

        node1.left = node2;
        node1.right = node3;

        node2.left = node4;
        node2.right = node5;

        node3.left = node6;
        //node3.right = node7;

        System.out.println("Max width is: " + widthOfBinaryTree(node1));
        System.out.println("Max width is: " + widthOfBinaryTreeDFS(node1));
    }

    public static void main(String[] args) {
        MaximumWidthBinaryTree r = new MaximumWidthBinaryTree();
        r.initialize();
    }
}
