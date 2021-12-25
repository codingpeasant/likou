package BFS;

import java.util.LinkedList;
import java.util.Queue;

// https://leetcode.com/problems/path-sum/
public class PathSum {
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

    public boolean hasPathSumDFS(TreeNode root, int sum) {
        if (root == null) {
            return false;
        }

        sum -= root.val;
        if (sum == 0 && root.left == null && root.right == null) {
            return true;
        }

        return hasPathSumDFS(root.left, sum) || hasPathSumDFS(root.right, sum);
    }

    public boolean hasPathSumBFS(TreeNode root, int sum) {
        if (root == null) return false;

        Queue<TreeNode> bfsQueue = new LinkedList<>();
        bfsQueue.add(root);

        while (!bfsQueue.isEmpty()) {
            TreeNode cur = bfsQueue.poll();
            int curNum = cur.val;

            if (cur.left != null) {
                cur.left.val += curNum;
                bfsQueue.add(cur.left);
            }

            if (cur.right != null) {
                cur.right.val += curNum;
                bfsQueue.add(cur.right);
            }

            if (cur.left == null && cur.right == null && sum == cur.val) {
                return true;
            }
        }

        return false;
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(9);
        TreeNode node3 = new TreeNode(20);
        TreeNode node4 = new TreeNode(15);
        TreeNode node5 = new TreeNode(7);
        TreeNode node6 = new TreeNode(10);

        node1.left = node2;
        node1.right = node3;
        node3.left = node4;
        node3.right = node5;
        node5.right = node6;

        System.out.println(hasPathSumDFS(node1, 40));
        System.out.println(hasPathSumBFS(node1, 38));
    }

    public static void main(String[] args) {
        PathSum mdt = new PathSum();
        mdt.initialize();
    }
}
