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
# n=3
# values  = [6, 10, 12]
# weights = [1, 2, 3]
# W = 5
# # here dp array will be 2D, as 2 parameters are changing in the recursive function
# dp = [[-1 for _ in range(W+1)]for _ in range(n)] # items can be from 0 to n-1 but capacity of bag can be from 0 till max value(W),so W+1
# ans=knapsack(0,n,values,weights,W,dp)
# print("Maximum Profit : ",ans)


# Knapsack Using Tabulation(DP- Bottom -Up approach)

# def knapsack(n,values,weights,W):
#     dp=[[0 for _ in range(W+1)]for _ in range(n+1)]
#     if W==0:
#         return 0 # no capacity means we cant loot
#     # now for each item, check the best profit for diff weights
#     for i in range(1,n+1): # travel each item
#         for j in range(1,W+1): # calculate for each weight
#             # now comes 2 cases: Take item & not take item
#             take=0
#             if weights[i-1]<=j: # -1 is because the indexing is 0 based for list
#                 take=values[i-1]+dp[i-1][j-weights[i-1]]
#             not_take=dp[i-1][j]
#             dp[i][j]=max(take,not_take)
#     return dp[n][W]

# n=3
# values  = [12.5, 16, 12]
# weights = [4, 5, 3]
# W = 5
# # DP array will be 2D because we have 2 changing parameters in the recursion function
# ans=knapsack(n,values,weights,W)
# print("Max Profit : ",ans)

# ans = knapsack(n, values, weights, W)

# Binary Knapsack Using Space Optimization :
# def knapsack(n,values,weights,W):
#     # n is no of items
#     pass
# n=5
# values=[10,5,8,5,6]
# weights=[3,2,4,6,4]
# W=6 # maximum capacity of Knapsack(bag)
# ans=knapsack(n,values,weights,W)

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


# Unbounded Knapsack Using Tabulation:
def knapsack(n,values,weights,W):
    if W==0:
        return 0
    dp=[[0 for _ in range(W+1)]for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
            take=0
            if weights[i-1]<=j:
                take=values[i-1]+dp[i][j-weights[i-1]] 
                # just 1 change, instead of taking best profit from prev (row) we:
                # took same row multiple items, because each row indicate each item and each item can be reused multiple times,
                # so we are not using 1 item at a time, 1 item multiple times
            not_take=dp[i-1][j]
            dp[i][j]=max(take,not_take)
    return dp[n][W]
n=5 # no of items
values=[10,20,8,5,6]
weights=[3,1,4,6,4]
W=5 # maximum capacity of Knapsack(bag)
ans=knapsack(n,values,weights,W)
print("Maximum Profit : ",ans)



# Fractional Knapsack- Greedy approach
pass




