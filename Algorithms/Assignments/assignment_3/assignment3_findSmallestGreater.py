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
    n = len(arr)

    if n == 0:
        return -1 
    
    if n < 2:
        if arr[0] > x:
            result = arr[0]
            return result

    left = 0
    right = n - 1

    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            left = mid + 1
            right = n - 1
        elif arr[mid] > x:
            result = arr[mid]
            right = mid - 1
        else:
            left = mid + 1
    
    return result



if __name__ == "__main__":
    #Visible Test Case 1
    arr = [1, 2, 3, 4, 5]
    result = find_smallest_greater(arr, 9)
    print(result)
    
    # Visible Test Case 2
    arr2 = [1, 2, 4, 5, 7, 9]
    result2 = find_smallest_greater(arr2, 4)
    print(result2)

    # Additional Test Case for sanity check
    arr2 = [2]
    result2 = find_smallest_greater(arr2, 1)
    print(result2)