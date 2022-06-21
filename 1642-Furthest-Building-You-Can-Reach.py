class Ledger:
    def __init__(self):
        self.tally = {}
        self.size = 0
        self.vals = []
        
    def get_min(self) -> int:
        if self.size < 1:
            return None
        return self.vals[0]
        
    def _insert_position(self, target: int) -> int:
        # binary search for ASC position
        left, right = 0, len(self.vals) - 1
        while left <= right:
            mid = (left + right) >> 1
            val = self.vals[mid]
            if target < val:
                right = mid - 1
                continue
            if target > val:
                left = mid + 1
                continue
            return mid
        return left
    
    def add(self, val: int):
        if val in self.tally:
            self.tally[val]+= 1
        else:
            self.vals.insert(self._insert_position(val), val)
            self.tally[val] = 1
        self.size+= 1
        
    def remove(self, val: int):
        if val not in self.tally:
            return
        self.tally[val]-= 1
        self.size-= 1
        if self.tally[val] > 0:
            return
        self.tally.pop(val, None)
        self.vals.remove(val)    

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        N = len(heights)
            
        borrowers = Ledger()
        for i in range(N - 1):
            jump = max(0, heights[i + 1] - heights[i])
            
            # no jump needed -> next building for free
            if jump < 1:
                continue
            
            # jump needed, dispose ladder if available
            if ladders > 0:
                borrowers.add(jump)
                ladders-= 1
                continue
            
            # see if you can trade bricks for a ladder from an exisiting borrower
            # replace smallest borrower with current jump ONLY IF current jump is bigger
            # replacement can only happen if there is ALSO enough bricks
            smallest_borrower = borrowers.get_min()
            if borrowers.size > 0 and jump > smallest_borrower and bricks >= smallest_borrower:
                bricks-= smallest_borrower
                borrowers.remove(smallest_borrower)
                borrowers.add(jump)
                continue
                
            # no borrowers to replace AND no ladders to use
            # can only rely on bricks
            if bricks < jump:
                return i
            
            # enough bricks to make the jump
            bricks-= jump
            
        return N - 1
    
