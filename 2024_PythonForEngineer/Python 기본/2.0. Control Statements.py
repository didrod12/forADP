''' # 제어문(Control Statements)
1-1. 조건문 : if, match-case
1-2. 조건 설정 : comparison operator & etc.
2. 반복문 : for, while
3. 예외처리(exception)
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

''' 1-4) Identity Operator : 식별 연산자
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
'''
- 1) is 연산자 : 두 객체가 동일한 객체인지 비교
- 2) == 연산자 : 두 객체의 값이 동일한지 비교
'''
print(list_num == list_num1 , list_num is list_num2) # True, False
print(list_num != list_num1 , list_num is not list_num2) # False, True  

## 4) 불변 객체(Immutable)와 is 연산자
'''
- 불변 객체(Immutable) : int, float, str, tuple, bool, frozenset(고정 집합)
- 불변 객체임에도 파이썬 내부적으로 메모리 효율성을 위해 일부 불변 객체는 "재사용".
'''
a = 1000
b = 1000
print(a == b) # True : 값이 동일
print(a is b) # False : 서로 다른 객체

# !) 작은 정수값(-5 ~ 256)이나 짧은 문자열등은, 내부적으로 자주 사용되어 "캐싱"됨.
c = 100
d = 100
print(c == d) # True : 값이 동일
print(c is d) # True : 서로 같은 객체

''' 1-5) Bitwise Operator : 비트 연산자
- bitwise operators are used to perform bitwise operations on integers.
- 저수준의 비트 조작, 효율적인 계산, 마스킹(masking), 플래그 제어 등에 자주 사용
- 1) & : AND operator, 두 비트가 모두 1인 경우에만 1을 반환
- 2) | : OR operator, 두 비트 중 하나라도 1이면 1을 반환
- 3) ^ : XOR operator, 두 비트가 다를 때만 1을 반환합니다
- 4) ~ : NOT operator, 각 비트를 반전 시킴(1 → 0, 0 → 1)
- 5) << : Left Shift operator, 지정된 비트 수만큼 왼쪽으로 비트 이동시키고 오른쪽에 0을 채움
- 6) >> : Right Shift operator, 지정된 비트 수만큼 오른쪽으로 비트 이동시키고 왼쪽에 0을 채움
'''
# 권한 제어 예시
READ_PERMISSION = 0b0001  # 읽기 권한
WRITE_PERMISSION = 0b0010  # 쓰기 권한
EXECUTE_PERMISSION = 0b0100  # 실행 권한

# 읽기, 쓰기 권한을 부여
permissions = READ_PERMISSION | WRITE_PERMISSION  # 0b0011

# 쓰기 권한이 있는지 확인
has_write = permissions & WRITE_PERMISSION  # 0b0010 (True)

## 2. 반복문(Loop Statements)
'''
1) for 문 
- for [idx] in range(start, end, step) { statements }
- for [obj] in [someList] { statement }
- for [idx],[obj] in [someList] { statement }
2) while : while (condition) { statements }
3) 반복문의 제어문 : break / continue / else
- break : 조건에 따라 반복을 즉시 종료할 때, 사용
- continue :  조건에 따라 현재 반복을 건너뛰고 다음 반복으로 넘어갈 때, 사용
- else : 반복문이 정상적으로 종료된 후 추가로 실행할 코드가 있을 때, 사용
'''
## 1-1) for ~ in | range(start, end, step) 이용
for idx in range(1, 6, 2):
    print(f'{idx}번째 출력')

## 1-2)  for ~ in | list 멤버 이용
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(f'{num}번째 출력')

text = 'Python 텍스트 출력'
for letter in text:
    print(letter)

## 1-3) for ~ in enumerate([list obj])| index와 list 멤버 동시 접근 : enumerate(list) 사용
nc_list = ['박민우', '손아섭', '박건우', '데이비슨', '권희동', '김휘집', '서호철', '박세혁', '천재환', '신민혁']
for idx, player in enumerate(nc_list):
    # if idx != (len(nc_list) - 1):
    if idx != nc_list[-1]:
        print(f'{idx+1}번 타자 : {player}')
    else:
        print(f'선발 투수 : {player}')

## 1-4) for ~ in | 중첩 반복문
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for col in row:
        print(f'{col}', end=' ')
    print() # 줄바꿈 처리

## 2) while 
count = 5
while  0 < count:
    print(f'{count}')
    if count == 1:
        print(f'Play ball!!!')
    count -= 1

