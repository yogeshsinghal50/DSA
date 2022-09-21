'''
https://www.techiedelight.com/find-k-closest-elements-to-given-value-array/
Given a sorted integer array `nums` and two positive integers `k` and `target`, find the `k` closest elements to `target` in the array. Here, `target` may or may not be present in the input array. The solution should return elements in the same order as present in the input array.

Input : nums[] = [10, 12, 15, 17, 18, 20, 25], k = 4, target = 16
Output: [12, 15, 17, 18]


• If `target` is less than or equal to the first element in the input array, the solution should return the first `k` elements.

Input : nums[] = [2, 3, 4, 5, 6, 7], k = 3, target = 1
Output: [2, 3, 4]


• If `target` is more than or equal to the last element in the input array, the solution should return the last `k` elements.

Input : nums[] = [2, 3, 4, 5, 6, 7], k = 2, target = 8
Output: [6, 7]


• In case multiple sets of `k` closest elements exists, the solution should return the first occuring set.

Input : nums[] = [10, 12, 15, 17, 20, 25], k = 3, target = 16
Output: [12, 15, 17]
Explanation: There are two k-closest element sets present in the array i.e., [12, 15, 17] and [15, 17, 20]. The solution returns set [12, 15, 17] as it appears before set [15, 17, 20] in the array.

'''

class Solution:
	def kClosestElements(self, nums: List[int], k: int, target: int) -> List[int]:
		left = 0 
		right = len(nums) - 1  
		while right - left >= k:
			if abs(target - nums[left]) > abs(nums[right] - target):
				left += 1 
			else:
				right -= 1 
		return nums[left:left+k]

