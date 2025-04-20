'''
Given an n by n matrix (2D array) where each row and column is sorted in non-decreasing order, find the k-th smallest element. 

For example, given the 3 by 3 matrix: 

            1  5  9
            10 11 13
            12 13 15

The 5th smallest number is 11. The 7th and 8th smallest numbers are both 13.  

Time Limit: 0.05s for each input
Memory Limit: 256 MB
Source Limit: 1024 KB
'''
import heapq

def kth_smallest(matrix, k):
    #insert your codes here
    n = len(matrix)
    min_heap = []
    
    # Add the first element of each row to the heap
    for i in range(min(n, k)):
        # (value, row, column)
        heapq.heappush(min_heap, (matrix[i][0], i, 0))
    
    # Pop from heap k-1 times
    for _ in range(k - 1):
        val, row, col = heapq.heappop(min_heap)
        if col + 1 < n:
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
    
    # The kth element is at the top of the heap
    return heapq.heappop(min_heap)[0]
                
            
if __name__ == "__main__":
    matrix = [
            [1, 5, 9],
            [10, 11, 13],
            [12, 13, 15]
            ]
    result = kth_smallest(matrix, 5)
    print(result)