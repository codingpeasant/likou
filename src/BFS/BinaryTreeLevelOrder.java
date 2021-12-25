package BFS;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

// https://leetcode.com/problems/binary-tree-level-order-traversal/
public class BinaryTreeLevelOrder {
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

    public List<List<Integer>> levelOrder(TreeNode root) {
        if (root == null) return null;

        Queue<TreeNode> bfsQueue = new LinkedList<>();
        List<List<Integer>> response = new ArrayList<>();

        bfsQueue.add(root);

        while (!bfsQueue.isEmpty()) {
            int count = bfsQueue.size(); // the key for level order traversal
            List<Integer> levelNodes = new ArrayList<>();
            for (int i = 0; i < count; i++) {
                TreeNode cur = bfsQueue.poll();
                levelNodes.add(cur.val);

                if (cur.left != null) {
                    bfsQueue.add(cur.left);
                }

                if (cur.right != null) {
                    bfsQueue.add(cur.right);
                }
            }
            response.add(levelNodes);
        }
        return response;
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

        List<List<Integer>> res = levelOrder(node1);
        for (List<Integer> level: res) {
            for (int val: level) {
                System.out.print(val + ", ");
            }
            System.out.print("\n");
        }
    }

    public static void main(String[] args) {
        BinaryTreeLevelOrder mdt = new BinaryTreeLevelOrder();
        mdt.initialize();
    }
}
