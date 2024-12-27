package DFS;

import java.util.ArrayList;
import java.util.List;

// https://leetcode.com/problems/balance-a-binary-search-tree/
public class BalanceBinarySearchTree {
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

    public TreeNode balanceBST(TreeNode root) {
        ArrayList<Integer> sortedValues = new ArrayList<>();
        getSortedValues(root, sortedValues);

        int right = sortedValues.size() - 1;
        return getBST(sortedValues, 0, right);
    }

    private TreeNode getBST(List<Integer> sortedValues, int left, int right) {
        if (left > right) {
            return null;
        }

        int mid = left + (right - left) / 2;
        TreeNode root = new TreeNode(sortedValues.get(mid));
        root.left = getBST(sortedValues, left, mid - 1);
        root.right = getBST(sortedValues, mid + 1, right);
        return root;
    }

    private void getSortedValues(TreeNode root, List<Integer> sortedValues) { // in order traversal to get sorted order
        if (root == null) return;
        getSortedValues(root.left, sortedValues);
        sortedValues.add(root.val);
        getSortedValues(root.right, sortedValues);
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(3);
        TreeNode node5 = new TreeNode(7);
        TreeNode node2 = new TreeNode(9);
        TreeNode node6 = new TreeNode(10);
        TreeNode node4 = new TreeNode(15);
        TreeNode node3 = new TreeNode(20);

        node1.right = node5;
        node5.right = node2;
        node2.right = node6;
        node6.right = node4;
        node4.right = node3;

        System.out.println("Balanced: " + balanceBST(node1).val);
    }

    public static void main(String[] args) {
        BalanceBinarySearchTree mdt = new BalanceBinarySearchTree();
        mdt.initialize();
    }

}
