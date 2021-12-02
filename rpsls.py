#coding:
"""
程序目标：通过自定义函数，实现RPSLS游戏，即用户通过键盘输入任意一个选择（石头/剪刀/布/蜥蜴/史波克），计算机自动生成一个随机选择，根据RPSLS规则，产生最终的结果
程序作者：杨燎原
日期；2021/12/01
"""
print("请输入你的选择：")
x = input()
print("-------")
if x in ("石头", "史波克", "布", "蜥蜴", "剪刀"):
    print("你的选择为：", x)
else:
    print("Error: No Correct Name")
if x in ("石头", "史波克", "布", "蜥蜴", "剪刀"):
    def name_to_number(x):
        if x == "石头":
            a = 0
        elif x == "史波克":
            a = 1
        elif x == "布":
            a = 2
        elif x == "蜥蜴":
            a = 3
        elif x == "剪刀":
            a = 4
        return a
    a = name_to_number(x)
    import random
    answer = random.randint(0, 4)
    def number_to_name(answer):
        if answer == 0:
            y = "石头"
        elif answer == 1:
            y = "史波克"
        elif answer == 2:
            y = "布"
        elif answer == 3:
            y = "蜥蜴"
        elif answer == 4:
            y = "剪刀"
        return y
    y = number_to_name(answer)
    print("计算机的选择为：", y)
    def rpsls(a, answer):
        if a == 0:
            if answer == 3 or answer == 4:
                result = "你赢了！"
            elif answer == 0:
                result = "您和计算机出的一样呢"
            else:
                result = "机器赢了"
        elif a == 1:
            if answer == 0 or answer == 4:
                result = "你赢了！"
            elif answer == 1:
                result = "您和计算机出的一样呢"
            else:
                result = "机器赢了"
        elif a == 2:
            if answer == 0 or answer == 1:
                result = "你赢了！"
            elif answer == 2:
                result = "您和计算机出的一样呢"
            else:
                result = "机器赢了"
        elif a == 3:
            if answer == 1 or answer == 2:
                result = "你赢了！"
            elif answer == 3:
                result = "您和计算机出的一样呢"
            else:
                result = "机器赢了"
        elif a == 4:
            if answer == 2 or answer == 3:
                result = "你赢了！"
            elif answer == 4:
                result = "您和计算机出的一样呢"
            else:
                result = "机器赢了"
        return result
    t = rpsls(a, answer)
    print(t)
