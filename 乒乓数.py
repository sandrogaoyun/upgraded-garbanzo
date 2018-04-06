"""
乒乓序列从1开始计数，并且始终向上或向下计数。
在元素k处，如果k是7的倍数或包含数字7，方向将切换。
乒乓序列的前30个元素如下所示，方向交换在第7,14和17，21，第27和28个元素：
1 2 3 4 5 6 [7] 6 5 4 3 2 1 [0] 1 2 [3] 2 1 0 [-1] 0 1 2 3 4 [5] [4] 5 6
"""
def contain(i, k): #如果i是k的倍数或包含数字k，返回True，否则返回False
    if i % k == 0:
        return True
    for x in str(i):
        if x == str(k):
            return True
    return False
    

def pingpong(n, k):
    direct = 1 # 初始方向为向上
    num = 1 # 初始数字为1
    if n == 1:
        print (1)
        return num
    pre_num = 1
    for i in range (2, n + 1):
        pre_num = num
        num = pre_num + direct
        if contain(i, k):
            direct = direct * (-1)
    print (str(num))
    return num

pingpong(100, 9)

