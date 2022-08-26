nums = [1,2,3,4,5,6,7]
k = 3

LEN = len(nums)

for _ in range( LEN - k%LEN ):
    nums.append( nums.pop(0) )

print(nums)
