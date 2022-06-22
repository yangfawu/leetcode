class Solution:
    def _bin_insert_position(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) >> 1
            val = arr[mid]
            if target < val:
                right = mid - 1
                continue
            if target > val:
                left = mid + 1
                continue
            return mid
        return left
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # map int -> count
        tally = {}
        
        # all unique values from least to greatest
        values = []
        
        # read in all values
        for d in nums:
            if d in tally:
                tally[d]+= 1
            else:
                tally[d] = 1
                values.insert(self._bin_insert_position(values, d), d)
        
        # find k-th largest starting at the end of the list
        for i in range(len(values) - 1, -1, -1):
            d = values[i] # the number
            c = tally[d] # the count of the number
            if k <= c:
                return d
            k-= c
        
        # default return never reached if k is valid
        return None
      
