class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            curr = intervals[i]
            last = merged[-1]
            
            # Step 2: Check overlap
            if curr[0] <= last[1]:
                # Merge intervals
                last[1] = max(last[1], curr[1])
            else:
                merged.append(curr)
        
        return merged
