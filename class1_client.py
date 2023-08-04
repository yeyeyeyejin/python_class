# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:15:30 2023

@author: MAIN
"""

import class1_module as c1


print(c1.AND(0,0))
print(c1.AND(0,1))
print(c1.AND(1,0))
print(c1.AND(1,1))


sen = '''여기는 여러줄을 문자열로 받아 들일 때 삼따움표를 사용합니다.'''
print(sen*5)
print(sen + 'Test') 
print('파이썬 '+'프로그래밍 '+'시간입니다. ')


c1.math_s()
c1.cmath_s()


a, b, c = 1, 2, 4
print(c1.ex1(a,b,c))


m = 6547000
c1.money(m)

y = 2022
print(c1.leap_year(y))