package DFS;

import java.util.ArrayList;
import java.util.List;

public class BinaryTreePaths {
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

    public List<String> binaryTreePaths(TreeNode root) {
        ArrayList<String> answer = new ArrayList<>();
        if (root == null) return answer;
        dfs(root, answer, "");
        return answer;
    }

    private void dfs(TreeNode root, ArrayList<String> answer, String path) {
        path += root.val;
        if (root.left == null && root.right == null) {
            answer.add(path);
            return;
        }

        if (root.left != null) {
            dfs(root.left, answer,path + " -> ");
        }
        if (root.right != null) {
            dfs(root.right, answer,path + " -> ");
        }
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

        System.out.println(binaryTreePaths(node1));
    }

    public static void main(String[] args) {
        BinaryTreePaths b = new BinaryTreePaths();
        b.initialize();
    }
}
