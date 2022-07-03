class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        
        # rising[i] = longest sub sequence with rising end after considering i-th element
        rising = N*[0]
        
        # falling[i] = longest sub sequence with falling end after considering i-th element
        falling = N*[0]
        
        rising[0] = falling[0] = 1
        for i in range(1, N):
            diff = nums[i] - nums[i - 1]
            rising[i] = rising[i - 1]
            falling[i] = falling[i - 1]
            if diff < 0:
                falling[i] = 1 + rising[i - 1]
            elif diff != 0:
                rising[i] = 1 + falling[i - 1]
        
        # get longest sub sequence with rising/falling edge
        return max(rising[N - 1], falling[N - 1])
        
