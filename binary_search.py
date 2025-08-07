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
        flag = False
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                flag = True
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