from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        LEN = len(nums)
        SUM = sum(nums)
        
        curr_sum = 0
        for i in range(LEN):
            if nums[i]+(curr_sum*2) == SUM:
                return i
            curr_sum += nums[i]
        return -1

if __name__ == '__main__':
    leetcode = Solution()
    result = leetcode.pivotIndex([1,7,3,6,5,6])
    print(result)
