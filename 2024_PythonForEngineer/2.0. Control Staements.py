''' # 제어문(Control Statements)

1-1. 조건문 : if, match-case
1-2. 조건 설정 : comparison operator & etc.
2. 반복문 : for, while
3. 분기문 : break, continue, pass
4. 예외처리(exception)
'''
## 1-1. 조건문(Condition Statements)
'''
1-1) if : if (condition) { statements }
1-2) if-else : if (condition) { statements } else { statements }
1-3) if-elif-else : if (condition1) { statements1 } else if (condition2) { statements2 } else { statements3 }

2) match-case : match (value) { case value1: statements1; case value2: statements2;...} # python 3.10+
'''
one = 1
if(one == 1):
    print('one is 1')
else:
    print('one is not 1')

something = input('enter something : ')

import re
if(something.isdigit()):
    print('You entered a number.')
# elif(something.isalpha()): # isalpha() : isalpha() checks if all the characters in the string are alphabetic(using unicode, so it can handle both English and Korean characters)
elif(re.fullmatch(r'[a-zA-Z]+', something)): # so, re.fullmatch is more accurate than isalpha()
    print('You entered a alphabet.')
elif(something.isalnum()):
    print('You entered a number and alphabet.')
elif(re.fullmatch(r'[가-힣]+', something)):
    print('You entered a hangul.(한국어)')
else:
    print('You entered some other letter.')

## 1-2. 조건 설정(Condition Setting) - comparison operator, etc.
''' 1-1) Comparison Operator : 비교 연산자
- comparison operators are used to compare two values and determine their relationship. 
- Examples : a > b, a < b, a == b, a!= b, a >=
- 1) == : equal to
- 2) != : not equal to
- 3) > : greater than
- 4) < : less than
- 5) >= : greater than or equal to
- 6) <= : less than or equal to
'''
number1, number2 = input('Enter two numbers separated by space : ').split()
if number1 == number2:
    print('They are equal.')
elif number1 > number2:
    print('Number1 is greater than number2.')
elif number1 < number2:
    print('Number1 is less than number2.')
else:
    print('You entered an incorrect number of numbers.')
    
word1, word2 = input('Enter two words separated by space : ').split()
if word1 == word2:
    print('They are equal.')
elif word1 != word2:
    print('They are not equal.')

height_me, height_other = input('Enter two heights separated by space : ').split()
if int(height_me) == int(height_other):
    print('They are same height.')
elif int(height_me) >= int(height_other):
    print('Height of me is higher than the other.')
elif int(height_me) <= int(height_other):
    print('Height of other is higher than me.')
else:
    print('You entered an incorrect height.')
    
''' 1-2) Logical Operator : 논리 연산자
- logical operators are used to combine boolean values. ⇒ "Combine boolean"
- examples : a and b, a or b, not a
- 1) and : logical AND (true if both operands are true)
- 2) or : logical OR (true if either operand is true)
- 3) not : logical NOT (true if the operand is false)
'''
fruits = ['blueberry', 'banana', 'cherry', 'melon', 'lemon']*4
len(fruits)

import random
for idx in range(5):
    random_fruit1, random_fruit2 = random.choice(fruits), random.choice(fruits)
    if((random_fruit1 == random_fruit2) and idx%2 == 0):
        print('홀수 : %s' % random_fruit1)
    elif(not(random_fruit1 == random_fruit2)):
        print('불일치 : %s' % random_fruit1, random_fruit2)
    elif((random_fruit1 == random_fruit2) or idx%2 != 0):
        print('일치 O 또는 짝수 과일: %s' % random_fruit1, random_fruit2)

''' 1-3) Membership Operator(sequence membership operator) : 멤버 연산자
- membership operators are used to check if a value exists in a sequence.
- examples : a in b, a not in b
-1) in : sequence/object membership (true if the value/object is in the sequence)
-2) not in : sequence/object membership (true if the value/object is not in the sequence)

'''
## 1) List membership operators-------------------------------
list_nc_lineup = ['박민우', '손아섭', '박건우', '데이비슨', '권희동', '서호철', '박세혁', '김주원', '천재환']

for idx in range(5):
    member = input('NC 라인업 입력: ')    
    trials = idx + 1
    if member in list_nc_lineup:
        print('%d 시도 - NC 라인업에 %s가 있습니다.' %(trials, member))
    else:
        print('%d 시도 - NC 라인업에 %s가 없습니다.' % member)

for idx in range(3):
    member = input('NC 라인업 입력: ')    
    trials = idx + 1
    if member not in list_nc_lineup:
        print(f'{trials}번째 시도 - NC 라인업에 {member}이/가 없습니다.')
    elif member in list_nc_lineup:
        print(f'{trials}번째 시도 - NC 라인업에 {member}이/가 있습니다.')

