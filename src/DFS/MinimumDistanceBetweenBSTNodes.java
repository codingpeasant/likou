package DFS;

// https://leetcode.com/problems/minimum-distance-between-bst-nodes/
public class MinimumDistanceBetweenBSTNodes {
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

    Integer res;
    Integer prev;

    public int minDiffInBST(TreeNode root) {
        res = Integer.MAX_VALUE;
        prev = null;
        inorder(root);
        return res;
    }
// why in order?
//    7
//    /\
//    4 8
//    /\
//    1 6
//      /
//      5
// pre = 4, root.val = 5 is the min
    public void inorder(TreeNode root) {
        if (root == null) return;
        inorder(root.left);
        if (prev != null) {
            res = Math.min(res, root.val - prev);
        }
        prev = root.val;
        inorder(root.right);
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

        System.out.println(minDiffInBST(node1));
    }

    public static void main(String[] args) {
        MinimumDistanceBetweenBSTNodes mdt = new MinimumDistanceBetweenBSTNodes();
        mdt.initialize();
    }
}
