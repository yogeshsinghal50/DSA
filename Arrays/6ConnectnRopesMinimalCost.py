# https://www.techiedelight.com/connect-n-ropes-with-minimal-cost/


import heapq
from heapq import heappush, heappop
 
 
# Function to calculate the minimum cost to join `n` ropes into a single rope
def findMinCost(prices):
 
    # In-place transform list `prices` into a min-heap in linear time
    heapq.heapify(prices)
 
    # keep track of the minimum cost so far
    cost = 0
 
    # repeat till heap size is reduced to one
    while len(prices) > 1:
 
        # Extract the top two elements from the min-heap
        x = heappop(prices)
        y = heappop(prices)
 
        # calculate the cost of the extracted values
        total = x + y
 
        # insert the cost back to the min-heap
        heappush(prices, total)
 
        # update the minimum cost
        cost += total
 
    return cost
 
 
if __name__ == '__main__':
 
    prices = [5, 4, 2, 8]
    print('The minimum cost is', findMinCost(prices))