# -*- coding: UTF-8 -*-
# python 练习100道题

from pip import main


def helloWorld():
    '''
    打印输出 'Hello World!'
    '''
    print('Hello World!')


def sum():
    """
    根据输入的数字进行求和
    """
    firstNumber = float(input("请输入第一个数字："))
    secendNumber = float(input("请输入第二个数字："))
    sum = firstNumber + secendNumber
    print('数字{0} 和数字{1}的和是：{2}'.format(firstNumber, secendNumber, sum))


def sum2():
    '''
    输入一组数字，计算数字的和，要求每个数字之间用空格隔开
    '''

    sum = 0
    inputNum = input("请输入一组数字（数字之间用空格相隔）：")
    num = inputNum.split(' ')
    for i in num:
        sum += float(i)
    print(sum)


def sqrt():
    """
    对输入的正数进行开平方根
    """
    inputNum = float(input("请输入数字："))
    sqrt = inputNum ** 0.5
    print(sqrt)







if __name__ == '__main__':

    helloWorld()
    sum()
    sum2()
    sqrt()