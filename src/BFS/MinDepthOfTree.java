package BFS;

import java.util.LinkedList;
import java.util.Queue;

// https://leetcode.com/problems/minimum-depth-of-binary-tree/
public class MinDepthOfTree {
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

    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        Queue<TreeNode> bfsQueue = new LinkedList<>();
        int level = 1;
        bfsQueue.add(root);

        while (!bfsQueue.isEmpty()) {
            int count = bfsQueue.size();
            for (int i = 0; i < count; i++) {
                TreeNode cur = bfsQueue.poll();
                if (cur.left == null && cur.right == null) { // when the first leaf node appears
                    return level;
                }
                if (cur.left != null) {
                    bfsQueue.add(cur.left);
                }
                if (cur.right != null) {
                    bfsQueue.add(cur.right);
                }
            }
            level++;
        }

        return level;
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(9);
        TreeNode node3 = new TreeNode(20);
        TreeNode node4 = new TreeNode(15);
        TreeNode node5 = new TreeNode(7);
        //TreeNode node6 = new TreeNode(10);
        //TreeNode node7 = new TreeNode(12);

        node1.left = node2;
        node1.right = node3;
        node2.left = node4;
        node2.right = node5;
        //node3.left = node6;
        //node3.right = node7;

        System.out.println("The min depth of tree is: " + minDepth(node1));
    }

    public static void main(String[] args) {
        MinDepthOfTree mdt = new MinDepthOfTree();
        mdt.initialize();
    }
}
