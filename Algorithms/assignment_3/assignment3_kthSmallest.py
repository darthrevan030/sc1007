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
def kth_smallest(matrix, k):
    n = len(matrix)
    
    # Define helper function to count elements less than or equal to mid
    def count_less_equal(mid):
        count = 0
        for row in range(n):
            # For each row, count elements <= mid
            col = 0
            while col < n and matrix[row][col] <= mid:
                col += 1
            count += col
        return count
    
    # Binary search for the kth smallest element
    low = matrix[0][0]
    high = matrix[n-1][n-1]
    
    while low < high:
        mid = low + (high - low) // 2
        if count_less_equal(mid) < k:
            low = mid + 1
        else:
            high = mid
    
    return low
                
            
if __name__ == "__main__":
    matrix = [
            [1, 5, 9],
            [10, 11, 13],
            [12, 13, 15]
            ]
    result = kth_smallest(matrix, 5)
    print(result)