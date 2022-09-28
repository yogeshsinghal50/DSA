'''
https://www.techiedelight.com/find-subarrays-given-sum-array/

Given an integer array, find all contiguous subarrays with a given sum `k`.

Input : nums[] = [3, 4, -7, 1, 3, 3, 1, -4], k = 7
Output: {(3, 4), (3, 4, -7, 1, 3, 3), (1, 3, 3), (3, 3, 1)}

Since the input can have multiple subarrays with sum `k`, the solution should return a set containing all the distinct subarrays.

'''

class Solution:
	def getAllSubarrays(self, nums: List[int], target: int) -> Set[Tuple[int]]:
		d = {0:[-1]}
		sum_ = 0
		s = set()
		for i,num in enumerate(nums):
			sum_ += num
			if (sum_ - target) in d:
				values = d[sum_ - target]
				for value in values:
					s.add(tuple(nums[value+1:i+1]))
			d[sum_] = d.get(sum_,[]) + [i]
		return s
				
