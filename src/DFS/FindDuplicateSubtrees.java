package DFS;

import java.util.*;

// https://leetcode.com/problems/find-duplicate-subtrees/
public class FindDuplicateSubtrees {
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

    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        List<TreeNode> res = new ArrayList<>();
        serialize(root, new HashMap<>(), res);
        return res;
    }

    private String serialize(TreeNode cur, Map<String, Integer> map, List<TreeNode> res) {
        if (cur == null) return "*";
        String serialized = cur.val + "," + serialize(cur.left, map, res) + "," + serialize(cur.right, map, res);
        System.out.println(serialized);
        map.put(serialized, map.getOrDefault(serialized, 0) + 1);
        if (map.get(serialized) == 2) res.add(cur); // only add once
        return serialized;
    }

    public void initialize() {
        TreeNode node1 = new TreeNode(3);
        TreeNode node2 = new TreeNode(9);
        TreeNode node3 = new TreeNode(20);
        TreeNode node4 = new TreeNode(15);
        TreeNode node5 = new TreeNode(20);
        TreeNode node6 = new TreeNode(15);

        node1.left = node2;
        node1.right = node3;
        node3.left = node4;
        node2.left = node5;
        node5.left = node6;

        findDuplicateSubtrees(node1).forEach(node -> System.out.println(node.val));
    }

    public static void main(String[] args) {
        FindDuplicateSubtrees mdt = new FindDuplicateSubtrees();
        mdt.initialize();
    }
}
