"""
1、 用户登陆程序需求:
1. 输入用户名和密码;
2. 判断用户名和密码是否正确? (name='root', passwd='westos')
3. 为了防止暴力破解， 登陆仅有三次机会， 如果超过三次机会， 提示错误次数过多，账号已被冻结;
"""


def login():
    for i in range(1, 4):
        name = input("请输入用户名：")
        pwd = input("请输入密码：")
        if name == "root" and pwd == "westos":
            print("登陆成功")
            break
        if 3 - i > 0:
            print("账号密码错误，还有{}次机会！！！".format(3 - i))
        else:
            print("错误次数过多，账号已被冻结")


# login()

"""
2、给定一个句子（只包含字母和空格）， 将句子中的单词位置反转，
比如： “hello xiao mi” > “mi xiao hello”
"""


def reverse_sentence(str1="hello xiao mi"):
    list1 = str1.rsplit(" ")
    list1.reverse()
    str2 = " ".join(list1)
    print(str2)


# reverse_sentence()

"""
3、运行程序，提示用户依次输入三个整数x,y,z，请把判断三个数的大小，然后由小到大打印输出到控制台
"""


def max_num():
    num = input("请依次输入三个整数，以空格隔开:")
    num_max = max([int(i) for i in num.rsplit(" ")])
    print("最大数为：", num_max)


# max_num()
"""
4、 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多
少米？第10次反弹多高？
"""


def rebound(height=100, num=10):
    m = 0
    height2 = 100
    for i in range(1, num + 1):
        if i == 1:
            m += 100
        else:
            height2 = height / (2 ** (i - 1))
            m += 2 * height2
    print("它在第{}次落地时，共经过{}米，反弹了{}米".format(num, m, height2))


# rebound(100, 10)

"""
5、题目：猴子吃桃问题：
猴子第一天摘下若干个桃子，当即吃了一半，还不过瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃
了一个。以后每天早上都吃了前一天剩下的一半 在加一个。到第10天早上想再吃时，见只剩下一个桃子了。
请通过一段通过代码来计算第一条摘了多少个桃子？
"""


def eat_peach(day=10):
    x = 1
    for i in range(day - 1, 0, -1):
        x = (x + 1) * 2
    print(x)


# eat_peach()

"""
6、题目：输入某年某月某日，判断这一天是这一年的第几天？
"""


def calculated_days():
    date = input("请输入日期格式为1996/02/20：")
    d = [int(i) for i in date.rsplit("/")]
    year = d[0]
    month = d[1]
    day = d[2]
    print(year, month, day)

    for i in range(1, month):
        if i in [1, 3, 5, 7, 8, 10, 12]:
            day += 31
        elif i == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                day += 29
            else:
                day += 28
        else:
            day += 30
    print("{}为{}年的第{}天".format(date, year, day))


# calculated_days()

"""
7、小明有100块钱 ，准备买100本书，a类数5元一本，b类书3元一本，c类书 1元2本。请计算小明有多少种购买的
方式？
"""


def work7():
    count = 0
    for a in range(100 // 5 + 1):
        for b in range(100 // 3 + 1):
            if a * 5 + b * 3 + (100 - a - b) * 0.5 <= 100:
                # print(f"{a},{b},{100 - a - b}")
                count += 1
    return count


# print(work7())

"""
8、题目：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时，高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于
100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
"""


def work8():
    price = float(input("请输入当月利润:"))
    if price < 0:
        print("您输入的金额有误！")
    elif price <= 100000:
        return price * 0.1
    elif price <= 200000:
        # 10万元以内的提成
        m1 = 100000 * 0.1
        # 超出10万部分的提成
        m2 = (price - 100000) * 0.075
        return m1 + m2
    elif price <= 400000:
        # 20万元以内的提成
        m1 = 100000 * 0.1 + 100000 * 0.75
        # 超出20万部分的提成
        m2 = (price - 200000) * 0.05
        return m1 + m2
    elif price <= 600000:
        # 40万元以内的提成
        m1 = 100000 * 0.1 + 100000 * 0.75 + 200000 * 0.05
        # 超出40万部分的提成
        m2 = (price - 400000) * 0.03
        return m1 + m2
    elif price <= 1000000:
        # 60万元以内的提成
        m1 = 100000 * 0.1 + 100000 * 0.75 + 200000 * 0.05 + 200000 * 0.03
        # 超出60万部分的提成
        m2 = (price - 600000) * 0.015
        return m1 + m2
    else:
        # 100万元以内的提成
        m1 = 100000 * 0.1 + 100000 * 0.75 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015
        # 超出60万部分的提成
        m2 = (price - 1000000) * 0.01
        return m1 + m2


# print(work8())

"""
9、编写一个自动售货机，运行功能如下:
1、请按下面提示，选择购买的商品
1). 可乐 2.5元 2). 雪碧 2.5元 3). 哇哈哈 3元 4). 红牛 6元 5). 脉动 4元 6). 果粒橙 3.5元
2、提示用户投币（支持1元，5元，10元）
用户输入投币金额，
用户投币金额不够商品价格，继续提示投币，
当投币超过商品价格，则返回商品和找零，然后结束程序
"""


def vending_machine():
    try:
        num = int(input("请按下面提示，选择购买的商品(1). 可乐 2.5元 (2). 雪碧 2.5元 (3). 哇哈哈 3元 (4). 红牛 6元 (5). 脉动 4元 (6). 果粒橙 3.5元"))
        if num in [1, 2, 3, 4, 5, 6]:
            shop = {1: 2.5, 2: 2.5, 3: 3, 4: 6, 5: 4, 6: 3.5}
            m = 0
            while True:
                n = int(input("请投币（支持1元，5元，10元）/元："))
                if n in [1, 5, 10]:
                    p = shop[num]
                    m += n
                    if p <= m:
                        print("购买成功，价格{}元，投币{}元，找零{}元".format(p, m, m - p))
                        break
                    print("投币金额不足,还差{}元".format(p - m))
                    continue
                print("请重新投币")
    except ValueError:
        print("请按要求输入！！！")

# vending_machine()
