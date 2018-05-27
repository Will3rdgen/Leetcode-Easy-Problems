#!/usr/bin/env python

'''
    File name: reverse-string.py
    Author: William Merritt
    Date created: 5/27/2018
    Date last modified: 5/27/2018
    Python Version: 3.6
    Leetcode Link: https://leetcode.com/problems/reverse-string/description/

    Write a function that takes a string as input and returns the string reversed.

    Example:
    Given s = "hello", return "olleh".
 '''

# Time Complexity: O(n) 
# Space Complexity : O(n) 
 
class Solution:
    # @param self 
    # @param s, string 
    # @return string
    def reverseString(self, s):
        newString = s[::-1] 
        return (newString)
