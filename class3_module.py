# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:30:19 2023

@author: MAIN
"""

#break문과 continue문
#예제1. 소수인지 프로그램
def prime(num):
    i = 2
    flag = 1
    while i < num:
    # i += 1 여기에 있으면 979일 때가 걸리기 때문에 소수가 아니라고만 나옴
        res = num % i
        if res == 0:
            print(i)
            flag = 0
            break    #반복문을 빠져나온다.
        #continue 아래 조건 하지 않고 바로 조건문으로 다시 올라간다.
        i += 1          #i +=1 의 위치 조심

    if flag:    
        return ('소수입니다.')
    else:
        return('소수가 아닙니다')
    
#예제2. 
def ex2():
    for i in range(10):
        if 3 < i < 6:
            continue  #break 보다 continue를 먼저 만나서 조건 발동이 안 됨.
            break
        print(i)
        
#예제3. 
def ex3():
    for i in range(20):
        if i % 3 == 0:
            continue
        if i > 16:
            break
        print(i)
        
#예제4.
def ex4():
    i = 0
    while i < 10:
        i += 1
        if 8 > i > 6:
            break
        print(i)
        
#예제5.
def prim2(number):
    for i in range(2, number):
        if number % i == 0:
            #break
            return(False) #break를 쓰는 것보다 return을 쓰는게 더 강력하다.
    return(True)


#while문예제1. 패스워드 확인
def passwd():
    passwds = '1234567'
    input_data = ''
    while input_data != passwds:
        print('정확한 비밀번호를 입력해주세요.')
        input_data = input('비밀번호를 입력해주세요. : ')
    print('비밀번호가 정확하게 입력되었습니다..')



#while문예제2. 이름입력프로그램
def names():
    input_name = ''

    while input_name != 'q':
        input_name = input("당신의 이름을 입력하세요.'q'를 입력하면 종료합니다. : ")
        print(input_name)
    print('종료합니다.')
'''
input_name = ''
stop = 'quit'

while input_name != stop:
    input_name = input("당신의 이름을 입력하세요.'q'를 입력하면 종료합니다. : ")
    print(input_name)
'''



#while문예제3. 이진수 변환 프로그램
def binary():
    x = int(input('2진수로 변환할 숫자를 입력하세요.:'))
    y = ''

    while x > 0:
        y = str(x%2) + y  # y += str(x%2) => y + str(x%2)라서 맞지 않음
        x //=2
    print('2진수:',y)
    
    
#while문예제4. 예상숫자 맞추기
def up_down():
    x = 50.0
    i = 0

    while i != x:
        i = float(input('예상 숫자를 입력하세요 : '))
        if i < x:
            print('up')
        elif i > x:
            print('down')
    print('정답')
    
    
    
#문자열 예제1. 어절 문제
def sentence():
    stop = 'q'
    sentence = ''
    print('문장을 입력하세요. q입력시 종료합니다.')
    while sentence != stop:
        sentence = input()
        if sentence != stop:
            sentence_num = len(sentence.split())
            print('이 문장은', sentence_num, '어절입니다.')
'''
내 코딩
x = 'q'
y = ''     #빈 문자열 주기 꼭 알아두기!
while y != x:
    y = input('문장을 입력하세요. q입력시 종료합니다.')
    z = y.split()
    if y ==x:
        print('q')
    else:
        print('이 문장은', len(z), '어절입니다.')
'''


# 종합문제. 암호 생성조건
'''
내 풀이
def passwd2():
    passwrd = ''

    for i in range(5):
        passwrd = input('PASSWORD : ')

        if len(passwrd) < 4:
            print('===4글자 이상으로 다시 입력하세요.===')
        elif passwrd.isalnum() == True:
            print('다시 입력해주세요.')
        else:
            while passwrd.isalnum() == False:
                if passwrd.find('!') >= 0:
                    passwrd = passwrd.replace('!','')
                elif passwrd.find('@') >= 0:
                    passwrd = passwrd.replace('@','')
                elif passwrd.find('#') >= 0:
                    passwrd = passwrd.replace('#','')
                elif passwrd.find('$') >= 0:
                    passwrd = passwrd.replace('$','')
                else:
                    print('다시 입력해주세요.')
                    break
            if passwrd.isalnum() == True:
                print('비밀번호가 정상으로 만들어졌습니다.')
                break
            else:
                continue
'''
def passwd2():
    passwd = ''
    alpha_flag = False
    numeric_flag = False
    special_flag = False

    for j in range(5):
        passwd = input('PASSWORD : ')
        if len(passwd) < 4:
            print('4글자이상으로 입력')
        else:
            for i in passwd:
                if i.isalpha():
                    alpha_flag = True
                elif i.isnumeric() :
                    numeric_flag = True
                elif i in '!@#$':
                    special_flag = True
                else:
                    special_flag = False
                    break
            if alpha_flag and numeric_flag and special_flag == True:
                print('비밀번호 설정')
                break
            else:
                print('다시 입력')







