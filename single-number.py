#!/usr/bin/env python

'''
    File name: single-number.py
    Author: William Merritt
    Date created: 5/27/2018
    Date last modified: 5/27/2018
    Python Version: 3.6
'''
# Time Complexity: O(n) 
# Space Complexity : O(n) 


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]