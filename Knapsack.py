# Binary(0/1) Knapsack
# Solution Using DP(recursion)
def knapsack(i,n,values,weights,W):
  if i==n:
    return 0
  take=0
  if weights[i]<=W:
    take=values[i]+knapsack(i+1,n,values,weights,W-weights[i])
  not_take=knapsack(i+1,n,values,weights,W)
  return max(take,not_take)
n=5 # no of items
values=[10,5,8,5,6]
weights=[3,2,4,6,4]
W=6 # maximum capacity of Knapsack(bag)
ans=knapsack(0,n,values,weights,W)
print("Maximum Profit : ",ans)