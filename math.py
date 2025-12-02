#rotate image
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft

            r -= 1
            l += 1

#spiral matrix
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        left = 0
        top = 0
        right = len(matrix[0])
        bottom = len(matrix)
        
        while left<right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])       
            top+=1

            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right-=1

            if not (left<right and top <bottom): break

            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -=1

            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left+=1
        return res
    
#set matrix zeroes
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        R = len(matrix)
        C = len(matrix[0])
        for i in range(R):
            # Since first cell for both first row and first column is the same i.e. matrix[0][0]
            # We can use an additional variable for either the first row/column.
            # For this solution we are using an additional variable for the first column
            # and using matrix[0][0] for the first row.
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, C):
                # If an element is zero, we set the first element of the corresponding row and column to 0
                if matrix[i][j]  == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Iterate over the array once again and using the first row and first column, update the elements.
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well        
        if is_col:
            for i in range(R):
                matrix[i][0] = 0
        
#happy number
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=set()
        while n!=1:
            n=sum(int(i) ** 2 for i in str(n))
            if n in s:
                return False
            else:
                s.add(n)
        else:
            return True
        

#plus one
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        mul =1 
        sum =0
        for i in reversed(digits):
            sum += i*mul
            mul *= 10
        sum +=1
        dig = str(sum)
        lst =[]
        for i in dig:
            lst.append(int(i))
        return lst
        
#pow(x, n)
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def help(x, n):
            if x==0:
                return 0
            if n ==0:
                return 1
            if n== 1:
                return x
            res = help(x, n//2)
            res*=res

            return res if n%2==0 else x*res


        res = help(x, abs(n))
        return res if n>=0 else 1/res
        
#multiply strings:
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
        res = map(str, res[beg:])
        return "".join(res)
    
#detect squares
class DetectSquares(object):

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point):
        """
        :type point: List[int]
        :rtype: None
        """
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point):
        """
        :type point: List[int]
        :rtype: int
        """
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)