class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n-1

        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return -1

#serach a 2-d matrix
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        #find the row
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        #binary search the column
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
        
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
    
#find minimum in rotated sorted array
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = (l + r) // 2
            
            if nums[m] < nums[r]:
                # The minimum is in the left half
                r = m
            else:
                # The minimum is in the right half including the middle
                l = m+1
        
        return nums[l]

#search in rotated sorted array
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # Left half is sorted
            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    # Target is in the right half
                    l = mid + 1
                else:
                    # Target is in the left half
                    r = mid - 1
            else:
                # Right half is sorted
                if target > nums[r] or target < nums[mid]  :
                    # Target is in the left half
                    r = mid - 1
                else:
                    # Target is in the right half
                    l = mid + 1

        return -1

class TimeMap(object):

    def __init__(self):
        self.store= {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.store:
            self.store[key]= []
        self.store[key].append((value, timestamp))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        res = ""
        values = self.store.get(key, [])
        l, r= 0, len(values)-1
        while l<=r:
            mid = (l+r)//2
            if values[mid][1] <=timestamp:
                res = values[mid][0]
                l = mid+1
            else:
                r =mid-1
        return res






# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
       # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m
        while left <= right:
            i = (left + right) // 2  # partition in nums1
            j = half - i             # partition in nums2

            # nums1 left and right values
            left1 = nums1[i-1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")

            # nums2 left and right values
            left2 = nums2[j-1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            # valid partition
            if left1 <= right2 and left2 <= right1:
                # odd total length
                if total % 2:
                    return float(min(right1, right2))
                # even total length
                return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1