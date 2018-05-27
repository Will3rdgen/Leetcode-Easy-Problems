#!/usr/bin/env python

'''
    File name: single-number.py
    Author: William Merritt
    Date created: 5/27/2018
    Date last modified: 5/27/2018
    Python Version: 3.6
    Leetcode Link: https://leetcode.com/problems/single-number/description/

    Given a non-empty array of integers, every element appears twice except for one. Find that single one.  
    Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

    Example 1:
    Input: [2,2,1]
    Output: 1 
 '''

# Time Complexity: O(n) 
# Space Complexity : O(n) 

class Solution(object):
    # @param self 
    # @param nums, List[int]
    # @return integer 
    def singleNumber(self, nums):

        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]


