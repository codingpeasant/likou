package DFS;

// https://leetcode.ca/2016-09-23-298-Binary-Tree-Longest-Consecutive-Sequence/
public class LongestConsecutiveSequenceBinary {
    int answer = 0;

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

    int longestConsecutive(TreeNode root) {
        if (root == null) return 0;
        dfs(root, 0, root.val);
        return answer;
    }

    private void dfs(TreeNode root, int cur, int expected) {
        if (root == null) return;
        if (root.val == expected) {
            cur++;
        } else {
            cur = 1;
        }

        answer = Math.max(answer, cur);

        dfs (root.left, cur, root.val + 1);
        dfs (root.right, cur, root.val + 1);
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(4);
        TreeNode node2 = new TreeNode(4);
        TreeNode node3 = new TreeNode(5);
        TreeNode node4 = new TreeNode(15);
        TreeNode node5 = new TreeNode(6);
        TreeNode node6 = new TreeNode(7);

        node1.left = node2;
        node1.right = node3;
        node3.left = node4;
        node3.right = node5;
        node5.right = node6;

        System.out.println("The longest is: " + longestConsecutive(node1));
    }

    public static void main(String[] args) {
        LongestConsecutiveSequenceBinary l = new LongestConsecutiveSequenceBinary();
        l.initialize();
    }
}
