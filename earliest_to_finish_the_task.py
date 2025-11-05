class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        best = float("inf")
        for t in tasks:
            if t[-1]+t[0] < best:
                best = t[-1]+t[0]
        return best
        
