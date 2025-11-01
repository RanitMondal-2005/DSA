# Binary(0/1) Knapsack
# Solution Using DP(recursion)
# def knapsack(i,n,values,weights,W):
#   if i==n:
#     return 0
#   take=0
#   if weights[i]<=W:
#     take=values[i]+knapsack(i+1,n,values,weights,W-weights[i])
#   not_take=knapsack(i+1,n,values,weights,W)
#   return max(take,not_take)
# n=5 # no of items
# values=[10,5,8,5,6]
# weights=[3,2,4,6,4]
# W=6 # maximum capacity of Knapsack(bag)
# ans=knapsack(0,n,values,weights,W)
# print("Maximum Profit : ",ans)

# Knapsack Using 
# DP (Memoization)
# def knapsack(i,n,values,weights,W,dp):
#     # base case
#     if i==n:
#         return 0 # all items visited
#     if dp[i][W]!=-1:# already calculated value
#         return dp[i][W]
#     take=0
#     if weights[i]<=W:
#         take=values[i]+knapsack(i+1,n,values,weights,W-weights[i],dp)
#     not_take=knapsack(i+1,n,values,weights,W,dp)
#     dp[i][W]=max(take,not_take)
#     return dp[i][W]
# n=5 # n is total no of items( from 0 to n-1)
# values=[10,5,8,5,6]
# weights=[3,2,4,6,4]
# W=6 # maximum capacity of Knapsack(bag)
# # here dp array will be 2D, as 2 parameters are changing in the recursive function
# dp = [[-1 for _ in range(W+1)]for _ in range(n)] # items can be from 0 to n-1 but capacity of bag can be from 0 till max value(W),so W+1
# ans=knapsack(0,n,values,weights,W,dp)
# print("Maximum Profit : ",ans)


# Knapsack Using Tabulation(DP- Bottom -Up approach)
# Knapsack Using Tabulation (DP - Bottom-Up approach)
def knapsack(n, values, weights, W):
    # Step 1: Create dp table (n+1) x (W+1)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Step 2: Fill dp table
    for i in range(1, n + 1):          # items 1..n
        for w in range(1, W + 1):      # capacity 1..W
            take = 0
            not_take = dp[i - 1][w]    # not taking the current item
            if weights[i - 1] <= w:    # if we can take it
                take = values[i - 1] + dp[i - 1][w - weights[i - 1]]
            dp[i][w] = max(take, not_take)
# i-1 is used because row i in the DP table represents using items 0 to i−1,
# so we look at previous row (i−1) for earlier items and use arrays[i−1] for the current one.
    print("Maximum Profit :", dp[n][W])
    return dp[n][W]
n = 5  # no of items
values = [10, 5, 8, 5, 6]
weights = [3, 2, 4, 6, 4]
W = 6  # maximum capacity of Knapsack(bag)

ans = knapsack(n, values, weights, W)



# Unbounded Knapsack ( Recursive Solution )
# n=5 # n is total no of items( from 0 to n-1)
# def knapsack(i,n,values,weights,W):
#     if i==n:
#         return 0
#     take=0
#     if weights[i]<=W:
#         take=values[i]+knapsack(i,n,values,weights,W-weights[i])
#     not_take=knapsack(i+1,n,values,weights,W)
#     return max(take,not_take)
# values=[10,5,8,5,6]
# weights=[3,2,4,6,4]
# W=6 # maximum capacity of Knapsack(bag)
# ans=knapsack(0,n,values,weights,W)
# print("Maximum Profit : ",ans)