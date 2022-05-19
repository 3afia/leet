#!/usr/bin/env python3

# https://leetcode.com/problems/valid-anagram/ solution by Abdellah Lafia 
#_____________________________________________________________________________________
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm_s = {}
        hm_t = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            # count letters in s, add count to hm_s
            if s[i] in hm_s:
                hm_s[s[i]] +=1
            else:
                hm_s[s[i]] = 1
            # count letters in t, add count to hm_t
            if t[i] in hm_t:
                hm_t[t[i]] +=1
            else:
                hm_t[t[i]] = 1
        return hm_s == hm_t
            
