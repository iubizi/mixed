'''
# 是错误的，会把正着反着全部输出一遍，而且自己和自己也输出了
LEN = 20
arr = list(range(LEN))

target = 10

num_dict = {}

for i in range(LEN):
    num_dict[arr[i]] = i

for i in range(LEN):
    if target-arr[i] in num_dict:
        print(i, num_dict[target-arr[i]])
'''

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        LEN = len(nums)
        num_dict = dict()
        for i in range(LEN):
            if target - nums[i] in num_dict:
                return [num_dict[target - nums[i]], i]
            num_dict[nums[i]] = i
        return []

if __name__ == '__main__':
    nums = list(range(20))
    
    leetcode = Solution()
    print(leetcode.twoSum(nums=nums, target=10))
