#climbing stairs.
#bottom up DP: starts at the base case and fills the tabulation. 
#Can also be done using memoization. 

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two  # Update step count
            two = temp       # Move `one` to `two`
        return one

        #memoization solution is similar to fib series:
        

# coin change
#similar to bestSum problem- use it for memoization solution

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # Initialize dp array with amount + 1, which acts as "infinity"
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins to make amount 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])  # Choose the minimum coins needed

        # If dp[amount] has not been updated, return -1 (impossible case)
        return dp[amount] if dp[amount] != amount + 1 else -1
    
# longest increasing sequence:
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1]*len(nums)
        for i in range(len(nums)-1, -1,-1):
            for j in range (i+1, len(nums)):
                if nums[i]< nums[j]:
                    dp[i]= max(dp[i], 1+ dp[j])
        return max(dp)
#LCS
#can be solved using recursion and memoization too
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        # Initialize dp table with (m+1) x (n+1) dimensions
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

#word break:

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s)) and (s[i : i + len(w)] == w):
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]