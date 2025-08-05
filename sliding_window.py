#best time to buy and sell stock.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0  # If there are fewer than 2 prices, there can be no profit
        l,r = 0,0
        maxProf = 0

        while r < len(prices):
            # profitable?
            if prices[l]< prices[r]:
                profit = prices[r] - prices[l] 
                maxProf = max(profit, maxProf)
            else:
                l = r
            r+=1
        return maxProf    

#longest substring without repeating characters.
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique = set()
        l =0
        res = 0 
        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l+=1
            unique.add(s[r])
            res= max(res, r-l+1)
        return res
        
            
# longest repeating character replacement.
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        res = 0
        l = 0
        maxf=0
        #maxf need not be updated when windpw is hsifting because it does not affect the result.
        for r in range(len(s)):
            count[s[r]]= 1+ count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            #maxf replaces count.values()
            while (r-l+1)-maxf>k:
                count[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res
        
#permutation in a string.
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

# minimum window substring.
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "": return ""
#initia;ize countT
        countT, window = {}, {}
        for c in t: 
            countT[c]=1 + countT.get(c,0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l=0
        for r in range(len(s)):
            c = s[r]
            window[c]= 1+ window.get(c,0)
            #if match is found
            if c in countT and window[c] == countT[c]:
                have+=1
            while have == need:
                #update our result
                if (r-l+1 )< resLen:
                    res= [l,r]
                    resLen = r-l+1
                #pop from left
                window[s[l]]-=1
                if s[l]in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        #making sure solution exist
        return s[l:r+1] if resLen != float("infinity") else ""

#slding window maximum.
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output