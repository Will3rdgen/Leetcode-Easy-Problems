#!/usr/bin/env python

'''
    File name: max-depth-binary-tree.py
    Author: William Merritt
    Date created: 5/27/2018
    Date last modified: 5/27/2018
    Python Version: 3.6
    Leetcode Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

    Given a binary tree, find its maximum depth.
    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
    Note: A leaf is a node with no children.

    Example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7

    return its depth = 3.
 '''
# Time Complexity: O(n)
# Space Complexity: O(n) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param self 
    # @param root
    # @return int
    def maxDepth(self, root):

        if root is None:
            return 0 
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

# NOTE: Be able to write iterative solution to recursive problem         
        