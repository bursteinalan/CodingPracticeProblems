def problem1():
	'''
	Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

	Example 1:

	Input: n = 12
	Output: 3 
	Explanation: 12 = 4 + 4 + 4.
	Example 2:

	Input: n = 13
	Output: 2
	Explanation: 13 = 4 + 9.
	'''

def problem2():
	'''
	Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

	a mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

	2:abc
	3:def
	4:ghi
	5:jkl
	6:mno
	7:pqrs
	8:tuv
	9:wxyz

	Example:

	Input: "23"
	Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
	Note:

	Although the above answer is in lexicographical order, your answer could be in any order you want.
	'''

def problem3():
	'''
	Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
	An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
	You may assume all four edges of the grid are all surrounded by water.

	Example 1:

	Input:
	11110
	11010
	11000
	00000

	Output: 1
	Example 2:

	Input:
	11000
	11000
	00100
	00011

	Output: 3
	'''

def problem4():
	'''
	Given preorder and inorder traversal of a tree, construct the binary tree.

	Note:
	You may assume that duplicates do not exist in the tree.

	For example, given

	preorder = [3,9,20,15,7]
	inorder = [9,3,15,20,7]
	Return the following binary tree:

	    3
	   / \
	  9  20
	    /  \
	   15   7
	'''

def problem5():
	'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.	'''
