'''
https://www.techiedelight.com/find-odd-occurring-elements-array/
Given an array having elements between 0 and 31, find elements that occur an odd number of times without using the extra space.

Input : [5, 8, 2, 5, 8, 2, 8, 5, 1, 8, 2]
Output: {5, 2, 1}

Explanation:

1 occurs once.
2 and 5 occurs thrice.
8 occurs four times.

Assume valid input.

'''

class Solution:
	def findOddOccuringElements(self, nums: List[int]) -> Set[int]:
		s = set()
		xor = 0
		for num in nums:
			xor = xor ^ (1 << num)
		for num in nums:
			if xor & (1 << num):
				s.add(num)
				xor = xor ^ (1 << num)
		return s

