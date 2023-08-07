# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:54:30 2023

@author: MAIN
"""

import time

#append와 extend함수 시간차이 계산
def app_ext_time():
    temp = 'test python program'
    sample_list=[]
    start = time.time()
    sample_list.append(temp)
    appendt = time.time()-start

    sample_list = []
    start1 = time.time()
    sample_list.extend([temp])
    extendt = time.time()-start1

    if appendt > extendt:
        short = "extend"
    else:
        short = "append"
    print(f'extend {extendt} \n append {appendt}\n {short}가 더 빠릅니다.')



#출석부 문제
def attendance():
    stu_list = ['이황','이이','원효']

    new_stu = input('전학 온 학생은 누구입니까? : ')
    stu_list.append(new_stu)
    stu_list.sort()
    for i, student in enumerate(stu_list, start=1):
        print(f"{i}번 : {student}")
        
#조건 만족하는 리스트 만들기
#1. 제곱리스트
def squared_list():
    squared_list = [i**2 for i in range(30)]
    print(squared_list)
    
#2. a가 있는 단어만 골라 리스트만들기
def fruits():
    fruits = ["apple","banana","cherry","kiwi","mango"]
    newlist = [x for x in fruits if 'a' in x]
    print(newlist)
'''
같은 뜻
fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
'''

#3. 홀수 제곱리스트
def odd_squared_list():
    squared_list_2 = [i**2 for i in range(30) if i % 2 == 1]
    print(squared_list_2)
    
#4. 짝짓기
def match_():
    seq1 = 'abc'
    seq2 = (1,2,3)
    
    seq_list = [(x,y) for x in seq1 for y in seq2]
    print(seq_list)