class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        LEN = len(nums)
        output = [1 for _ in range(LEN)]
        
        left = 1
        for i in range(LEN):
            output[i] *= left
            left *= nums[i]
            
        right = 1
        for i in range(LEN-1, -1, -1):
            output[i] *= right
            right *= nums[i]    
        
        return output
