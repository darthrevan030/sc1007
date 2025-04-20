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



if __name__ == "__main__":
    # Visible Test Case 1
    arr = [1, 2, 2, 2, 3, 4]
    result = first_occurrence(arr, 2)
    print(result)
    
    # Visible Test Case 2
    arr2 = [1, 2, 3, 4]
    result2 = first_occurrence(arr2, 5)
    print(result2)
