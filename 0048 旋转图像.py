def tp(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr[0])):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    return arr

def flip(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])>>1):
            arr[i][j], arr[i][len(arr[0])-1-j] = \
            arr[i][len(arr[0])-1-j], arr[i][j]
    return arr

def print_arr(arr):
    for i in arr:
        print(i)
    print()

if __name__ == '__main__':
    
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    print_arr(arr)
    print_arr(tp(arr))

    arr = [[1,2,3],[4,5,6],[7,8,9]]
    print_arr(arr)
    print_arr(flip(arr))
