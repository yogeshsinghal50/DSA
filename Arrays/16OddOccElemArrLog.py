'''
https://www.techiedelight.com/find-odd-occurring-element-logn-time/
Given an integer array where every element appears an even number of times, except one element which appears an odd number of times. If the identical elements appear in pairs in the array and there cannot be more than two consecutive occurrences of an element, find the odd occurring element in logarithmic time and constant space.

Input: [2, 2, 3, 3, 2, 2, 4, 4, 3, 1, 1]
Output: 3

Assume valid input. For instance, both arrays [1, 2, 1] and [1, 1, 2, 2, 2, 3, 3] are invalid. The first one doesn't have identical elements appear in pairs, and the second one contains three consecutive instances of an element.

'''

class Solution:
	def findOddOccuringElement(self, nums: List[int]) -> int:
		low = 0
		high = len(nums) - 1
		while low < high:
			mid = low + (high-low)//2
			if mid%2 == 0:
				if nums[mid] == nums[mid+1]:
					low = mid + 1
				elif nums[mid] == nums[mid-1]:
					high = mid - 1
				else:
					return nums[mid]
			else:
				if nums[mid] == nums[mid-1]:
					low = mid + 1
				elif nums[mid] == nums[mid+1]:
					high = mid - 1
				else:
					return nums[mid]
		return nums[low]