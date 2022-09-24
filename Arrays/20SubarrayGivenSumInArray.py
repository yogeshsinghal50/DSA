# https://www.techiedelight.com/find-subarray-having-given-sum-given-array/
# Function to print sublist having a given sum using hashing
def findSublist(nums, target):
 
    # insert (0, -1) pair into the set to handle the case when a
    # sublist with the given sum starts from index 0
    d = {0: -1}
 
    # keep track of the sum of elements so far
    sum_so_far = 0
 
    # traverse the given list
    for i in range(len(nums)):
 
        # update sum_so_far
        sum_so_far += nums[i]
 
        # if `sum_so_far - target` is seen before, we have found
        # the sublist with sum equal to `target`
        if (sum_so_far - target) in d:
            print('Sublist found', (d.get(sum_so_far - target) + 1, i))
            return
 
        # insert (current sum, current index) pair into the dictionary
        d[sum_so_far] = i
 
 
if __name__ == '__main__':
 
    # a list of integers
    nums = [0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10]
    target = 15
 
    findSublist(nums, target)
 