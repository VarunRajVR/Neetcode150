#insert intervals
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(intervals)):
            if newInterval[1]< intervals[i][0]:
                res.append(newInterval)
                return res+intervals[i:]
            
            elif newInterval[0]> intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]),max(newInterval[1], intervals[i][1])]
        res.append(newInterval)
        return res

#merge intervals
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])  # Sort intervals based on the start time
        
        i = 0
        while i < len(intervals) - 1:
            # Check if the end time of the current interval is greater than the start time of the next interval
            if intervals[i][1] >= intervals[i + 1][0]:
                # Merge the intervals
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals.pop(i + 1)
            else:
                i += 1
        
        return intervals
    
#non-overlapping intervals
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key= lambda x : x[0])
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res+=1
                prevEnd = min(end, prevEnd)
        return res

#meeting rooms
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        flag = True
        if len(intervals)<2: return True
        intervals.sort()
        prevEnd = intervals[0][1]

        for start ,end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                flag = False
        return flag

#meeting rooms II
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        res, count = 0 , 0 
        s, e = 0,0
        while s< len(intervals):
            if start[s]<end[e]:
                s+=1
                count+=1 
            else:
                e+=1
                count-=1
            res= max(count, res)
        return res   

#minimum interval to include each query
class Solution(object):
    def minInterval(self, intervals, queries):
        """
        :type intervals: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1, r))
                i += 1

            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            res[q] = minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
        