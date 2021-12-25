package DFS;

// https://leetcode.com/problems/validate-binary-search-tree/
public class ValidateBST {
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

    public boolean isValidBST(TreeNode root) {
        return helper1(root, null, null);
    }

    public boolean helper1(TreeNode root, Integer upper, Integer lower) {
        if (root == null) return true;
        if (upper != null && root.val >= upper) return false;
        if (lower != null && root.val <= lower) return false;
        boolean leftBST = helper1(root.left, root.val, lower);
        boolean rightBST = helper1(root.right, upper, root.val);
        return leftBST && rightBST;
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(5);
        TreeNode node4 = new TreeNode(4);
        TreeNode node5 = new TreeNode(7);
        TreeNode node6 = new TreeNode(6);

        node1.left = node2;
        node1.right = node3;
        node3.left = node4;
        node3.right = node5;
        node5.right = node6;

        System.out.println("Is BST: " + isValidBST(node2));
    }

    public static void main(String[] args) {
        ValidateBST mdt = new ValidateBST();
        mdt.initialize();
    }
}
