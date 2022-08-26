from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = 0
        
        LEN = len(nums)
        
        for i in range(LEN):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            if left_sum == right_sum:
                return i
        return -1

if __name__ == '__main__':
    leetcode = Solution()
    result = leetcode.pivotIndex([1,7,3,6,5,6])
    print(result)
