class Heap:
    def __init__(self):
        self.arr = []
        
    def _bin_pos(self, target: int) -> int:
        left, right = 0, len(self.arr) - 1
        while left <= right:
            mid = (left + right) >> 1
            val = self.arr[mid]
            if val < target:
                left = mid + 1
                continue
            if val > target:
                right = mid - 1
                continue
            return mid
        return left
    
    def add(self, val: int):
        self.arr.insert(self._bin_pos(val), val)
    
    def is_empty(self) -> bool:
        return len(self.arr) < 1
    
    def max(self) -> int:
        return self.arr[-1]
    
    def pop_max(self) -> int:
        return self.arr.pop(-1)
            
class Solution:
    def minDeletions(self, s: str) -> int:
        # tally maps letter -> # of them
        tally = {}
        for c in s:
            if c in tally:
                tally[c]+= 1
            else:
                tally[c] = 1
        
        # count maps freq -> # of them
        count = {}
        # priority queue of lowest to highesst freq
        pq = Heap()
        for v in tally.values():
            if v in count:
                count[v]+= 1
            else:
                pq.add(v)
                count[v] = 1
        
        # decrement your way down from highest to lowest freq
        total = 0
        while not pq.is_empty():
            # get biggest frequency and its count
            f = pq.pop_max()
            c = count[f]
            
            if c < 2:
                # if count is not >= 2, there is no conflict
                continue
            
            # new_f -> new frequency of decremented letters
            # new_c -> # of letters decremented
            new_f, new_c = f - 1, c - 1
            total+= new_c
            
            if new_f < 1:
                # if the new frequency is 0 or less, there is no conflict
                continue
            
            # else add to count map
            if new_f in count:
                count[new_f]+= new_c
                # by default, if new_f is already in count map
                # then we don't have to add it to PQ because
                # it has yet to been seen
            else:
                count[new_f] = new_c
                pq.add(new_f)
        
        return total
