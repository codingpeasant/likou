package BFS;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

// https://leetcode.com/problems/binary-tree-right-side-view/
public class BinaryTreeRightSideView {
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

    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> visibleNodes = new ArrayList<>();
        if (root == null) return visibleNodes;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while(!queue.isEmpty()) {
            int size = queue.size(); // total number of nodes in this level
            for (int i = 0; i < size; i++) {
                TreeNode cur = queue.poll();
                if (i == size - 1) { // when encountering the last in this level
                    visibleNodes.add(cur.val);
                }
                if (cur.left != null) {
                    queue.add(cur.left);
                }
                if (cur.right != null) {
                    queue.add(cur.right);
                }
            }
        }
        return visibleNodes;
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

        System.out.println("Visible list: " + rightSideView(node1));
    }

    public static void main(String[] args) {
        BinaryTreeRightSideView mdt = new BinaryTreeRightSideView();
        mdt.initialize();
    }
}
