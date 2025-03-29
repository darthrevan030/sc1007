'''
First occurrence in a sorted array:
You are given a sorted array of integers (possibly with duplicates). Write a function to find the index
of the first occurrence of a given target number. If the target is not present, return -1.
Consider using binary search based algorithm as brute force algorithm will report "Time Limit exceeded" 
for some test cases. 

Time Limit: 0.05s for each input
Memory Limit: 256 MB
Source Limit: 1024 KB
'''

def first_occurrence(arr, target):
    #insert your codes
    n = len(arr)
    
    i = 0
    j = n - 1

    while i <= j:
        k = (i + j) // 2
        if target <= arr[k]:
            j = k - 1
        if arr[k] <= target:
            i = k + 1
    
    if arr[k] == target:
        return k
    else:
        return -1
    


if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 4]
    result = first_occurrence(arr, 2)
    print(result)