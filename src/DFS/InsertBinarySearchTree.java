package DFS;

// https://leetcode.com/problems/insert-into-a-binary-search-tree/
public class InsertBinarySearchTree {

    public TreeNode insertIntoBST(TreeNode root, int val) {
        if(root == null){
            return new TreeNode(val);
        }
        helper(root, val);
        return root;
    }

    private void helper(TreeNode root, int val) {
        if (root == null) {
            return;
        }
        // create as a child when the parent current child is null
        if (root.val < val && root.right == null) {
            root.right = new TreeNode(val);
            return;
        } else if (root.val > val && root.left == null) {
            root.left = new TreeNode(val);
        } else if (root.val < val) {
            helper(root.right, val);
        } else {
            helper(root.left, val);
        }
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(5);
        TreeNode node4 = new TreeNode(4);
        TreeNode node5 = new TreeNode(7);
        TreeNode node6 = new TreeNode(10);

        node1.left = node2;
        node1.right = node3;
        node3.left = node4;
        node3.right = node5;
        node5.right = node6;

        preOrder(insertIntoBST(node1, 6));
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
        InsertBinarySearchTree mdt = new InsertBinarySearchTree();
        mdt.initialize();
    }

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
}
