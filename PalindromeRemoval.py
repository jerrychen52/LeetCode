'''
Given an integer array arr, in one move you can select a palindromic subarray arr[i], arr[i+1], ..., arr[j] where i <= j, and remove that subarray from the given array. 
 Note that after removing a subarray, the elements on the left and on the right of that subarray move to fill the gap left by the removal.
Return the minimum number of moves needed to remove all numbers from the array.
Example 1:

Input: arr = [1,2]
Output: 2

Example 2:

Input: arr = [1,3,4,1,5]
Output: 3
Explanation: Remove [4] then remove [1,3,1] then remove [5].

Constraints:

    1 <= arr.length <= 100
    1 <= arr[i] <= 20

Let use dp[i][j] represents the minimum number of moves needed to remove all the numbers from the array from i to j inclusive. Then,

(1) dp[i][j] = 1 + dp[i+1][j] //since it can ways be done by removing one by one;

(2) if(dp[i] == dp[i+1]), dp[i][j] = min(dp[i][j], 1 + dp[i+2][j]);

(3) if(dp[i] == dp[j]),  dp[i][j] = min(dp[i][j], dp[i+1][j-1])//both ends can be removed along with previous palindromes;

(4) if(dp[i] == dp[k]) dp[i][j] = min(dp[i][j], dp[i][k-1] + dp[k+1][j])  for k = i + 2, to j - 1;
'''
from typing import List

def palindromeRemoval(arr:List[int])->int:
    n = len(arr)
    dp = []
    for i in range(n):
        dp.append([n]*n)
    
    for l in range(1,n+1,1):
        for i in range(n):
            for j in range(i+l-1,n,1):
                if (i == j):
                    dp[i][j] = 1
                    continue
                dp[i][j] = 1+dp[i+1][j] # can always delete current element
                if (arr[i] == arr[i+1]):
                    dp[i][j] = min(dp[i][j],1+dp[i+2][j])
                if (arr[i] == arr[j] and j>i+1):
                    dp[i][j] = min(dp[i][j], dp[i+1][j-1]) # 
                for k in range(i+2,j,1):
                    if (arr[i] == arr[k]):
                        dp[i][j] = min(dp[i][j], dp[i+1][k-1]+dp[k+1][j])
    
    return dp[0][n-1]

if __name__ == '__main__':
    inputs= [[1,2],[1,3,4,1,5]]
    results=[2,3]
    for i in range(len(inputs)):
        input = inputs[i]
        numRemoval=palindromeRemoval(input)
        print("input={} result={} expect={} match={}".format(input,numRemoval,results[i],numRemoval==results[i]))

