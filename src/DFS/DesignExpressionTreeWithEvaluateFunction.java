package DFS;

import java.util.Stack;

// https://leetcode.ca/2020-05-15-1628-Design-an-Expression-Tree-With-Evaluate-Function/
public class DesignExpressionTreeWithEvaluateFunction {
    class Node {
        String val;
        Node left, right;

        Node(String val, Node left, Node right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }

        class TreeBuilder {
            Node buildTree(String[] postfix) {
                Stack<Node> stack = new Stack<>();
                for (String s : postfix) {
                    switch (s) {
                        case "+":
                        case "-":
                        case "*":
                        case "/":
                            stack.push(new Node(s, stack.pop(), stack.pop()));
                            break;
                        default:
                            stack.push(new Node(s, null, null));
                    }
                }
                return stack.pop();
            }
        }

        public int evaluate() {
            if (left == null && right == null)
                return Integer.parseInt(val);

            int l = left.evaluate();
            int r = right.evaluate();

            switch (val) {
                case "+":
                    return l + r;
                case "-":
                    return r - l;
                case "*":
                    return l * r;
                case "/":
                    return r / l;
            }
            return -1;
        }
        // define your fields here
    }

    ;
}
