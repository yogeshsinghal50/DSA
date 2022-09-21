'''
https://www.techiedelight.com/find-longest-subsequence-formed-by-consecutive-integers/
Given an integer array, find the length of the longest subsequence formed by the consecutive integers. The subsequence should contain all distinct values, and the character set should be consecutive, irrespective of its order.

Input : [2, 0, 6, 1, 5, 3, 7]
Output: 4
Explanation: The longest subsequence formed by the consecutive integers is [2, 0, 1, 3]. It has distinct values and length 4.

Input : [1, 4, 4, 0, 2, 3]
Output: 5
Explanation: The longest subsequence formed by the consecutive integers is [1, 4, 4, 0, 2, 3]. The distinct subsequence is [1, 4, 0, 2, 3] having length 5.

Input : [2, 4, 6, 3, 7, 4, 8, 1]
Output: 4
Explanation: The longest subsequence formed by the consecutive integers is [2, 4, 3, 4, 1]. The distinct subsequence is [2, 4, 3, 1] having length 4.

'''

class Solution:
	def findMaxLenSubseq(self, nums: List[int]) -> int:
		if not nums:
			return 0
		s = set(nums)
		max_len = 1
		for n in nums:
			i = 1
			if n-i not in s:
				while n + i in s:
					i += 1
			max_len = max(max_len,i)
		return max_len