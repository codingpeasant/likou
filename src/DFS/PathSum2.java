package DFS;

import java.util.ArrayList;
import java.util.List;
// https://leetcode.com/problems/path-sum-ii/
public class PathSum2 {
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

    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> paths = new ArrayList<>();
        findPath(root, sum, new ArrayList<>(), paths);
        return paths;
    }

    public void findPath(TreeNode root, int sum, List<Integer> path, List<List<Integer>> paths) {
        if (root == null) {
            return;
        }

        path.add(root.val);
        if (root.val == sum && root.left == null && root.right == null) {
            paths.add(path);
            return;
        }
        sum -= root.val;

        findPath(root.left, sum, new ArrayList<>(path), paths);
        findPath(root.right, sum, new ArrayList<>(path), paths);
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
        node5.right = node6;

        System.out.println(pathSum(node1, 12));
        System.out.println(pathSum(node1, 38));
    }

    public static void main(String[] args) {
        PathSum2 mdt = new PathSum2();
        mdt.initialize();
    }
}
