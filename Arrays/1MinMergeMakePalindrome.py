'''
https://www.techiedelight.com/find-minimum-number-merge-operations-make-array-palindrome/
Given a list of non-negative integers, find the minimum number of merge operations to make it a palindrome.

Input : [6, 1, 3, 7]
Output: 1
Explanation: [6, 1, 3, 7] —> Merge 6 and 1 —> [7, 3, 7]

Input : [6, 1, 4, 3, 1, 7]
Output: 2
Explanation: [6, 1, 4, 3, 1, 7] —> Merge 6 and 1 —> [7, 4, 3, 1, 7] —> Merge 3 and 1 —> [7, 4, 4, 7]

Input : [1, 3, 3, 1]
Output: 0
Explanation: The list is already a palindrome

'''

class Solution:
	def findMin(self, arr: List[int]) -> int:
		i = 0
		j = len(nums) - 1
		count = 0
		while i < j:
			if arr[i] < arr[j]:
				arr[i+1] += arr[i]
				i += 1
				count += 1
			elif arr[i] > arr[j]:
				arr[j-1] += arr[j]
				j -= 1
				count += 1
			else:
				i += 1
				j -= 1
		return count
