'''
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. 
Implement a method to count how many possible ways the child can run up the stairs.
'''
def jump(n:int)->int:
    dp=[0]*(n+1)
    dp[0]=1
    dp[1]=1
    dp[2]=2
    for i in range(3,n+1,1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]    
    return dp[n]
print(jump(7))