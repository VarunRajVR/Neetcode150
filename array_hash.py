# contains Duplicate:

# brute force n2
# can sort and use two pointers.
# can use hashset.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        S = set()
        for i in nums:
            if i in S:
                return True
            S.add(i)
                
        return False

# Valid anagram.
#can use the get operator 

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

       # Initialize dictionaries to count character occurrences
        S, T = {}, {}

        for char in s:
            if char in S:
                S[char] += 1
            else:
                S[char] = 1
        
        for char in t:
            if char in T:
                T[char] += 1
            else:
                T[char] = 1
        
        # Compare the two dictionaries
        return S == T
    

# two sum:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [ hashmap[diff],i ]
            hashmap[n] = i

# group anagrams:
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26  # Array to count occurrences of each letter
            for c in s:
                count[ord(c) - ord('a')] += 1
            # Use the tuple of counts as the key
            res[tuple(count)].append(s)
            # this is how to handle it if the default dict is not available.
            # key = tuple(count)  # Convert the count array to a tuple to use as a key
            
            # if key not in res:
            #     res[key] = []  # Initialize the key with an empty list if not present
            # res[key].append(s)  # Append the string to the appropriate list
        
        # Return the grouped anagrams as a list of lists
        return list(res.values())

# top k frequent elements:

### we can solve using hash and sort - nlogn, hash and heapify- klogn, or the best way is bucket sort. 
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Count the frequency of each element
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Step 2: Create a bucket array where index represents frequency
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)
        
        # Step 3: Gather the top k frequent elements
        res = []
        for i in range(len(freq) - 1, 0, -1):  # Start from the highest frequency
            for n in freq[i]:
                res.append(n)
                if len(res) == k:  # Stop when we have collected k elements
                    return res

# encode and decode.
#keep it simple.
class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result += str(len(i)) + "#" + i
        return result

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i< len(s):
            j= i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res  
    

# product of array except self. 
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n =len(nums)
        res =[1]*n
        prefix = 1
        
        for i in  range(n):
            res[i]= prefix
            prefix *= nums[i]

        postfix =1
        for i in range(n-1,  -1,-1):
            res[i] =postfix * res[i]
            postfix*= nums[i]
        return res

#valid sudoku:
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                elif (board[r][c] in rows[r] or
                board [r][c] in cols[c] or 
                board[r][c] in square[(r//3,c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True
    
#longest consecutive sequence:
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0

        for num in num_set:
            # Only check for the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest
