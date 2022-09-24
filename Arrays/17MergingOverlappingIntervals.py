'''
https://www.techiedelight.com/merging-overlapping-intervals/
Given a collection of intervals, return all non-overlapping intervals after merging the overlapping intervals.

Input : [(1, 5), (2, 3), (4, 6), (7, 8), (8, 10), (12, 15)]
Output: {(1, 6), (7, 10), (12, 15)}

'''

class Solution:
	def mergeIntervals(self, intervals: List[Tuple[int]]) -> Set[Tuple[int]]:
		intervals.sort(key=lambda x: x[0])
		stack = []
		for interval in intervals:
			if not stack or interval[0] > stack[-1][1]:
				stack.append(interval)
			if interval[0] <= stack[-1][1] and interval[1] > stack[-1][1]:
				s = stack.pop()
				start,begin = s[0], interval[1]
				stack.append((start,begin))
		return set(stack)

