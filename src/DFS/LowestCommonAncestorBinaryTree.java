package DFS;

public class LowestCommonAncestorBinaryTree {
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

    // this is a tree search and backtrack. When find the values, back track to the first node with results from subtrees
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == p || root == q || root == null)
            return root;
        TreeNode left = lowestCommonAncestor(root.left,  p,  q);
        TreeNode right = lowestCommonAncestor(root.right,  p,  q);
        if (left == null)
            return right;
        else if (right == null)
            return left;
        else
            return root;
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(4);
        TreeNode node2 = new TreeNode(2);
        TreeNode node3 = new TreeNode(6);
        TreeNode node4 = new TreeNode(1);
        TreeNode node5 = new TreeNode(3);
        TreeNode node6 = new TreeNode(5);
        TreeNode node7 = new TreeNode(7);

        node1.left = node2;
        node1.right = node3;

        node2.left = node4;
        node2.right = node5;

        node3.left = node6;
        node3.right = node7;

        System.out.println("LCA is: " + lowestCommonAncestor(node1, node7, node2).val);
    }

    public static void main(String[] args) {
        LowestCommonAncestorBinaryTree r = new LowestCommonAncestorBinaryTree();
        r.initialize();
    }
}
