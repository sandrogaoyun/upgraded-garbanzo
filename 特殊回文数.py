#123321是一个非常特殊的数，它从左边读和从右边读是一样的，我们称这样的数为回文数。
#给你一个正整数n， 编程求所有这样的五位和六位十进制数，
#满足各位数字之和等于n(5<=n<=54)。
#按从小到大的顺序输出满足条件的整数。

n = int(input("请输入(5<=n<=54)：")) #先不考虑各种字符检测

#最土的做法
#计算满足条件的5位数
for i in range (1, 10): #第一、五位数字
    for j in range (0, 10): #第二、四位数字
        for k in range (0, 10): #第三位数字
            if i + j + k + j + i == n:
                tmp = i * 10001 + j * 1010 + k * 100
                print(tmp)
                
#计算满足条件的6位数
for i in range (1, 10): #第一、六位数字
    for j in range (0, 10): #第二、五位数字
        for k in range (0, 10): #第三、四位数字
            if i + j + k + k + j + i == n:
                tmp = i * 100001 + j * 10010 + k * 1100
                print(tmp)

#好的做法
def reverse(n):
    # 返回一个整数的逆序
    return int(str(n)[::-1])

def accumulate(n):
    # 返回一个整数的各位数之和
    return sum([int(x) for x in str(n)])

for i in range(10000,1000000):
    if i == reverse(i) and accumulate(i) ==n:
        print(i)
