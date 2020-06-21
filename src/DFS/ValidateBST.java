package DFS;

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
        return helper(root, null, null);
    }

    public boolean helper(TreeNode root, Integer upper, Integer lower) {
        if (root == null) return true;
        if (upper != null && root.val >= upper) return false;
        if (lower != null && root.val <= lower) {
            return false;
        }

        if (!helper(root.right, upper, root.val))  {
            return false;
        }

        if (!helper(root.left, root.val, lower))  {
            return false;
        }

        return true;
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(9);
        TreeNode node3 = new TreeNode(20);

        node2.left = node1;
        node2.right = node3;

        System.out.println("Is BST: " + isValidBST(node2));
    }

    public static void main(String[] args) {
        ValidateBST mdt = new ValidateBST();
        mdt.initialize();
    }
}
