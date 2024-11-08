class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        i=0
        n=len(intervals)
        results=[]
        while i<n and intervals[i][1]<newInterval[0]:
            results.append(intervals[i])
            i+=1
        while i<n and intervals[i][0]<=newInterval[1]:
            newInterval[0]=min(intervals[i][0],newInterval[0])
            newInterval[1]=max(intervals[i][1],newInterval[1])
            i+=1
        results.append(newInterval)
        while i<n:
            results.append(intervals[i])
            i+=1
        return results
            
        