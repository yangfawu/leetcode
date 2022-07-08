class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # map # -> chain it belong to
        heads = {}
        tails = {}
        seen = {}
        for d in nums:
            if d in seen:
                continue
            seen[d] = True
            head_check = d + 1 in heads
            tail_check = d - 1 in tails
            if head_check and tail_check:
                # if left and right chain exist, fuse them
                h, t = tails[d - 1][0], heads[d + 1][1]
                heads.pop(d + 1, None)
                tails.pop(d - 1, None)
                tails[t] = heads[h]
                heads[h][1] = t
                tails[t][0] = h
            elif head_check:
                h, t = heads[d + 1]
                heads.pop(h, None)
                heads[d] = tails[t]
                heads[d][0] = d
            elif tail_check:
                h, t = tails[d - 1]
                tails.pop(t, None)
                tails[d] = heads[h]
                tails[d][1] = d
            else:
                heads[d] = tails[d] = [d, d]
        
        best = 0
        for h, t in heads.values():
            best = max(best, t - h + 1)
        
        return best
      
