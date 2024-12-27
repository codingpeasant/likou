package DFS;

import com.sun.source.tree.Tree;

import java.util.ArrayList;
import java.util.List;

// https://leetcode.com/problems/maximum-depth-of-binary-tree/
public class MaxDepthOfTree {
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

    public int maxDepth(TreeNode root) {
        int maxDepth = 0;
        return Dfs(root, maxDepth);
    }

    public int Dfs(TreeNode node, int currentDepth) {
        if (node == null) {
            return currentDepth;
        }

        currentDepth++;
        return Math.max(Dfs(node.left, currentDepth), Dfs(node.right, currentDepth));
    }

    // find the ancestors of a node
    public void dfs(TreeNode root, TreeNode target, List<TreeNode> path, List<List<TreeNode>> res) {
        if (root == null) {
            return;
        }

        if (root.val == target.val) {
            res.add(new ArrayList<>(path));
            return;
        }

        path.add(root);
        dfs(root.left, target, path, res);
        dfs(root.right, target, path, res);
        path.remove(path.size() - 1);
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(10);
        TreeNode node3 = new TreeNode(20);
        TreeNode node4 = new TreeNode(15);
        TreeNode node5 = new TreeNode(7);
        TreeNode node6 = new TreeNode(10);

        node1.left = node2;
        node1.right = node3;
        node3.left = node4;
        node3.right = node5;
        node5.right = node6;

        System.out.println("The max depth of tree is: " + maxDepth(node1));

        List<List<TreeNode>> resList = new ArrayList<>();
        List<TreeNode> initialList = new ArrayList<>();
        dfs(node1, node6, initialList, resList);
        resList.forEach((list) -> {
            for (TreeNode node : list) {
                System.out.print(node.val + " ");
            }
            System.out.print('\n');
        });
    }

    public static void main(String[] args) {
        MaxDepthOfTree mdt = new MaxDepthOfTree();
        mdt.initialize();
    }
}
