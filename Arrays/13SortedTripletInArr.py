'''
https://www.techiedelight.com/find-sorted-triplet-array/
Given an integer array `nums`, efficiently find a sorted triplet such that `nums[i] < nums[j] < nums[k]` where `i < j < k`.

Input : [7, 3, 4, 2, 6]
Output: (3, 4, 6)

• If the input contains several sorted triplets, the solution can return any one of them.

Input : [5, 4, 3, 7, 6, 1, 9]
Output: (5, 7, 9) or (4, 7, 9) or (3, 7, 9) or (5, 6, 9) or (4, 6, 9) or (3, 6, 9)

• If no triplet exists, return an empty tuple.

Input : [5, 4, 3]
Output: ()

'''

class Solution:
	def findSortedTriplet(self, nums: List[int]) -> Tuple[int]:
		min_index = 0
		low = 0
		mid = -1
		if len(nums) < 3:
			return ()
		for i,n in enumerate(nums):
			if n <= nums[min_index]:
				min_index = i 
			elif mid == -1 or n <= nums[mid]:
				low = min_index
				mid = i 
			else:
				return nums[low],nums[mid],n 
		return ()
				
			

