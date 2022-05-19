#/usr/bin/env python3

# https://leetcode.com/problems/contains-duplicate/ solution by Abdellah Lafia
#______________________________________________________________________________
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
