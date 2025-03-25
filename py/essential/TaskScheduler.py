# https://leetcode.com/problems/task-scheduler/description/?envType=problem-list-v2&envId=rab78cw1
# Grind

from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        ## APPROACH : HASHMAP ##
        ## LOGIC : TAKE THE MAXIMUM FREQUENCY ELEMENT AND MAKE THOSE MANY NUMBER OF SLOTS ##
        ##  Slot size = (n+1) if n
        # = 2 => slot size = 3 Example: {A:5, B:1} => ABxAxxAxxAxxAxx => indices of A = 0,2 and middle there should be n elements, so slot size should be n+1

        ## Ex: {A:6,B:4,C:2} n = 2
        ## final o/p will be
        ## slot size / cycle size = 3
        ## Number of rows = number of A's (most freq element)
        # [
        #     [A, B,      C],
        #     [A, B,      C],
        #     [A, B,      idle],
        #     [A, B,      idle],
        #     [A, idle,   idle],
        #     [A   -        - ],
        # ]
        #
        # so from above total time intervals = (max_freq_element - 1) * (n + 1) + (all elements with max freq)
        # ans   =     rows_except_last   * columns +        last_row

        ## but consider {A:5, B:1, C:1, D:1, E:1, F:1, G:1, H:1, I:1, J:1, K:1, L:1} n = 1
        ## total time intervals by above formula will be 4 * 2 + 1 = 9, which is less than number of elements, which is not possible. so we have to return max(ans, number of tasks)

        counts = list(Counter(tasks).values())
        most_repeats = max(counts)
        num_longest = counts.count(most_repeats)
        return max(len(tasks), (most_repeats - 1) * (n + 1) + num_longest)


s = Solution()
print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # 8
print(s.leastInterval(["A", "A", "A", "A", "B"], 2))
print(s.leastInterval(["A", "A", "A", "C", "C", "C", "B", "B", "B"], 3))
print(
    s.leastInterval(
        ["A", "A", "A", "A", "C", "C", "C", "B", "B", "B", "B", "D", "D", "D"], 2
    )
)
