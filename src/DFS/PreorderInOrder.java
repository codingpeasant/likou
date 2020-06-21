package DFS;

import BFS.PathSum;

import java.util.HashMap;

public class PreorderInOrder {
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

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder == null || inorder == null || preorder.length == 0 || inorder.length == 0 || preorder.length != inorder.length) {
            return null;
        }

        HashMap<Integer, Integer> inMap = new HashMap<Integer, Integer>();
        for (int i = 0; i < inorder.length; i++) {
            inMap.put(inorder[i], i);
        }

        return build(preorder, inorder, 0, inorder.length - 1, inMap);
    }

    public TreeNode build(int[] preOrder, int[] inOrder, int inOrderLeft, int inOrderRight, HashMap<Integer, Integer> inMap) {
        if (inOrderLeft > inOrderRight) {
            return null;
        }

        int rootVal = preOrder[index++];
        TreeNode root = new TreeNode(rootVal);
        int cut = inMap.get(rootVal);
        root.left = build(preOrder, inOrder, inOrderLeft, cut - 1, inMap);
        root.right = build(preOrder, inOrder, cut + 1, inOrderRight, inMap);
        return root;
    }

    public void initialize() {
        int[] preorder = {3,9,20,15,7};
        int[] inorder = {9,3,15,20,7};

        preOrder(buildTree(preorder, inorder));
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
        PreorderInOrder mdt = new PreorderInOrder();
        mdt.initialize();
    }
}
