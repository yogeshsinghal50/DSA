'''
https://www.techiedelight.com/find-maximum-sum-path-involving-elements-given-arrays/
Given two sorted arrays of integers, find a maximum sum path involving elements of both arrays whose sum is maximum. You can start from either array, but can switch between arrays only through its common elements.

Input:

X = [3, 6, 7, 8, 10, 12, 15, 18, 100]
Y = [1, 2, 3, 5, 7, 9, 10, 11, 15, 16, 18, 25, 50]

Output: The maximum sum is 199

Explanation: The maximum sum path is 1 —> 2 —> 3 —> 6 —> 7 —> 9 —> 10 —> 12 —> 15 —> 16 —> 18 —> 100

'''

class Solution:
	def findMaxPathSum(self, X: List[int], Y: List[int]) -> int:
		i = 0 
		j = 0
		sum_X = sum_Y = sum_final = 0
		while i < len(X) and j < len(Y):
			if X[i] < Y[j]:
				sum_X += X[i]
				i += 1
			elif X[i] > Y[j]:
				sum_Y += Y[j]
				j += 1
			else:
				sum_final += max(sum_Y,sum_X) + X[i]
				i += 1 
				j += 1
				sum_X = sum_Y = 0
		while i < len(X):
			sum_X += X[i]
			i += 1
		while j < len(Y):
			sum_Y += Y[j]
			j += 1
		sum_final += max(sum_Y,sum_X)
		return sum_final
					
