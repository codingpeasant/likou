package DFS;

import java.util.HashMap;
import java.util.Map;

// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
public class ConstructBinaryTreeInorderPostorderTraversal {
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

    int index = 0;
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder.length != postorder.length || inorder.length == 0 || postorder.length == 0) {
            return null;
        }
        Map<Integer, Integer> inOrderMap = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            inOrderMap.put(inorder[i], i);
        }
        index = postorder.length - 1;
        return build(postorder, inOrderMap, 0, index);
    }


    private TreeNode build(int[] postOrder, Map<Integer, Integer> inOrderMap, int left, int right) {
        if (left > right) {
            return null;
        }
        int rootValue = postOrder[index--];
        TreeNode newRoot = new TreeNode(rootValue);
        int cut = inOrderMap.get(rootValue);
        newRoot.right = build(postOrder, inOrderMap, cut + 1, right);
        newRoot.left = build(postOrder, inOrderMap, left, cut - 1);
        return newRoot;
    }

    public void initialize() {
        int[] postorder = {9,15,7,20,3};
        int[] inorder = {9,3,15,20,7};

        preOrder(buildTree(inorder, postorder));
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
        ConstructBinaryTreeInorderPostorderTraversal mdt = new ConstructBinaryTreeInorderPostorderTraversal();
        mdt.initialize();
    }
}
