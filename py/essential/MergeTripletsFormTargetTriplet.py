# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/?envType=problem-list-v2&envId=plakya4j
# Neet

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Because we can merge triplets any number of times, we can just check if the maximum values of each index
        # Initialize a set to keep track of the maximum values
        max_values = [0, 0, 0]

        # Iterate through each triplet
        for triplet in triplets:
            # Check if the triplet is valid
            if all(triplet[i] <= target[i] for i in range(3)):
                # Update the maximum values
                max_values = [max(max_values[i], triplet[i]) for i in range(3)]

        # Return True if the maximum values match the target, False otherwise
        return max_values == target