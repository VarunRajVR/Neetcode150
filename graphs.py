#number of connected components in an undirected graph
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        # Initialize the adjacency list for all nodes
        graph = {i: [] for i in range(n)}
        
        # Build the graph
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        visited=set()
        count = 0

        #for no of comp
        def explore(graph, node, visited):
            if node in visited: return False
            visited.add(node)
            for i in graph[node]:
                explore(graph, i, visited)
            return True 

        for i in graph:
            if explore(graph, i, visited) == True:
                count+=1
        return count


#number of islands
class Solution(object):
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            # out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            # water or already visited
            if grid[r][c] == '0' or (r, c) in visited:
                return

            visited.add((r, c))
            # 4-dir flood fill
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)     # mark entire island
                    count += 1    # count this island once
        return count
        
#max area of island
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            # out of bounds or water or visited
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))
            # area of this cell + 4-neighbour areas
            return (1
                    + dfs(r - 1, c)
                    + dfs(r + 1, c)
                    + dfs(r, c - 1)
                    + dfs(r, c + 1))

        largest = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    largest = max(largest, dfs(i, j))

        return largest
    
#clone graph

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldtonew = {}

        def dfs (node):
            if node in oldtonew:
                return oldtonew[node]
            copy = Node(node.val)
            oldtonew[node]= copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None
from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        Modify rooms in-place.
        rooms[r][c] is:
          -1 : wall
           0 : gate
        INF : empty room (2**31 - 1); fill with min distance to a gate
        """
        if not rooms or not rooms[0]:
            return

        ROWS, COLS = len(rooms), len(rooms[0])
        q = deque()
        visit = set()

        # push a room into the BFS queue if it's valid to visit
        def addRoom(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                (r, c) in visit or rooms[r][c] == -1):
                return
            visit.add((r, c))
            q.append((r, c))

        # multi-source BFS: start from every gate (0)
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):         # process one BFS "level"
                r, c = q.popleft()
                rooms[r][c] = dist          # distance from the nearest gate
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1

#pacific atlantic water flow
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c, visit, prevheight):
            if (r,c) in visit or r<0 or c<0 or r== rows or c== cols or heights[r][c]< prevheight:
                return
            visit.add((r,c))
            dfs(r+1,c, visit, heights[r][c])
            dfs(r-1,c, visit, heights[r][c])
            dfs(r,c+1, visit, heights[r][c])
            dfs(r,c-1, visit, heights[r][c])

        for c in range(cols):
            dfs(0,c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        for r in range(rows):
            dfs(r,0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][c])
        res=[]
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res

#rotting oranges
from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])

        # Step 1: count fresh oranges and enqueue all rotten ones
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Step 2: BFS starting from all rotten oranges at once
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    # check bounds and if it's a fresh orange
                    if (row < 0 or row == ROWS or col < 0 or col == COLS 
                        or grid[row][col] != 1):
                        continue

                    # make this orange rotten
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1

            time += 1

        # Step 3: return minutes if all oranges are rotten, else -1
        return time if fresh == 0 else -1

#word ladder
import collections
from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        
        # Build neighbor map
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        visit = set([beginWord])
        q = deque([beginWord])
        res = 1

        # BFS
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1

        return 0

#redundant connection
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            
#graph valid tree
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n == 0:
            return True  # An empty graph is a valid tree (as it's trivially acyclic and connected).

        # If there are more edges than n-1, it cannot be a tree
        if len(edges) != n - 1:
            return False

        # Initialize adjacency list
        adj = {i: [] for i in range(n)}

        # Build the adjacency list
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == parent:  # Skip the edge leading back to the parent node
                    continue
                if neighbor in visited:  # If we revisit a node, there's a cycle
                    return False
                if not dfs(neighbor, node):  # Recursively visit all neighbors
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
    
#surrounded regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == ROWS or
                c == COLS or board[r][c] != "O"
            ):
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
                
#course schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Map each course to its prerequisites
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Store all courses along the current DFS path
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

#course schedule II:
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output
