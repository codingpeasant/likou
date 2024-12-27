package BFS;

import java.util.LinkedList;
import java.util.Queue;

// https://leetcode.com/problems/check-completeness-of-a-binary-tree/
public class CheckCompletenessBinaryTree {
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

    public boolean isCompleteTree(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        // when true, stop adding more nodes and start to examine if there is any none-null nodes after
        boolean gotNull = false;

        while (!queue.isEmpty()) {
            TreeNode cur = queue.poll();
            if (cur == null && !gotNull) {
                gotNull = true;
            } else if (gotNull && cur != null) {
                return false;
            } else if (!gotNull && cur != null){
                queue.add(cur.left);
                queue.add(cur.right);
            }
        }
        return true;
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
        //node2.right = node5;

        node3.right = node6;
        //node3.right = node7;

        System.out.println("Is complete: " + isCompleteTree(node1));
    }

    public static void main(String[] args) {
        CheckCompletenessBinaryTree r = new CheckCompletenessBinaryTree();
        r.initialize();
    }
}
