class Solution:
    def _check(self, nums: List[int], N: int, start: int, prev_max: int, warned: bool) -> bool:
        curr_max = nums[start]
        for i in range(start + 1, N):
            d = nums[i]
            
            # if the current element is not >= current max
            # then we have a problem with the array not being non-decreasing
            if d < curr_max:
                # if we have already warned, then this array is hopeless
                if warned:
                    return False
                
                # if this is the first warning AND the element satisfies the previous max
                # then we can throw out the current max AND perform a new check
                # we will only warn if the new check fails (returns False)
                warned = d < prev_max or not self._check(nums, N, i, prev_max, True)
                continue
            prev_max, curr_max = curr_max, d
        return True
        
    def checkPossibility(self, nums: List[int]) -> bool:
        N = len(nums)    
        if N < 3:
            # array can always be fixed if we have < 3 elements
            return True
        return self._check(nums, N, 0, float("-inf"), False)
      
