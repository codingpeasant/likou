package DFS;

// https://leetcode.com/problems/search-in-a-binary-search-tree/
public class SearchBinarySearchTree {
    public TreeNode searchBST(TreeNode root, int val) {
        if (root == null) {
            return null;
        }

        if (root.val == val) return root;
        else if (root.val < val) return searchBST(root.right, val);
        else return searchBST(root.left, val);
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

        preOrder(searchBST(node1, 5));
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
        SearchBinarySearchTree mdt = new SearchBinarySearchTree();
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