## 2) string membership operators-----------------------------
str_nc_lineup ='박민우, 서호철, 데이비슨, 권희동, 김성욱, 김휘집, 천재환, 김형준, 김주원'
some_day = '2024.08.04'

for idx in range(3):
    member = input('NC 라인업 입력: ').strip()
    if member in str_nc_lineup:
        print(f'{idx+1}번째 시도 - {some_day}, NC 라인업에 {member}이/가 있습니다.')
    elif member not in str_nc_lineup:
        print(f'{idx+1}번째 시도 - {some_day}, NC 라인업에 {member}이/가 없습니다.')

## 3) tuple membership operators------------------------------
tuple_nc_pitcher = ('목지훈', '이준호', ' 임정호', '김재열', ' 김태현', '전루건', '류진욱')
some_day = '2024.08.04'

for idx in range(3):
    member = input('NC 라인업 입력: ').strip()
    if member in tuple_nc_pitcher:
        print(f'{idx+1}번째 시도 - {some_day}, NC 등판 투수에 {member}이/가 있습니다.')
        if member == '이준호':
            print(f'{some_day}, {member}가 승리 투수입니다.')
    elif member not in tuple_nc_pitcher:
        print(f'{idx+1}번째 시도 - {some_day}, NC 등판 투수에 {member}이/가 없습니다.')

## 4) dictionary membership operators-------------------------
list_baseball_position = ['1B', '2B', '3B', 'SS', 'RF', 'CF','LF','Catcher','Pitcher']
list_nc_members =['데이비슨', '박민우', '서호철', '김주원', '박건우', '김성욱', '권희동', '김형준', '하트']

# i) zip(keys, values), pairs elements from the two lists into tuples
# ii) dict() function to convert these tuples into a dictionary
dict_nc_position =  dict(zip(list_baseball_position, list_nc_members))

for idx in range(3):
    position = input('Position 입력 : ').strip()
    if position in dict_nc_position:
        print(f'{idx+1}번째 시도 - NC에서 {dict_nc_position[position]}의 주 포지션 {position}입니다.')
    elif position not in dict_nc_position:
        print(f'{idx+1}번째 시도 - 입력하신 {position}은 정해진 용어와 상이합니다.')

dict_grades = {'Korean': 'A+', 'Math':'A', 'Physics':'A-', 'English':'B'}
if 'A' in dict_grades.values():
    print(f'"A" 성적이 있긴 함.')

## 5) set membership operators--------------------------------
set_colors = {'white', 'black', 'gold','navy','mint'}

for idx in range(3):
    color = input('Color 입력 : ').strip()
    if color in set_colors:
        print(f'{idx+1}번째 시도 - {color}가 set에 포함되어 있습니다.')
    elif color not in set_colors:
        print(f'{idx+1}번째 시도 - {color}가 set에 포함되어 있지 않습니다.')

'''1-4) Identity Operator : 식별 연산자
- identity operators are used to compare the memory locations of two objects.
- examples : a is b, a is not b
- 1) is : object identity (same memory location)
- 2) is not : object identity (different memory location)

'''
list_num = [1, 2, 3]
list_num1 = list_num
list_num2 = [1, 2, 3]
print(list_num, list_num1, list_num2)

## 1) is 
print(list_num is list_num1) # True, 동일한 객체 참조(same memory location)
print(list_num is list_num2) # False, 다른 객체 참조(different memory location)

## 2) is not
print(list_num is not list_num1) # False, 동일한 객체 참조
print(list_num is not list_num2) # True, 다른 객체 참조

## 3) is vs. == 
print(list_num == list_num1 , list_num is list_num2) # True, False
print(list_num != list_num1 , list_num is not list_num2) # False, True  

## 4) 불변 객체(Immutable)와 is 연산자
'''
-  불변 객체(Immutable) : int, float, str, tuple, frozenset(고정 집합)
'''


'''
1-5) Bitwise Operator : 비트 연산자
- bitwise operators are used to perform bitwise operations on integers.
'''


## 2. 반복문(Loop Statements)
'''
1) for & for in
1-1) for (initialization; condition; increment/decrement) { statements }
1-2) for in range(start, end, step) { statements }
2) while : while (condition) { statements }

'''

## 3. 분기문(Branch Statements)
'''
1) break : breaks out of the current loop
2) continue : skips the current iteration of the loop and moves to the next iteration
3) pass : skips the current iteration of the loop and moves to the next iteration

'''

## 4. 예외 처리(Handling Exceptions)
'''
1) try : try block (requires)
2) except : catch block (requires)
3) else : optional catch block 
4) finally : finally block
5) raise : raises an exception

'''