LEN = 20
arr = list(range(LEN))

target = 10

for i in range(LEN):
    for j in range(i+1, LEN):
        if arr[i] +arr[j] == target:
            print(i, j)
