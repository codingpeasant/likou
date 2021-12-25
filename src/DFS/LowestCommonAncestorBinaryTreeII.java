package DFS;

// https://leetcode.ca/2020-05-31-1644-Lowest-Common-Ancestor-of-a-Binary-Tree-II/
public class LowestCommonAncestorBinaryTreeII {
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

    // 计数找到了p和q的多少个节点
    private int count = 0;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode res = lca(root, p, q);
        // 如果都找到了，就可以返回res了，否则说明某个节点不存在，返回null
        return count == 2 ? res : null;
    }

    private TreeNode lca(TreeNode root, TreeNode p, TreeNode q) {
        // if found, return immediately; root == null means the subtrees from this root have neither p nor q
        if (root == null) {
            return null;
        }

        if (root == p || root == q) {
            count++;
            return root;
        }
        TreeNode left = lca(root.left, p, q);
        TreeNode right = lca(root.right, p, q);
        // if left subtree has p or q, and right subtree also has p or q
        if (left != null && right != null) return root;
        // return the subtree that has p or q; if both are null, return right, which is null.
        return left != null ? left : right;
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

        System.out.println("LCA is: " + lowestCommonAncestor(node1, node7, node2).val);
    }

    public static void main(String[] args) {
        LowestCommonAncestorBinaryTreeII r = new LowestCommonAncestorBinaryTreeII();
        r.initialize();
    }
}
