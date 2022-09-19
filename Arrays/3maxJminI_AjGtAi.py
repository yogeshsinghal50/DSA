'''
https://www.techiedelight.com/find-maximum-value-index-array/
Given an integer array `nums`, find the maximum value of `j-i` such that `nums[j] > nums[i]`.

For example,

Input: nums = [9, 10, 2, 6, 7, 12, 8, 1]
Output: 5
Explanation: The maximum difference is 5 for i = 0, j = 5

Input: nums = [9, 2, 1, 6, 7, 3, 8]
Output: 5
Explanation: The maximum difference is 5 for i = 1, j = 6

Input: nums = [8, 7, 5, 4, 2, 1]
Output: -1 (or any other negative number)
Explanation: Array is sorted in decreasing order.

'''
		
class Solution:
	def findMaxDiff(self, nums: List[int]) -> int:
		if not nums:
			return -1
		n = len(nums)
		j_nums = [0]*n
		j_nums[n-1] = nums[n-1]
		for i in reversed(range(n-1)):
			j_nums[i] = max(j_nums[i+1],nums[i])
		i = 0
		j = 0
		max_diff = -1
		while i < n and j < n:
			if nums[i] < j_nums[j]:
				max_diff = max(max_diff,j - i)
				j += 1
			else:
				i += 1
		return max_diff