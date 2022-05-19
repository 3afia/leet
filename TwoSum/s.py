#!/usr/bin/env python3

# https://leetcode.com/problems/two-sum/ solution by Abdellah Lafia

#___________________________________________________________________
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        l = len(nums)
        s = 1
        for i in range(l):
            for j in range(s, l):
                if nums[i] + nums[j] == target:
                    return [i,j]
            s += 1
