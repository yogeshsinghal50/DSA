'''
https://www.techiedelight.com/divide-array-pairs-sum-divisible-k/
Given an integer array, determine whether it can be divided into pairs such that the sum of elements in each pair is divisible by a given positive integer `k`.

Input: nums[] = [3, 1, 2, 6, 9, 4], k = 5
Output: True
Explanation: Array can be divided into pairs {(3, 2), (1, 9), (4, 6)}, where the sum of elements in each pair is divisible by 5.

Input: nums[] = [2, 9, 4, 1, 3, 5], k = 6
Output: True
Explanation: Array can be divided into pairs {(2, 4), (9, 3), (1, 5)}, where the sum of elements in each pair is divisible by 6.

Input: nums[] = [3, 1, 2, 6, 9, 4], k = 6
Output: False
Explanation: Array cannot be divided into pairs where the sum of elements in each pair is divisible by 6.

'''

class Solution:
	def hasPairs(self, nums: List[int], k: int) -> bool:
		if len(nums) % 2 != 0:
			return False
		div_k = [0]*k
		for n in nums:
			div_k[n % k] += 1
		if div_k[0] % 2 != 0:
			return False
		i = 1
		j = k - 1
		while i < j:
			if div_k[i] != div_k[j]:
				return False
			i += 1 
			j -= 1 
		return True