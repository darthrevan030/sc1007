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
    #insert your codes here
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            count += 1
            if count == k:
                return matrix[i][j]
                
            
if __name__ == "__main__":
    matrix = [
            [1, 5, 9],
            [10, 11, 13],
            [12, 13, 15]
            ]
    result = kth_smallest(matrix, 5)
    print(result)