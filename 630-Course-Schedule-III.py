class Solution:
    def _bin_insert_pos(self, arr: List[int], target: int) -> int:
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
    
    def insert_inorder(self, arr: List[int], target: int):
        arr.insert(self._bin_insert_pos(arr, target), target)
    
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # greeedy sort by end date
        courses.sort(key=lambda c : c[1])
        
        # list of all the taken courses' durations [always ASC order]
        taken = []
        
        # simulation
        # curr_total is the sum of all durations in <taken>
        # during the iteration, we know that the deadline is always non-decreasing
        # this means that the current deadline in an iteration is always the latest one
        curr_total = 0
        for duration, deadline in courses:
            new_total = curr_total + duration
            
            # if the new_total falls under the new deadline, add it into the list
            if new_total <= deadline:
                self.insert_inorder(taken, duration)
                curr_total = new_total
                continue
                
                
            # we now know we can't fit new course without bargaining
            # we can always switch out the currently largest duration course for this new one
            # but don't even bother if there are no durations to make the swap
            if len(taken) < 1:
                continue
            
            # if the new course duration is greater than all exisitng durations
            # then there is no point is making the swap
            if duration >= taken[-1]:
                continue
            
            # perform swap
            new_total-= taken.pop()
            self.insert_inorder(taken, duration)
            curr_total = new_total
        
        return len(taken)
      
