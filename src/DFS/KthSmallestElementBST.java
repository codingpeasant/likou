package DFS;

// https://leetcode.com/problems/kth-smallest-element-in-a-bst/
public class KthSmallestElementBST {
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

    int result = Integer.MIN_VALUE;
    int count = 0;
    public int kthSmallest(TreeNode root, int k) {
        traverse(root, k);
        return result;
    }

    public void traverse(TreeNode root, int k) {
        if (root == null) {
            return;
        }

        traverse(root.left, k); // inorder
        count++;
        if (count == k) {
            result = root.val;
            return;
        }

        traverse(root.right, k);
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(1);
        TreeNode node3 = new TreeNode(4);
        TreeNode node4 = new TreeNode(2);

        node1.left = node2;
        node1.right = node3;
        node2.right = node4;

        System.out.println(kthSmallest(node1, 2));
    }

    public static void main(String[] args) {
        KthSmallestElementBST mdt = new KthSmallestElementBST();
        mdt.initialize();
    }
}
