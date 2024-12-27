package DFS;

// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
public class ConvertArrayToBST {
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

    public TreeNode createBST(int[] nums, int left, int right) {
        if (left > right) {
            return null;
        }

        int mid = (left + right) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = createBST(nums, left, mid - 1);
        root.right = createBST(nums, mid + 1, right);
        return root;
    }

    public TreeNode sortedArrayToBST(int[] nums) {
        return createBST(nums, 0, nums.length - 1);
    }

    public void initialize() {
        int[] nums = {-10,-3,0,5,9, 10};

        preOrder(sortedArrayToBST(nums));
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
        ConvertArrayToBST mdt = new ConvertArrayToBST();
        mdt.initialize();
    }
}
