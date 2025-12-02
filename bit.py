#reverse integer
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MIN = -2**31     # -2147483648
        MAX = 2**31 - 1  # 2147483647

        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10

            # Check overflow
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0

            res = res * 10 + digit

        return sign * res

#single number
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
        
#number of 1 bits
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res +=n %2
            n = n >>1
        return res
        
#counting bits
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        dp = [0]*(n+1)
        offset = 1
        for i in range (1, n+1):
            if offset * 2 == i:
                offset = i 
            dp[i] = 1+ dp [i - offset]
        return dp 

#reverse bits
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res =0 
        for i in range(32):
            bit = (n>>i)%2
            res = res | (bit << 31-i)
        return res
        
#missing number
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)
        for i in range(len(nums)):
            res += (i- nums[i])
        return res
    
# sum of two integers
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while b!=0:
            tmp = a&b <<1
            a = a ^ b
            b = tmp
        return a