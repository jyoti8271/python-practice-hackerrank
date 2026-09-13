
# HackerRank Home
# |
# Prepare
# Certify
# Compete
# Search

# |
# Switch to..

# jyoti8271singh
# PrepareData StructuresLinked ListsDelete a Node
# Delete a Node
# 25 more points to get your first star!
# Rank: 4603042|Points: 5/30
# Problem Solving
# Problem
# Submissions
# Leaderboard
# Discussions
# Editorial
# This challenge is part of a tutorial track by MyCodeSchool and is accompanied by a video lesson.

# Delete the node at a given position in a linked list and return a reference to the head node. The head is at position 0. The list may be empty after you delete the node. In that case, return a null value.

# Example



# After removing the node at position , .

# Function Description

# Complete the deleteNode function in the editor below.

# deleteNode has the following parameters:
# - SinglyLinkedListNode pointer llist: a reference to the head node in the list
# - int position: the position of the node to remove

# Returns
# - SinglyLinkedListNode pointer: a reference to the head of the modified list

# Input Format

# The first line of input contains an integer , the number of elements in the linked list.
# Each of the next  lines contains an integer, the node data values in order.
# The last line contains an integer, , the position of the node to delete.

# Constraints

# , where  is the  element of the linked list.
# Sample Input

# 8
# 20
# 6
# 2
# 19
# 7
# 4
# 15
# 9
# 3
# Sample Output

# 20 6 2 7 4 15 9
# Explanation

# The original list is . After deleting the node at position , the list is .

# Language
# Pypy 3
# More
# 13839404142434445464748495051525354555657585960


# import math
# import os
# import random
# import re
# import sys

# class SinglyLinkedListNode:
#     def __init__(self, node_data):
#         self.data = node_data
#         self.next = None

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def insert_node(self, node_data):
#         node = SinglyLinkedListNode(node_data)

#         if not self.head:
#             self.head = node
#         else:
#             self.tail.next = node


#         self.tail = node

# def print_singly_linked_list(node, sep, fptr):
#     while node:
#         fptr.write(str(node.data))

#         node = node.next

#         if node:
#             fptr.write(sep)

# #
# # Complete the 'deleteNode' function below.
# #
# # The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# # The function accepts following parameters:
# #  1. INTEGER_SINGLY_LINKED_LIST llist
# #  2. INTEGER position
# #

# Line: 38 Col: 1

# Test against custom input
# Authorharsha_s
# DifficultyEasy
# Max Score5
# Submitted By336818
# Need Help?
# View discussions
# View editorial
# View top submissions
# rate this challenge

# MORE DETAILS
# Download problem statement
# Download sample test cases
# Suggest Edits
# Share on XShare on LinkedIn
# BlogScoringEnvironmentFAQAbout UsHelpdeskCareersTerms Of ServicePrivacy Policy
# #






def insertNodeAtPosition(llist, data, position):
    ##creating the new node
    new_node = SinglyLinkedListNode(data)
    #if the given position==0 the node align at the left position and it behave like as a head
    
    if position == 0:
        new_node.next = llist
        return new_node
    
    else:
        current = llist
        # setting the position
        for _ in range(position - 1):
            current = current.next
        
        ##adding the pointers of new node to existing left and right node     
        new_node.next = current.next
        current.next = new_node
        return llist