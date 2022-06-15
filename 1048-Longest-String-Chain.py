class Solution:
    def wordWithoutIndex(self, word: str, i: int) -> str:
        return word[:i] + word[i+1:]
    
    def condense(self,  arr: List[int]) -> List[Tuple[int]]:
        out = []
        if len(arr) > 0:
            arr.sort()
            i = j = arr[0]
            arr.append(i - 1) # added fake end to skip
            for k in arr[1:]:
                if k == j + 1:
                    j = k
                    continue
                out.append((i, j, j - i + 1))
                i = j = k
        return out
    
    def longestStrChain(self, words: List[str]) -> int:
        # break words into a map
        # map[n] = list of words with length n
        len_dict = {}
        for w in words:
            i = len(w)
            if i in len_dict:
                len_dict[i].append(w)
            else:
                len_dict[i] = [w]
        
        # word A can only be related to word B if their length differ by 1
        # break all recorded word lengths into ranges: [1,2,3,4,8,9,11,12] -> [(1,4), (8,9), (11,12)]
        ranges = self.condense(list(len_dict.keys()))
        ranges = list(filter(lambda r : r[0] < r[1], ranges))
        ranges.sort(key=lambda r : r[2], reverse=True)
        
        # minimum answer is 1
        # solve each range in order of size [DESC]
        # if the range size is <= best answer, the range can never beat it, so don't bother solving it
        best = 1
        for r in ranges:
            s, e, N = r
            if best >= N:
                break
                
            # apply bfs on individual range to get longest path
            while e >= s:
                queue = [(w, 1) for w in len_dict[e]]
                while len(queue) > 0:
                    w, d = queue.pop(0)
                    l = len(w)
                    best = max(best, d)
                    
                    # if the word's length is the range's starting length, we reached the end of the path
                    if l == s:
                        continue
                        
                    # next_repo reference acts as a <seen>
                    # word is removed when visited to avoid revisiting
                    next_repo = len_dict[l - 1]
                    for i in range(l):
                        w_2 = self.wordWithoutIndex(w, i)
                        if w_2 not in next_repo:
                            continue
                        next_repo.remove(w_2)
                        queue.append((w_2, d + 1))
                # sometimes the longest chain does not start with the longest word in range
                # we loop through whole range
                e-= 1
        
        return best
        
