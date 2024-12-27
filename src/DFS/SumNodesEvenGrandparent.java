package DFS;

// https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
public class SumNodesEvenGrandparent {
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

    public int sumEvenGrandparent(TreeNode root) {
        return helper(root, 1, 1);
    }

    public int helper(TreeNode node, int p, int gp) {
        if (node == null) return 0;
        return helper(node.left, node.val, p) + helper(node.right, node.val, p) + (gp % 2 == 0 ? node.val : 0);
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(2);
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

        System.out.println("The max depth of tree is: " + sumEvenGrandparent(node1));
    }

    public static void main(String[] args) {
        SumNodesEvenGrandparent mdt = new SumNodesEvenGrandparent();
        mdt.initialize();
    }
}
