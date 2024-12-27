package DataStructure;

import java.util.HashSet;
import java.util.Set;

// https://leetcode.ca/2020-06-06-1650-Lowest-Common-Ancestor-of-a-Binary-Tree-III/
public class LowestCommonAncestorBinaryTreeIII {
    class Node {
        public int val;
        public Node parent;
    }

    public Node lowestCommonAncestor(Node p, Node q) {
        Set<Node> set = new HashSet<>();
        Node temp = p;
        while (temp != null) {
            set.add(temp);
            temp = temp.parent;
        }
        temp = q;
        while (temp != null) {
            if (set.contains(temp))
                break;
            else
                temp = temp.parent;
        }
        return temp;
    }
}
