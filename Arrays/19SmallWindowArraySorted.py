'''
https://www.techiedelight.com/smallest-window-sorting-which-make-array-sorted/
Given an integer array, find the smallest window sorting which will make the entire array sorted in increasing order. The solution should return a pair consisting of the starting and ending index of the smallest window.

Input : [1, 2, 3, 7, 5, 6, 4, 8]
Output: (3, 6)
Explanation: The array can be sorted from index 3 to 6 to get sorted version.

Input : [1, 3, 2, 7, 5, 6, 4, 8]
Output: (1, 6)
Explanation: The array can be sorted from index 1 to 6 to get sorted version.

If the array is already sorted, the solution should return None.

Input : [1, 2, 3, 4, 5]
Output: None
Explanation: The array is already sorted.

'''

class Solution:
	def findSmallestWindow(self, nums: List[int]) -> Tuple[int]:
		if not nums:
			return None
		max_ = nums[0]
		first = 0
		for i,n in enumerate(nums):
			if n > max_:
				max_ = n 
			elif n < max_:
				first = i
		min_ = nums[-1]
		second = 0
		for i in reversed(range(len(nums))):
			if nums[i] < min_:
				min_ = nums[i]
			elif nums[i] > min_:
				second = i
		if first or second:
			return (second,first)
		return None

