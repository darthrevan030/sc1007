'''
You are given a sorted list of integers (no duplicates) and a target number. Your task is to find the 
smallest number in the list that is greater than the target. 
If such a number does not exist, return -1.

Consider using the binary-search based algorithm. The brute-force algorithm will report "Time limit exceeded" 
error for some test cases. 

Time Limit: 0.05s for each input
Memory Limit: 256 MB
Source Limit: 1024 KB
'''


def find_smallest_greater(arr, x):
    #insert your codes here


if __name__ == "__main__":
    #Visible Test Case 1
    arr = [1, 2, 3, 4, 5]
    result = find_smallest_greater(arr, 9)
    print(result)
    
    # Visible Test Case 2
    arr2 = [1, 2, 4, 5, 7, 9]
    result2 = find_smallest_greater(arr2, 4)
    print(result2)