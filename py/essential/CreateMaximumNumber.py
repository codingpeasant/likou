# https://leetcode.com/problems/create-maximum-number/description/

from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def get_max_subseq(nums, k):
            stack = []
            for i, num in enumerate(nums):
                while stack and len(nums) - i + len(stack) > k and stack[-1] < num:
                    stack.pop()
                if len(stack) < k:
                    stack.append(num)
            return stack

        def merge(nums1, nums2):
            merged = []
            i, j = 0, 0
            while i < len(nums1) or j < len(nums2):
                if i >= len(nums1):
                    merged.append(nums2[j])
                    j += 1
                elif j >= len(nums2):
                    merged.append(nums1[i])
                    i += 1
                elif nums1[i:] > nums2[j:]:
                    merged.append(nums1[i])
                    i += 1
                else:
                    merged.append(nums2[j])
                    j += 1
            return merged

        ans = []
        # len(subseq1) + len(subseq2) = k
        for i in range(max(0, k - len(nums2)), min(len(nums1), k) + 1):
            print(i)
            j = k - i
            subseq1 = get_max_subseq(nums1, i)
            subseq2 = get_max_subseq(nums2, j)
            print(subseq1, subseq2)
            merged = merge(subseq1, subseq2)
            ans = max(ans, merged)
        return ans


s = Solution()
print(s.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5))
print(s.maxNumber([6, 7], [6, 0, 4], 5))
