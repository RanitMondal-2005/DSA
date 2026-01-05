#  TYPE 1 : Binary(0/1) Knapsack
# One item can be selected only Once

# Method 1: Solution Using DP(recursion)

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

# Method 2 : Solution DP ( Memoization [ Top - Down] )

def knapsack(i,n,values,weights,W,dp):
    # base case
    if i==n:
        return 0 # all items visited
    if dp[i][W]!=-1:# already calculated value
        return dp[i][W]
    take=0
    if weights[i]<=W:
        take=values[i]+knapsack(i+1,n,values,weights,W-weights[i],dp)
    not_take=knapsack(i+1,n,values,weights,W,dp)
    dp[i][W]=max(take,not_take)
    return dp[i][W]
n=3
values  = [6, 10, 12]
weights = [1, 2, 3]
W = 5
# here dp array will be 2D, as 2 parameters are changing in the recursive function
dp = [[-1 for _ in range(W+1)]for _ in range(n)] # items can be from 0 to n-1 but capacity of bag can be from 0 till max value(W),so W+1
ans=knapsack(0,n,values,weights,W,dp)
print("Maximum Profit : ",ans)


# Method 3 : Solution  Using Tabulation(Bottom - Up approach)

def knapsack(n,values,weights,W):
    dp=[[0 for _ in range(W+1)]for _ in range(n+1)]
    if W==0:
        return 0 # no capacity means we cant loot
    # now for each item, check the best profit for diff weights
    for i in range(1,n+1): # travel each item
        for j in range(1,W+1): # calculate for each weight
            # now comes 2 cases: Take item & not take item
            take=0
            if weights[i-1]<=j: # -1 is because the indexing is 0 based for list
                take=values[i-1]+dp[i-1][j-weights[i-1]]
            not_take=dp[i-1][j]
            dp[i][j]=max(take,not_take)
    return dp[n][W]

n=3
values  = [12.5, 16, 12]
weights = [4, 5, 3]
W = 5
# DP array will be 2D because we have 2 changing parameters in the recursion function
ans=knapsack(n,values,weights,W)
print("Max Profit : ",ans)
ans = knapsack(n, values, weights, W)


# Method 4 : Solution Using Space Optimization :
def knapsack(n,values,weights,W):
    if W==0 or n==0: # bag has no capacity or no items at house
        return 0 
    # Pattern to Notice From Tabulation-> Space Optimization :
    # we actually only need the values from previous row,,so just store that prev array
    # in that prev array we will simply store only the : Best profit for item i that has remaining capacity W 
    dp=[0]*(W+1)
    for i in range(n): # each item
        for j in range(W,weights[i]-1,-1):
            # we need to Loop in Backward, because:
            # if we move in forward we would reuse the same items multiple times-> that would make it unbounded knapsack
            #NOTE: You could have looped from W to 0,but then u need to handle the if weights[i]<=W , i.e, Take case individually using a if condition
            take=values[i]+dp[j-weights[i]]
            not_take=dp[j]
            dp[j]=max(take,not_take)
    return dp[W]
n=5
values=[10,5,8,5,6]
weights=[3,2,4,6,4]
W=6 # maximum capacity of Knapsack(bag)
ans=knapsack(n,values,weights,W)
# print("MAx Profit :",ans)



# TYPE 2: Unbounded Knapsack 
# Once item can be selected Multiple times

#  Method 1 : Recursive Solution 

n=5 # n is total no of items( from 0 to n-1)
def knapsack(i,n,values,weights,W):
    if i==n:
        return 0
    take=0
    if weights[i]<=W:
        take=values[i]+knapsack(i,n,values,weights,W-weights[i])
    not_take=knapsack(i+1,n,values,weights,W)
    return max(take,not_take)
values=[10,5,8,5,6]
weights=[3,2,4,6,4]
W=6 # maximum capacity of Knapsack(bag)
ans=knapsack(0,n,values,weights,W)
print("Maximum Profit : ",ans)


# Method 2 : Solution Using Tabulation:
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
                # took same row multiple times, because each row indicate each item and each item can be reused multiple times,
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


# Method 3 : Solution Using Space Optimization
def knapsack(n,values,weights,W):
    if W==0 or n==0: # bag has no capacity or no items at house
        return 0 
    dp=[0]*(W+1)
    for i in range(n): # each item
        for j in range(weights[i],W+1):
            # we need to Loop in forward, because: we need to reuse same value many times
            #NOTE: You could have looped from 0 to W,but then u need to handle the if weights[i]<=W , i.e, Take case individually using a if condition
            take=values[i]+dp[j-weights[i]]
            take=values[i]+dp[j-weights[i]]
            not_take=dp[j]
            dp[j]=max(take,not_take)
    return dp[W] # dont write dp[n] because the index represents capacity not no of items
n=5
values=[10,5,8,5,6]
weights=[3,2,4,6,4]
W=6 # maximum capacity of Knapsack(bag)
ans=knapsack(n,values,weights,W)
print("MAx Profit :",ans)


# TYPE 3 : Fractional Knapsack- Greedy approach
# We can choose fractions of each item !!! 
# Problem : Geeks For Geeks Fractional Knapsack
def fractionalKnapsack(values, weights, W):
    ratio=[]
    n=len(values) # n is no of items
    for i in range(n):
        # Step 1 : for each item calculate it's value to weight ratio
        # Store in this form: [(ratio,value,weight)]
        ratio.append((values[i]/weights[i],values[i],weights[i]))
    # step 2 : sort the ratio in decreasing order i.e highest value of ratio first
    # ratio is at 1st index of tuple so no issues in sorting,,
    ratio.sort(reverse=True)
    total_value=0
    # Step 3 : Select items based on the ration till u have capacity left
    for r,val,wt in ratio:
        if wt<=W: # take full item if weight allows
            total_value+=val
            W-=wt # that capacity reduced
        else : # take the fraction of the item if the item dont fits completely
            total_value+=r*W # since ; value per unit weight
            break
    return round(total_value,6) # value rounded to 6 decimal places
n=3
values=[100,280,120]
weights=[10,40,20]
W=50
print("Max profit : ",fractionalKnapsack(values, weights, W))



