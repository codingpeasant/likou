package DFS;

// https://leetcode.com/problems/binary-tree-cameras
//        Return 0 if it's a leaf.
//        Return 1 if it's a parent of a leaf, with a camera on this node.
//        Return 2 if it's covered, without a camera on this node.
//
//        For each node,
//        if it has a child, which is leaf (node 0), then it needs camera.
//        if it has a child, which is the parent of a leaf (node 1), then it's covered.
//
//        If it needs camera, then res++ and we return 1.
//        If it's covered, we return 2.
//        Otherwise, we return 0.
public class BinaryTreeCamera {
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

    int res = 0;
    public int minCameraCover(TreeNode root) {
        return (helper(root) < 1 ? 1 : 0) + res;
    }

    private int helper(TreeNode root) {
        if (root == null) { // assume null nodes have been covered
            return 2;
        }
        if (root.left == null && root.right == null) { // leaf nodes
            return 0;
        }

        int left = helper(root.left);
        int right = helper(root.right);

        if (left == 0 || right == 0) { // is a parent of leaf, put camera - greedy
            res++;
            return 1;
        }
        return left == 1 || right == 1 ? 2 : 0; // if child has a camera: covered otherwise this node needs to put a camera
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

        System.out.println(minCameraCover(node1));
    }

    public static void main(String[] args) {
        BinaryTreeCamera mdt = new BinaryTreeCamera();
        mdt.initialize();
    }
}
