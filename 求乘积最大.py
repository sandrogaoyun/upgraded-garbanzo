#设定一个长度为 N 的数字串，将其分为两部分，
#找出一个切分位置，使两部分的乘积值最大，并返回最大值。
#如输入123，可拆分成1,23或12,3，所以返回值是12*3=36

#我的做法
def product(num):
    l = len(str(num)) # 数字长度
    s = l - 1 # 有l-1种分割方法
    n = list(str(num))
    p_max = 0 #乘积最大值
    for i in range (1, s + 1):
        #第i种分割，左边是n[0:i],i个数字组成一个数,
        #右边是n[i-1:l-1],(l-i)个数字组成一个数
        p_l = num_comb(n[0:i],i)
        p_r = num_comb(n[i:l],(l-i))
        p = p_l * p_r
        if p > p_max:
            p_max = p
    return p_max

def num_comb(n, l):
    #n是个l位的列表，所有元素都是一位数字，返回列表按顺序组成的数值
    #比如n=["1", "2", "3"]，返回int型123
    sum = 0
    for i in range (0, l):
        sum += (int(n[i])) * (10 ** (l-1-i))
    return sum

print(product(312))
print(product(1234))
print(product(12345))

import itertools

def product_2(num):
    num_all = list(itertools.permutations(str(num), len(str(num))))
    p_max = 0
    for i in num_all:
        p = product(num_comb(i, len(i)))
        if p > p_max:
            p_max = p
    return p_max

print(product_2(1234))


#标准做法
def product(num):
    # 数字转为字符串
    num2str = str(num)    
    # 预设最大的结果
    max_num = 0
    len_str = len(num2str)    
    for i in range(1,len_str):        
        # 分别得到字符串两边
        left = num2str[:i]
        right = num2str[i:]
        res = int(left) * int(right)        
        # 如果现在的乘积超过目前的乘积，则更新最大值
        if res > max_num:
            max_num = res    
    return max_num

print(product(312))
