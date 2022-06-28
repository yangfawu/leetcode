class Heap:
    def __init__(self):
        self.arr = []
        
    def __bin_pos(self, target: int) -> int:
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
        self.arr.insert(self.__bin_pos(val), val)
        
    def size(self) -> int:
        return len(self.arr)
    
    def is_empty(self) -> bool:
        return self.size() < 1
    
    def _access(self, idx: int) -> int:
        if self.is_empty():
            return None
        return self.arr[idx]
    
    def _pop(self, idx: int) -> int:
        if self.is_empty():
            return None
        return self.arr.pop(idx)
    
    def min(self) -> int:
        return self._access(0)
    
    def max(self) -> int:
        return self._access(-1)
    
    def pop_min(self) -> int:
        return self._pop(0)
    
    def pop_max(self) -> int:
        return self.pop(-1)
    
