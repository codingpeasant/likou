package DFS;

// https://leetcode.com/problems/sum-of-left-leaves/
public class SumLeftLeaves {
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

    public int sumOfLeftLeaves(TreeNode root) {
        return dfs(root, false);
    }

    private int dfs(TreeNode root, boolean isLeft) {
        if (root == null) {
            return 0;
        }

        if (isLeft && root.left == null && root.right == null) {
            return root.val;
        } else {
            return dfs(root.left, true) + dfs(root.right, false);
        }
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(9);
        TreeNode node3 = new TreeNode(20);
        TreeNode node4 = new TreeNode(15);
        TreeNode node5 = new TreeNode(7);
        TreeNode node6 = new TreeNode(10);

        node1.left = node2;
        node1.right = node3;
        node3.left = node4;
        node3.right = node5;
        node5.left = node6;

        System.out.println("The left sum is: " + sumOfLeftLeaves(node1));
    }

    public static void main(String[] args) {
        SumLeftLeaves mdt = new SumLeftLeaves();
        mdt.initialize();
    }
}
