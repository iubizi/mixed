def func(digits):
    digits = [0] + digits # 添加首位
    digits[-1] += 1 # 整个数+1

    for i in range(len(digits)-1, 0, -1): # 从最后一位到第二位
        if digits[i] == 10:
            digits[i] = 0 # 10没了
            digits[i-1] += 1 # 进位
        else: # 行波加法器结束
            break

    if digits[0] == 0:  return digits[1:]
    else:               return digits
    
if __name__ == '__main__':
    digits = [4,3,2,1]
    print( func(digits) )
