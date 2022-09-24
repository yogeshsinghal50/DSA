'''
https://www.techiedelight.com/calculate-frequency-elements-present-array-specified-range/
Given an unsorted integer array whose elements lie in the range 0 to `n-1` where `n` is the array size, calculate the frequency of all array elements in linear time and using constant space.

Input : [2, 3, 1, 3, 1, 1]
Output: {1: 3, 2: 1, 3: 2}

Explanation:

Element 1 appears thrice.
Element 2 appears once.
Element 3 appears twice.

'''

class Solution:
	def findFrequency(self, nums: List[int]) -> Dict[int, int]:
		n = len(nums)
		dict_ = {}
		for i,num in enumerate(nums):
			nums[num%n] += n
		for i,num in enumerate(nums):
			if num >= n:
				dict_[i] = num//n
		return dict_
