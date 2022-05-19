#! /usr/bin/env python3

# https://leetcode.com/problems/valid-palindrome/ solution by Abdellah Lafia
#___________________________________________________________________________
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(x for x in list(''.join(s.lower().strip().split(' '))) if x.isalnum()) 
        s_ = ''.join(x for x in list(''.join(s.lower().strip().split(' '))[::-1]) if x.isalnum())
        return s == s_
