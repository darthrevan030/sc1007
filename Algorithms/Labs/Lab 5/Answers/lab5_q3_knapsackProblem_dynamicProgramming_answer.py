def knapsack(weights, profits, capacity):
    n = len(weights) - 1 
    dp = [[0 for _ in range(n + 1)] for _ in range(capacity + 1)]
    
    for i in range(1, capacity + 1):
        for j in range(1, n + 1):
            if weights[j] <= i:  
                dp[i][j] = max(dp[i][j-1], dp[i - weights[j]][j-1] + profits[j])
            else:
                dp[i][j] = dp[i][j-1]
                
    return dp[capacity][n]


num = int(input("Enter number of objects: "))
weights = [0] * (num + 1)  
profits = [0] * (num + 1) 

for i in range(1, num + 1):  
    weights[i] = int(input(f"Enter weight of object {i}: "))
    profits[i] = int(input(f"Enter profit of object {i}: "))

capacity = int(input("Enter total capacity of knapsack: "))

print("Maximum profit is:", knapsack(weights, profits, capacity))