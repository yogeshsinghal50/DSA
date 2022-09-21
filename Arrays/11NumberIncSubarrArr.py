'''
https://www.techiedelight.com/count-strictly-increasing-sub-arrays/
Given an integer array, count the total number of strictly increasing contiguous subarrays in it.

Input: [1, 2, 4, 4, 5]
Output: 4
Explanation: The total number of strictly increasing subarrays are [1, 2], [1, 2, 4], [2, 4], [4, 5]

Input: [1, 3, 2]
Output: 1
Explanation: The total number of strictly increasing subarrays is [1, 3]

Input: [5, 4, 3, 2, 1]
Output: 0
Explanation: The total number of strictly increasing subarrays is 0

'''

class Solution:
	def getCount(self, nums: List[int]) -> int:
		j = 1
		count = 0
		n = 1
		while j < len(nums):
			if nums[j] > nums[j-1]:
				count += n
				n += 1
			else:
				n = 1
			j += 1
		return count