#network time delay
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1
    
#reconstruct itinerary
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # adj = {src: [] for src, dst in tickets}
        # tickets.sort()
        # for src, dst in tickets:
        #     adj[src].append(dst)

        # res = ["JFK"]
        # def dfs(src):
        #     if len(res) == len(tickets) + 1:
        #         return True
        #     if src not in adj:
        #         return False

        #     temp = list(adj[src])
        #     for i, v in enumerate(temp):
        #         adj[src].pop(i)
        #         res.append(v)
        #         if dfs(v): return True
        #         adj[src].insert(i, v)
        #         res.pop()
        #     return False

        # dfs("JFK")
        # return res
        adj = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        res = []
        def dfs(src):
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]
    
#minimum cost to connect all points


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        N = len(points)
        adj = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        res = 0
        visit = set()
        minH = [[0, 0]]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])
        return res

#swim in rising water
class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or
                    neiR == N or neiC == N or
                    (neiR, neiC) in visit
                ):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
            
#alien dictionary
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Create a graph (adjacency list)
        adj = {c: set() for w in words for c in w}

        # Build the graph by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # If the prefix of the longer word is the same as the shorter word, and the longer word comes first, it's invalid
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            # Find the first differing character and establish an ordering
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # Dictionary to track visited nodes (True = visiting, False = visited)
        visit = {}
        res = []

        # DFS function to detect cycles and build the result
        def dfs(c):
            if c in visit:
                return visit[c]  # If already visited, return whether it's in the current path (cycle)

            visit[c] = True  # Mark as visiting
            for nei in adj[c]:
                if dfs(nei):  # If a cycle is found in any neighbor
                    return True

            visit[c] = False  # Mark as visited
            res.append(c)  # Add to result in post-order

        # Perform DFS for each character
        for c in adj:
            if dfs(c):
                return ""  # If a cycle is detected, return an empty string

        res.reverse()  # Reverse the result to get the correct order
        return "".join(res)
#cheapest flights within k stops
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        from collections import defaultdict
        import heapq

        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # Min-heap: (cost, current_node, stops)
        heap = [(0, src, 0)]
        # visited[node] = minimum stops used to reach node
        visited = dict()

        while heap:
            cost, node, stops = heapq.heappop(heap)

            # If destination is reached
            if node == dst:
                return cost

            # If we've already visited with fewer or same stops, skip
            if node in visited and visited[node] <= stops:
                continue

            visited[node] = stops

            if stops <= k:
                for neighbor, price in graph[node]:
                    heapq.heappush(heap, (cost + price, neighbor, stops + 1))

        return -1