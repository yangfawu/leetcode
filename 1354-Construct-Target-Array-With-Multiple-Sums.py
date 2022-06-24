class Solution:
    def _bin_insert_pos(self, arr: List[int], target: int):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) >> 1
            val = arr[mid]
            if val < target:
                left = mid + 1
                continue
            if val > target:
                right = mid - 1
                continue
            return mid
        return left
    
    def _insert_inorder(self, arr: List[int], target: int):
        arr.insert(self._bin_insert_pos(arr, target), target)
    
    def isPossible(self, target: List[int]) -> bool:
        # populate priority queue from smallest to biggest value
        # we will ignore entries with a 1 because we cannot reverse engineer any further
        pq = []
        curr_sum = 0
        for d in target:
            if d > 1:
                self._insert_inorder(pq, d)
            curr_sum+= d
        
        # we will keep shaving away the largest entry until there's none left
        # when there's none left, we should have a 1-vector
        while len(pq) > 0:
            v = pq.pop()
            diff = curr_sum - v
            
            # if the value is the only item in pq,
            # then pq will only be filled with this value's previous states
            if len(pq) < 1:
                # use mod to see if we can reach 1
                return diff != 0 and (v - 1) % diff == 0
            
            # compute previous state of largest value
            v_prev = v - diff
            
            # swap largest value with previous state
            # same as making current_sum become the current largest value
            curr_sum = v
                
            # we already know pq is not empty
            # sometimes v_prev is also the previous state's largest value
            next_v = pq[-1]
            if next_v <= v_prev:
                # note: if v_prev <= 1, this check automatically gets skipped because pq wont have smaller values
                # we can shave down v_prev until it is smaller than the next largest value
                diff*= math.ceil((v_prev - next_v)/diff)
                v_prev-= diff
                curr_sum-= diff
            
            if v_prev < 1:
                # if the previous state is anything less than 1, then we cannot solve
                return False
            if v_prev < 2:
                # if the previous state is 1, we cannot reverse engineer any further
                continue
            self._insert_inorder(pq, v_prev)
        
        return True
      
