'''
https://www.techiedelight.com/segregate-positive-negative-integers-using-mergesort/
Given an array of positive and negative integers, segregate them without changing the relative order of elements. The output should contain all positive numbers follow negative numbers while maintaining the same relative ordering.

Input : [9, -3, 5, -2, -8, -6, 1, 3]
Output: [-3, -2, -8, -6, 9, 5, 1, 3]

'''

class Solution:
	def merge(self,nums1,nums2,nums):
		print(nums1,nums2,nums)
		i = 0
		k = 0
		while i < len(nums1):
			if nums1[i] < 0:
				nums[k] = nums1[i]
				k += 1
			i += 1
		i = 0
		while i < len(nums2):
			if nums2[i] < 0:
				nums[k] = nums2[i]
				k += 1
			i += 1
		i = 0
		while i < len(nums1):
			if nums1[i] >= 0:
				nums[k] = nums1[i]
				k += 1
			i += 1
		i = 0
		while i < len(nums2):
			if nums2[i] >= 0:
				nums[k] = nums2[i]
				k += 1
			i += 1
		
	def mergesort(self,nums,start,end):
		if len(nums) <= 1:
			return
		mid = start + (end-start)//2
		self.mergesort(nums[start:mid],start,mid)
		self.mergesort(nums[mid:end],mid,end)
		self.merge(nums[start:mid],nums[mid:end],nums)
		
	def rearrange(self, nums: List[int]) -> None:
		self.mergesort(nums,0,len(nums))
		return nums
	

