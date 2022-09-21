'''
https://www.techiedelight.com/find-pair-with-given-sum-circularly-sorted-array/
Given a circularly sorted integer array, find a pair with a given sum. Assume there are no duplicates in the array, and the rotation is in an anti-clockwise direction around an unknown pivot.

• The solution can return pair in any order.

Input : nums[] = [10, 12, 15, 3, 6, 8, 9], target = 18
Output: (3, 15) or (15, 3)

Input : nums[] = [5, 8, 3, 2, 4], target = 12
Output: (4, 8) or (8, 4)

• If no pair with the given sum exists, the solution should return an empty tuple.

Input : nums[] = [9, 15, 2, 3, 7], target = 20
Output: ()

'''

class Solution:
	def findPivot(self, nums: List[int]) -> int:
		for i in range(len(nums)-1):
			if nums[i] > nums[i+1]:
				return i + 1	
		return len(nums)
		
	def findPair(self, nums: List[int], target: int) -> Tuple[int]:
		n = len(nums)
		if n<=1:
			return ()
		p = self.findPivot(nums)
		
		i = p%n
		j = p - 1
		while i != j:
			if nums[i] + nums[j] > target:
				j = (j - 1 + n)%n
			elif nums[i] + nums[j] < target:
				i  = (i + 1 )%n
			else:
				return (nums[i],nums[j])
		return ()
				