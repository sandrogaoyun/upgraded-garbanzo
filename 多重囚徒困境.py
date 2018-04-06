"""
两个共谋犯罪的人被关入监狱，不能互相沟通情况。
如果两个人都不揭发对方，则由于证据不确定，每个人都坐牢一年；
若一人揭发，而另一人沉默，则揭发者因为立功而立即获释，沉默者因不合作而入狱五年；
若互相揭发，则因证据确实，二者都判刑两年。
"""
#多重囚徒困境
#求进行 N 次博弈下，使用不同的策略，囚犯各自的获刑年限

"""
目前有三种策略：
nice：不管对方揭发还是沉默，都保持沉默
rat：不管对方沉默还是揭发，都选择揭发
tit_for_tat：第一轮选择沉默，第二轮开始如果对方上一轮沉默，本轮就选择沉默，
对方上一轮揭发，本轮也选择揭发。
"""
#expose: 揭发
#silent: 沉默

def sentence(choice1, choice2):
    if (choice1, choice2) == ("expose", "expose"):
        return (2, 2)
    if (choice1, choice2) == ("silent", "silent"):
        return (1, 1)
    if (choice1, choice2) == ("expose", "silent"):
        return (0, 5)
    if (choice1, choice2) == ("silent", "expose"):
        return (5, 0)

def nice(last_turn): #保持沉默
    return "silent"

def rat(last_turn): #总是揭发
    return "expose"
 
def tit_for_tat(last_turn):
    #第一轮选择沉默，如果对方上一轮沉默，本轮就选择沉默，
    #对方上一轮揭发，本轮也选择揭发。
    if last_turn == "expose":
        return "expose"
    else:
        return "silent"

def prisoner_delimma(N, strategy1, strategy2):
    p1_sentence = 0
    p2_sentence = 0
    p1_last_turn = " "
    p2_last_turn = " "
    for i in range (0, N):
        p1_choice = strategy1(p2_last_turn) #函数也是一种对象，可以直接这样传值
        p2_choice = strategy2(p1_last_turn) #函数也是一种对象，可以直接这样传值
        p1_last_turn = p1_choice
        p2_last_turn = p2_choice
        p1_sentence += sentence(p1_choice, p2_choice)[0]
        p2_sentence += sentence(p1_choice, p2_choice)[1]
    print (str(p1_sentence), str(p2_sentence))

prisoner_delimma(4, nice, nice)
prisoner_delimma(5, rat, rat)
prisoner_delimma(6, nice, rat)
prisoner_delimma(4, rat, tit_for_tat)
prisoner_delimma(7, tit_for_tat, tit_for_tat)


