package DFS;

public class RangeSumBST {

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

    public int rangeSumBST(TreeNode root, int L, int R) {
        if (root == null) return 0;
        int sum = 0;
        if (root.val > R) sum += rangeSumBST(root.left, L, R); // left child is a possible candidate.
        if (root.val < L) sum += rangeSumBST(root.right, L, R);

        if (root.val <= R && root.val >= L) {
            sum += root.val + rangeSumBST(root.left, L, R) + rangeSumBST(root.right, L, R);
        }

        return sum;
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

        System.out.println("Sum is: " + rangeSumBST(node1, 5, 7));
    }

    public static void main(String[] args) {
        RangeSumBST r = new RangeSumBST();
        r.initialize();
    }
}
