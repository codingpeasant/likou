package DFS;

// https://leetcode.com/problems/convert-bst-to-greater-tree/
public class ConvertBSTGreaterTree {
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

    public TreeNode convertBST(TreeNode root) {
        inOrderTranversal(root);
        return root;
    }

    int sum = 0;
    private void inOrderTranversal(TreeNode root) {
        if (root == null) {
            return;
        }

        inOrderTranversal(root.right);
        root.val += sum;
        sum = root.val;
        inOrderTranversal(root.left);
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


        preOrder(convertBST(node1));
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
        ConvertBSTGreaterTree mdt = new ConvertBSTGreaterTree();
        mdt.initialize();
    }
}
