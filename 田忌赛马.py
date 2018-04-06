"""
现在我们将齐王的马抽象为一个列表 [3,6,9]，田忌的马抽象为另一个列表 [2,5,8]，
分别代表各自的下、中、上等马。
设计一个函数 race()，将两个列表作为参数传递给 race()，
将背景资料的策略抽象为代码使田忌赢得比赛，函数返回每轮对阵情况
"""

import itertools

qi_wang = [3, 6, 9]
tian_ji = [2, 5, 8]

#期望输出结果[(3, 5), (6, 8), (9, 2)]

def race (p1, p2):
    match = [] #每局比赛, 比如((3, 2), (6, 5), (9, 8))
    p1_l = [] #p1所有派遣马匹的方式
    p2_l = [] #p2所有派遣马匹的方式
    p2_l = list(itertools.permutations(p2, 3)) 
    for i in range (0, len(p2_l)):
        p1_l.append(p1)
    match_win = 0
    for i in range (0, len(p2_l)): #每局比赛，包括三轮
        game_win = 0
        game = []
        for j in range (0, len(p2_l[i])): #每轮比赛，
            if p1_l[i][j] < p2_l[i][j]:
                game_win += 1
            game.append((p1_l[i][j], p2_l[i][j]))
        if game_win >= 2:
            match_win += 1
            match.append(game)
            print (match)

race (qi_wang, tian_ji)
