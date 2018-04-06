#韩信带着 10000 金币和纠结，来到了神秘的古老商店，他仅有如下装备选择：
#影忍之足：690
#巨人之握：1500
#破甲弓：2100
#泣血之刃：1740
#无尽战刃：2140
#贤者的庇护：2080

#在不考虑装备重复的情况之下，即可以多次购买一件装备，要填满六格物品栏，有多少种购买方式？写一个程序，输出所有可行的购买组合。

#附加题：
#1、如果没有6格物品栏限制，有多少种购买方式？
#2、在 1 的前提下，影忍之足最多购买一次，现在有多少种购买方式？



import itertools

equipment = [690,1500,2100,1740,2140,2080]

# 装满 6 格，金额小于 10000
def func1():
    conb = itertools.combinations_with_replacement(equipment,6)
    count = 0
    for i in conb:
        if sum(i) < 10000:
            count += 1
    return count

print(func1())


# 没有格子的限制，
def func2():
    count = 0
    for j in range(1,(10000//min(equipment)+1)):
        conb = itertools.combinations_with_replacement(equipment,j)
        for i in conb:
            if sum(i) < 10000:
                count += 1
    return count

print(func2())

# 在附加题一的限制下，价值690的鞋子最多出现一次
def func3():
    count = 0
    for j in range(1,(10000//min(equipment)+1)):
        conb = itertools.combinations_with_replacement(equipment,j)
        for i in conb:
            if sum(i) < 10000 and i.count(690) <= 1:
                count += 1
    return count

print(func3())
