#!/usr/bin/env python3

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ solution by Abdellah Lafia 
#_____________________________________________________________________________________

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        h = 0
        l = 99999
        for i in prices:
            h = i if i > h
            l = i if i < l
        return h - l
