package DFS;

public class FindDistanceBetween2NodesBST {
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

    public int bstDistance(TreeNode root, int node1, int node2) {
        if (root == null) return -1;
        TreeNode lca = lca(root, node1, node2);
        return getDistance(lca, node1) + getDistance(lca, node2);
    }

    private TreeNode lca(TreeNode root, int node1, int node2) {
        if (root.val < node1 && root.val < node2) {
            return lca(root.right, node1, node2);
        } else if (root.val > node1 && root.val > node2) {
            return lca(root.left, node1, node2);
        } else {
            return root;
        }
    }

    private int getDistance(TreeNode root, int node) {
        if (root.val == node) {
            return 0;
        } else if (root.val > node) {
            return 1 + getDistance(root.left, node);
        } else {
            return 1 + getDistance(root.right, node);
        }
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(9);
        TreeNode node3 = new TreeNode(20);
        TreeNode node4 = new TreeNode(15);
        TreeNode node5 = new TreeNode(7);
        TreeNode node6 = new TreeNode(10);

        node2.left = node5;
        node2.right = node4;
        node5.left = node1;
        node5.right = node2;
        node4.left = node6;
        node4.right = node3;

        System.out.println("The distance: " + bstDistance(node2, 20, 10));
    }

    public static void main(String[] args) {
        FindDistanceBetween2NodesBST mdt = new FindDistanceBetween2NodesBST();
        mdt.initialize();
    }
}
