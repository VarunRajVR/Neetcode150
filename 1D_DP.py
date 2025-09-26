class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        if n > 1:
            dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]
        
#min cost climbing stairs
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
        

#house robber
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1, rob2 = 0,0
        for n in nums:
            temp = max(rob1+ n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

#house robber II
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums[0], self.helper(nums[1:]),
                            self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
    
#longest palindromic subsequence
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        resLen = 0 
        for i in range(len(s)):
            # Check for odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # Check for even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res

#palindromic substrings
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = 0

        for i in range(len(s)):
            # Check for odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res+=1
                l -= 1
                r += 1

            # Check for even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res+=1
                l -= 1
                r += 1

        return res

#decode ways
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = { len(s): 1 }
        
        # Bottom-up approach
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if (i + 1 < len(s) and (s[i] == "1" or 
                (s[i] == "2" and s[i + 1] in "0123456"))):
                dp[i] += dp[i + 2]
                
        return dp[0]

        # # Top-down approach with memoization
        # dp = { len(s): 1 }
        
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     if s[i] == "0":
        #         return 0
            
        #     res = dfs(i + 1)
            
        #     if (i + 1 < len(s) and (s[i] == "1" or 
        #         (s[i] == "2" and s[i + 1] in "0123456"))):
        #         res += dfs(i + 2)
            
        #     dp[i] = res
        #     return res
        
        # return dfs(0)

#coin change 
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

#maximum product subarray
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        curmin = 1
        curmax =1
        for n in nums:
            if n ==0:
                curmin = 1
                curmax =1
                continue
            tmp = curmax * n
            curmax = max(n *curmax, n * curmin, n)
            curmin = min(tmp, n * curmin, n)
            res = max(res, curmax)
        return res
    
#word break
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

#longest increasing subsequence
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
        
#equal subset sum partition
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP

        return True if target in dp else False