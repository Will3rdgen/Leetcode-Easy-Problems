#!/usr/bin/env python

'''
    File name: move-zeroes.py
    Author: William Merritt
    Date created: 5/28/2018
    Date last modified: 5/28/2018
    Python Version: 3.6
    Leetcode Link: https://leetcode.com/problems/move-zeroes/description/

    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

    Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
 '''

# Time Complexity: O(n) 
# Space Complexity: O(1) 

class Solution:
    '''
    @param self 
    @param nums: List[int]
    @return void
    '''
    def moveZeroes(self, nums):
        for num in nums: 
            if num == 0:
                nums.append(num)
                nums.remove(num)
            