package DFS;

import java.util.ArrayList;
import java.util.List;

// https://leetcode.ca/2016-11-28-364-Nested-List-Weight-Sum-II/
public class NestedListWeightSum2 {
    // This is the interface that allows for creating nested lists.
    // You should not implement it, or speculate about its implementation
    private interface NestedInteger {
        // @return true if this NestedInteger holds a single integer, rather than a nested list.
        public boolean isInteger();

        // @return the single integer that this NestedInteger holds, if it holds a single integer
        // Return null if this NestedInteger holds a nested list
        public Integer getInteger();

        // @return the nested list that this NestedInteger holds, if it holds a nested list
        // Return null if this NestedInteger holds a single integer
        public List<NestedInteger> getList();
    }

    private int maxDepth = 0;
    public int depthSumInverse(List<NestedInteger> nestedList) {
        if (nestedList == null || nestedList.size() == 0) {
            return 0;
        }

        getDepth(1, nestedList);

        return depthSumHelper(maxDepth, nestedList);
    }

    private void getDepth(int level, List<NestedInteger> nestedList) {
        maxDepth = Math.max(maxDepth, level);
        for (NestedInteger n : nestedList) {
            if (!n.isInteger()) {
                getDepth(level + 1, n.getList());
            }
        }
    }

    private int depthSumHelper(int depth, List<NestedInteger> nestedList) {
        int sum = 0;
        for (NestedInteger n : nestedList) {
            if (n.isInteger()) {
                sum += depth * n.getInteger();
            } else {
                sum += depthSumHelper(depth - 1, n.getList());
            }
        }

        return sum;
    }
}
