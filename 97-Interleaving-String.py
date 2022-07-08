class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        N1, N2, N3 = len(s1), len(s2), len(s3)
        if N1 + N2 != N3:
            return False
        
        @cache
        def solve(i: int, j: int, k: int) -> bool:
            nonlocal s1, s2, s3, N1, N2, N3
            if k >= N3:
                return True
            c = s3[k]
            a = None if i >= N1 else s1[i]
            b = None if j >= N2 else s2[j]
            opts = []
            if a == c:
                opts.append(solve(i + 1, j, k + 1))
            if b == c:
                opts.append(solve(i, j + 1, k + 1))
            return True in opts
        return solve(0, 0, 0)
      
