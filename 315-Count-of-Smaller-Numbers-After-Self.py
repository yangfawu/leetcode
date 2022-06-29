class Solution:
    def _bin_last_pos(self, arr: List[int], left: int, target: int):
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) >> 1
            val = arr[mid]
            if val == target and (mid < 1 or arr[mid - 1] < target):
                return mid
            if val < target:
                left = mid + 1    
                continue
            right = mid - 1
        return left
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        # dp[i] = # of elements smaller than dp[i] on the right
        dp = N*[0]
        
        # ordered list of #s from nums
        queue = []
        
        # map # -> last first index
        seen = {}
        for i in range(N - 1, -1, -1):
            d = nums[i]
            j = self._bin_last_pos(queue, seen[d] if d in seen else 0, d)
            dp[i] = seen[d] = j
            queue.insert(j, d)
                
        return dp
      
