# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 13:49:14 2023

@author: MAIN
"""

import keyword

#조건문 예제1. 이름확인코드
def name_check(name):
    if name == '블랙핑크':
        return '본인입니다.'
    else:
        return '본인이 아닙니다.'
    
#조건문 예제2. 개월 수별 예방접종
'''
내 코드
def vaccin(age):
    if age < 2.0 :
        print('결핵 예방접종 대상자입니다.')
        print('B형감염 예방접종 대상자입니다.')
    if 2.0 <= age < 6.0:
        print('B형감염 예방접종 대상자입니다.')
        print('파상풍 예방접종 대상자입니다.')
        print('폐렴구균 예방접종 대상자입니다.')
    if 6.0 <= age < 15.0:
        print('파상풍 예방접종 대상자입니다.')
        print('폐렴구균 예방접종 대상자입니다.')
    if 15.0 <= age < 16.0 : 
        print('폐렴구균 예방접종 대상자입니다.')
'''
#모범답안
def vaccin(age):
    if age < 2:
        print('결핵 예방접종 대상자입니다.')
    if age < 6:
        print('B형감염 예방접종 대상자입니다.')
    if 2 <= age < 15:
        print('파상풍 예방접종 대상자입니다.')
    if  2 <= age <= 15:
        print('폐렴구균 예방접종 대상자입니다.')
        
#조건문예제3. 최댓값 찾기
def find_max(num1,num2,num3):
    if num1 < num3 and num2 < num3:
        print('최대값은', num3)
    if num1 < num2 and num3 < num2:
        print('최대값은', num2)
    if num2 < num1 and num3 < num1:
        print('최대값은', num1)
'''
같은 뜻 -> elif을 사용해서
def find_max(num1,num2,num3):
    if num1 < num3 and num2 < num3:
        print('최대값은', num3)
    elif num1 < num2 and num3 < num2:
        print('최대값은', num2)
    else :
        print('최대값은', num1)
        
같은 뜻2
'''
def find_max2(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        print('최대값은', num1)
    elif num2 > num3:
        print('최대값은', num2)
    else :
        print('최대값은', num3)
        

#조건문예제4. 윤년문제 다르게 풀기
def leap_year(year):
    cond1 = (year%4) == 0
    cond2 = (year%100) !=0
    cond3 = (year%400) == 0
    case1 = cond1 and cond2 or cond3

    if case1:
        print('leap year')
    else:
        print('not leap year')


#조건문예제5. 점수별 등급매기기
def grade(score):
    if score >= 90.0:
        print('A등급입니다.')
    elif score >= 80.0:
        print('B등급입니다.')
    elif score >= 70.0:
        print('C등급입니다.')
    elif score >= 60.0:
        print('D등급입니다.')
    else:
        print('F등급입니다.')
        

#조건문예제6. 홀짝판별
def odd_even(x):
    if x % 2 == 0:
        print('짝수입니다.')
    else:
        print('홀수입니다.')
'''
더 세심하게 한다면,
def odd_even(x):
    if x <= 0:
        print('자연수가 아닙니다.')
    elif x % 2 == 0:
        print('짝수입니다.')
    else:
        print('홀수입니다.')
'''


#조건문예제7. BMI로 비만분류하기
def bmi(weight,height):
    bmi = weight/(height/100)**2

    if bmi >= 30.0:
        print('고도비만입니다.')
    elif bmi>= 25.0:
        print('비만입니다.')
    elif bmi >= 23.0:
        print('과체중입니다.')
    elif bmi >= 18.5:
        print('정상입니다.')
    else:
        print('저체중입니다.')
        

#반복문예제1. 좋아하는 색, 단어 출력
def for_ex(fav_color,words,list2):
    for i in fav_color:
        print(i)
    for i in words:
        print(i,len(i))
    for i in list2[1:]:
        print(i)
        
        

#반복문예제2. for와 range응용
def for_ex2():
    result1 = []
    result2 = []
    result3 = []
    result4 = []
    
    for i in range(11):
        result1.append(i)
    print(result1)
    
    for i in range(5,16):
        result2.append(i)
    print(result2)
    
    for i in range(0,22,2):
        result3.append(i)
    print(result3)
    
    for i in range(-100,101,4):
        result4.append(i)   
    print(result4)
    

#반복문예제3. 합
def sums(x):
    total = 0
    for i in range(1,x+1):
        total += i
    return total
    
        
    
# import keyword
k_list = keyword.kwlist
        


#반복문예제4. 곱
def mult(x):
    total = 1
    for i in range(1, x+1):
        total *= i
    return total


#반복문예제5. 구구단
#2단 구구단
def gugudan_2():
    for i in range(1,10):
        print('2*',i,'=',2*i)
#2단~9단
def gugudan_2_9():
    for i in range(2,10):
        print(i,'구구단')
        for j in range(1,10):
            print(i,'*',j,'=',i*j)
#출력을 한줄씩 나오게
def gugudan_2_9_2():
    for i in range(2,10):
        for j in range(1,10):
            m = i * j
            print(i,'*',j,'=',m, end='  ')
        print() 
        

#while문예제. 소수찾기
def prime(x):
    i = 2
    
    while x % i != 0:
        i += 1
        
    if i == x:
        return '소수입니다.'
    else:
        return '소수가 아닙니다.'
                   