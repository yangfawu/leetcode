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
    
    def pop_max(self) -> int:
        return self.arr.pop(-1)

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # map height => PQ of k
        tally = {}
        
        # pq for unique height
        heights = Heap()
        
        
        for h, k in people:
            if h not in tally:
                tally[h] = Heap()
                heights.add(h)
            tally[h].add(k)
        
        # approach:
        # [max_height, k] should always be inserted first
        # because nothing would be greater in height than them
        
        # we then move onto the next greatest height
        # k determines the insertion index
        # when we insert at k, we are always sure that there are k elements before it
        
        # in the future, this k criteria remains satisfied
        out = []
        while not heights.is_empty():
            h = heights.pop_max()
            for k in tally[h].arr:
                out.insert(k, [h, k])
        
        return out
        
