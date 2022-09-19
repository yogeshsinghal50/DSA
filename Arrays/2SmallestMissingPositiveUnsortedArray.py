'''
https://www.techiedelight.com/find-smallest-missing-positive-number-unsorted-array/
Given an unsorted integer array, find the smallest missing positive integer in it.

Input: [1, 4, 2, -1, 6, 5]
Output: 3

Input: [1, 2, 3, 4]
Output: 5

'''

class Solution:
	def findPivot(self,nums : List[int]) -> int:
		pvt = 0
		for i,n in enumerate(nums):
			if n > 0:
				temp = nums[pvt]
				nums[pvt] = nums[i]
				nums[i] = temp
				pvt += 1
		return pvt
		
	def findSmallestMissingNumber(self, nums: List[int]) -> int:
		pvt = self.findPivot(nums)
		for i in range(pvt):
			val = abs(nums[i])
			if val - 1 < pvt and nums[val-1] >=0:
				nums[val-1] = -nums[val-1]
		for i,n in enumerate(nums):
			if n > 0:
				return i + 1
		return pvt + 1	