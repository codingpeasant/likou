package DFS;

import java.util.ArrayList;
import java.util.List;

// https://leetcode.com/problems/unique-binary-search-trees-ii/
public class UniqueBinarySearchTrees2 {
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

    public List<TreeNode> generateTrees(int n) {
        return genTreeList(1,n);
    }

    private List<TreeNode> genTreeList (int start, int end) {
        List<TreeNode> list = new ArrayList<>();
        if (start > end) {
            list.add(null); // the caller is a leaf node; cannot just return here, otherwise the double for loop won't have anything to iterate on
        }
        for(int idx = start; idx <= end; idx++) {
            List<TreeNode> leftList = genTreeList(start, idx - 1);
            List<TreeNode> rightList = genTreeList(idx + 1, end);
            for (TreeNode left : leftList) { // all combination of left and right
                for(TreeNode right: rightList) {
                    TreeNode root = new TreeNode(idx);
                    root.left = left;
                    root.right = right;
                    list.add(root);
                }
            }
        }
        return list;
    }

    public void preOrder(TreeNode node) {
        if (node == null) {
            return;
        }
        System.out.print(node.val + ", ");
        preOrder(node.left);
        preOrder(node.right);
    }


    public static void main(String[] args) {
        UniqueBinarySearchTrees2 mdt = new UniqueBinarySearchTrees2();
        mdt.generateTrees(3).forEach(mdt::preOrder);
    }
}
