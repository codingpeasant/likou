package BFS;

import java.util.LinkedList;
import java.util.Queue;

// https://leetcode.com/problems/find-bottom-left-tree-value/
public class FindBottomLeftTreeValue {
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

    public int findBottomLeftValue(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        int lastValue = 0;
        while (!q.isEmpty()) {
            TreeNode cur = q.poll();
            if (cur.right != null) { // add right first so the right most will be last element
                q.offer(cur.right);
            }

            if (cur.left != null) {
                q.offer(cur.left);
            }

            if (q.isEmpty()) {
                lastValue = cur.val;
            }
        }
        return lastValue;
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

        System.out.println(findBottomLeftValue(node1));
    }

    public static void main(String[] args) {
        FindBottomLeftTreeValue mdt = new FindBottomLeftTreeValue();
        mdt.initialize();
    }
}
