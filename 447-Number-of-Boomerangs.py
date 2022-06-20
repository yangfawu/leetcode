class Solution:
    def dist(self, p1: List[int], p2: List[int]) -> float:
        # taking the square root is unnecessary
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        N = len(points)
        # boomerang is not possible without 3 points
        if N < 3:
            return 0
        
        # build symmetric matrix
        # dists[i][j] = dist between point i and point j
        dists = [N*[0] for _ in range(N)]
        for i in range(N):
            dists[i][i] = -1
            for j in range(i + 1, N):
                dists[i][j] = dists[j][i] = self.dist(points[i], points[j])
        
        total = 0
        # go through each row
        # any boomerang from row i is (points[i], ??, ??)
        for i, r in enumerate(dists):
            # tally all distances between points[i] and other points
            tally = {}
            for d in r:
                if d in tally:
                    tally[d]+= 1
                else:
                    tally[d] = 1
                    
            # for tallies >= 2, add the P(n, 2) to the total
            # P(n, 2) = # of ways to arrange a selection of 2 of n items
            for c in tally.values():
                if c < 2:
                    continue
                total+= factorial(c)//factorial(c - 2)
        
        return total
      
