package DFS;

// https://leetcode.com/problems/maximum-binary-tree/
public class MaximumBinaryTree {
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

    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return construct(nums, 0, nums.length - 1);
    }

    private TreeNode construct(int[] nums, int from, int to) {
        if (from > to) {
            return null;
        }

        if (from == to) {
            return new TreeNode(nums[from]);
        }
        int maxIndex = getMaxValueIndex(nums, from, to);
        TreeNode root = new TreeNode(nums[maxIndex]);
        root.left = construct(nums, from, maxIndex - 1);
        root.right = construct(nums, maxIndex + 1, to);

        return root;

    }

    private int getMaxValueIndex(int[] nums, int from, int to) {
        int max = Integer.MIN_VALUE;
        int index = from;
        for (int i = from; i <= to; i++) {
            index = nums[i] > max ? i : index;
            max = Math.max(max, nums[i]);
        }
        return index;
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
        int[] input = {3,2,1,6,0,5};
        MaximumBinaryTree m = new MaximumBinaryTree();
        m.preOrder(m.constructMaximumBinaryTree(input));
    }
}
