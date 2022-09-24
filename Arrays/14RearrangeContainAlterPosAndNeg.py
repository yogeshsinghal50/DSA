# Partitioning routine of Quicksort
# https://www.techiedelight.com/rearrange-array-positive-negative-numbers-alternate-positions/
def partition(A):

	j = 0
	pivot = 0   	# consider 0 as a pivot

	# each time we find a negative number, `j` is incremented,
	# and a negative element would be placed before the pivot
	for i in range(len(A)):
		if A[i] < pivot:
			# swap `A[i]` with `A[j]`
			temp = A[i]
			A[i] = A[j]
			A[j] = temp

			j = j + 1
	print(A)
	# `j` holds the index of the first positive element
	return j


# Function to rearrange a given list such that it contains positive
# and negative numbers at alternate positions
def rearrange(A):

	# partition a given list such that all positive elements move
	# to the end of the list

	p = partition(A)

	# swap alternate negative elements from the next available positive
	# element till the end of the list is reached or all negative or
	# positive elements are exhausted.

	n = 0
	while len(A) > p > n:
		# swap `A[n]` with `A[p]`
		temp = A[n]
		A[n] = A[p]
		A[p] = temp

		p = p + 1
		n = n + 2


if __name__ == '__main__':

	A = [-3,-2,-7,-10,5, -2, 9, -6, 1, -8, 3, -3,-2,-7,-10]

	rearrange(A)
	print(A)		# print the rearranged list
