# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:13:50 2023

@author: MAIN
"""

import numpy as np
import math
import cmath

def AND(x1, x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.dot(x,w)+b
    if tmp < 0:
        return 0
    else:
        return 1

#import math
def math_s():
    print(math.sqrt(2.0))  #제곱근(복소수는X)
    print(math.pi) #3.14
    
#import cmath  -> 복소수계산 가능
def cmath_s():
    print(cmath.sqrt((-4)))
    print(cmath.sqrt((2+4j)))
    


#코딩예제1. 근의 공식
def ex1(a, b, c):
    D = b**2 - 4*a*c
    x = ((-b + cmath.sqrt(D))/(2*a),
         (-b - cmath.sqrt(D))/(2*a))
    return x


#코딩예제2. 지폐계수기 프로그램
'''
내 답안1
def money(m):
    a = m//50000
    b = (m - a*50000)//10000
    c = (m - a*50000 - b*10000)//5000
    d = (m - a*50000 - b*10000 - c*5000)//1000
    return f'지폐 개수 = {a+b+c+d}'

내 답안2
def money(m):
    a = m//50000
    b = (m%50000)//10000
    c = (m%10000)//5000
    d = (m%5000)//1000
    return '지폐 개수 = {a+b+c+d}'
'''
def money(x):
    a = x // 50000
    b = (x % 50000) // 10000
    c = (x % 10000) // 5000 
    d = (x % 5000) // 1000
    
    print('5만원권', a, '장')
    print('1만원권', b, '장')
    print('5천원권', c, '장')
    print('1천원권', d, '장')
    

#코딩예제3. 윤년구하기
def leap_year(y):
    cond1 = y%4 == 0
    cond2 = y%100 != 0
    cond3 = y%400 == 0
    leapy = cond1 and (cond2 or cond3)
    if leapy == True:
        return f'{y}년은 윤년이다.'
    else:
        return f'{y}년은 윤년이 아니다.'