isGo = True
question = 'KBO 10개 구단 중 하나의 구단을 입력하세요.'
answer_list = [ 'NC Dinos', '엔씨 다이노스', 'NC', '엔씨 Dinos', 'NC 다이노스']
while isGo:
    answer = input(question)
    if answer in answer_list:
        # break      # break는 해당 줄에서 out. 
        isGo = False #  == break와 유사하나, 아래 줄 수행 후, while 조건에서 out.
    print(f'입력하신 값은 {answer} 입니다.')
    
user_input = ''
while user_input != 'exit':
    user_input = input('명령어를 입력하세요.(exit로 종료) : ')
    
## 3) 반복문의 제어문 : break / continue / else
'''
1) break : breaks out of the current loop
2) continue : skips the current iteration of the loop and moves to the next iteration
3) pass : skips the current iteration of the loop and moves to the next iteration
- pass가 필요한 이유 
→ Python은 들여쓰기로 코드 블록을 구분
→ 함수, 클래스, 조건문, 반복문 등에서 코드 블록이 필요하지만 실제로 그 블록을 비워두고 싶다면 pass를 사용해야 함. 
→ 그렇지 않으면 "구문 오류"가 발생
'''
numbers = [1, 3, 5, 6, 7, 9, 10]
for idx, num in enumerate(numbers):
    if num % 2 == 0:  # 첫 번째 짝수를 찾으면
        print(f"{idx+1}번째 - 첫 번째 짝수: {num}")
        break  # 반복문 즉시 종료 - break시, 반복문 즉시 out
    else:
        print(f"{idx+1}번째 - 짝수를 찾지 못했습니다.")
   
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in numbers:
    if num % 2 != 0:  # 홀수라면
        continue  # 아래 코드를 건너뛰고 다음 반복으로
    print(num)  # 짝수만 출력

numbers = [2, 4, 6, 8, 10]
for num in numbers:
    if num == 7:
        print("7을 찾았습니다.")
        break
else: # 반복문이 정상적으로 종료되었을 때 실행됩니다. break로 인해 종료된 경우에는 실행되지 않음
    print("7이 리스트에 없습니다.")  # 7이 없으므로 else 실행

for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num}은 짝수이므로 continue로 건너뛰기")
        continue  # 첫 번째 짝수는 건너뛴다
    print(f"num: {num}")
else:
    print("반복이 정상적으로 완료되었습니다.")
    
for num in range(0, 11):
    if num > 0:
        pass  # num 가 0보다 크지만, 아무 작업도 하지 않음
    else:
        print("num 는 0 이하 입니다.")

## 3. 예외 처리(Handling Exceptions)
'''
1) try : try block (requires)
2) except : catch block (requires)
3) else : optional catch block 
4) finally : finally block
5) raise : raises an exception - 즉, 의도적으로 예외를 발생시키는 코드(예외를 강제로 발생시킴)

- ex) 아래 확인
try:
    # 예외가 발생할 수 있는 코드
    pass
except [예외종류]:
    # 예외가 발생했을 때 실행할 코드
    pass
else:
    # 예외가 발생하지 않았을 때 실행할 코드
    # try block 내에서 except block 이 실행되지 않았을 때 실행할 코드
    pass
finally:
    # 예외 발생 여부와 상관없이 항상 실행되는 코드
    # try block, except block, else block, finally block 모두 실행할 코드
    pass
'''
try:
    x = 10
    # y = 0 # except : ZeroDivisionError
    y = 2   # else  
    result = x / y
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print("결과는:", result)
finally:
    print("이 메시지는 항상 출력됩니다.")
    
    
try:
    numbers = [1, 2, 3]
    index = 5
    print(numbers[index])
except IndexError:
    print("리스트의 인덱스 범위를 벗어났습니다.")
except Exception as e:
    print(f"다른 예외가 발생했습니다: {e}")
    

## 사용자 정의 예외 예시--------------------------------
class MyCustomError(Exception):
    pass

def process(value):
    if value < 0:
        raise MyCustomError("값이 음수일 수 없습니다.")
    return value

try:
    result = process(-10)
except MyCustomError as e:
    print(f"사용자 정의 예외 발생: {e}")
    
## raise 사용 예시1--------------------------------
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("0으로 나눌 수 없습니다.")
    return x / y

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"예외 발생: {e}")

## raise 사용 예시2--------------------------------
class NegativeNumberError(Exception):
    """음수일 때 발생하는 예외"""
    pass

def process_number(number):
    if number < 0:
        raise NegativeNumberError("음수는 허용되지 않습니다.")
    return number

try:
    result = process_number(-5)
except NegativeNumberError as e:
    print(f"예외 발생: {e}")