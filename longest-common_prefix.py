class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans =""
        x = sorted(strs)
        first= x[0]
        last = x[-1]
        m = min(len(first), len(last))
        for i in range(m):
            if first[i]!=last[i]:
                return ans
            ans+= first[i]
        return ans
        
