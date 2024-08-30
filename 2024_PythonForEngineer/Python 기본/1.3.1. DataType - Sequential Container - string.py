''' # 순차 컨테이너(Sequential Container type)
- 모든 요소를 특정 순서대로 저장한 컨테이너 ⇒ 요소를 선형적 순차열(Linear Sequence)에 저장
- 요소 저장 위치와 요소 값은 서로 독립적, also 서로 다른 데이터 타입을 담을 수 있다.
- list, tuple, string 등이 있다.

3. 문자열(string) 
- Sequence ⇒ Immutable sequence
- 서로 다른 데이터 타입(str, bytes), 중복 가능
1) str : immutable sequence of Unicode characters
2) bytes : immutable sequence of 8-bit bytes 
 - bytes는 텍스트 파일을 저장할 때, encoding된 상태를 표현하기 위해 주로 사용
'''
# 1) 유니코드 문자열(str) : str----------------------------------------------------------------
str_word = 'word' # one line of text
str_sentence = '''sentence  
                   string''' # multiline string
str_escape = 'Hello, \nWorld!' # newline character
print(str_word, str_sentence)                  
print(str_escape)

# 2) 바이트 문자열(byte) : byte----------------------------------------------------------------
byte_work = b'word' # one byte of binary data
print(byte_work)

''' ## raw 리터럴(raw literal)  -------------------------------------------------------- 
- raw string literal : escape sequences are not processed
- ex) r'C:\Users\username\Documents\project' : backslash characters are not, just add a 'r' before the opening quote

'''
# str_path = 'C:\Users\username\Documents\new-project' # Error
str_path1 = 'C:\\Users\\username\\Documents\\new-project' # normal string literal(using backslash characters)
str_path2 = r'C:\Users\username\Documents\new-project' # raw string literal
print(str_path1)
print(str_path2)

''' ## 형변환(Convert)  -------------------------------------------------------- 
- int() : str to(→) int
- str() : int to(→) str
'''
int_one = 1
str_one = str(int_one)
type(str_one), type(int_one)

str_two = '2'
int_two = int(str_two)
type(str_two), type(int_two)

''' ## 연산  -------------------------------------------------------- 
- + : each charters be concatenated using the + operator
- * : charters can be multiplied using the * operator
'''
header = 'Header'
body = 'Body'
tail = 'Tail'
str_combined = header + '-' + body + '-' + tail
print(str_combined)
print("="* 50)
print('만세! ' * 3)

''' ## 인덱싱(Indexing) & 슬라이싱(Slicing) -------------------------------------------------------- 
- indexing is used to access the value of an element in a string.
- i starts from 0 to n-1 where n is the length of the list.
- list, tuple, str, etc.
- ex) x[i:j] : x[i] to x[j-1] (inclusive)  -> Accessing elements in a range

'''
str_sentence = 'Hello, World!'
str_sentence[0], str_sentence[1], str_sentence[2], str_sentence[3], str_sentence[4]
str_sentence[-1] # accessing the last character of the string
str_sentence[0:5]  # accessing elements in a range, from index 0 to 4
str_sentence[6:]  # accessing elements in a range, from index 6 to the end
str_sentence[::-1] # reverse the string
str_sentence[0] = 'Y' # Error! - modifying the first character of the string is not allowed

''' ## 문자열 포맷팅(formatting) -------------------------------------------------------- 
- case1 : C style - '%' expression ⇒ 'Hello, %s!' % 'World'
- case2 : string.format() - 'My {} is {}'.format('age', age) ⇒ 'Hello, {value}'
- case3 : f-string - f'{expression}' ⇒ f'Hello, { value }' # python 3.6+ only
- case4 : template literals - Template('My name is $name and I am $age years old.') ⇒ for security?
'''
# case1 : C style - '%' 연산자----------------------------------------------------------------
str_format1 = 'I have %d apples. and I have a %s' % (5, 'car') # 1개이면, 괄호 없이 씀
print(str_format1)
print('%s 라는 %d글자에~' % ('"뭐해?"', 2))

# case2 : string.format()----------------------------------------------------------------
str_format2 = '{}이 넘기 전에 {}을 할런지...\nGive it to me'.format(30, '결혼')
print(str_format2)
print('{cake} : ${price}'.format(price=14.50, cake='Tiramisu Cake'))

# case3 :  f-string - f'{expression}'----------------------------------------------------------------
meal = '식사'
none = '없어.'
juice = '음료'
str_format3 = f'{meal}는 {none} 배고파도 \n{juice}는 {none} 목말라도'
print(str_format3)

# case4 : template literals----------------------------------------------------------------
from string import Template
feeling = 'shy'
verb = 'wait'
template = Template("I'm super $feeling, super $feeling. But $verb a minute.")
song =  template.substitute(feeling='shy', verb='waits')
print(song)

''' ## 기타 Function-------------------------------------------------------- 
- append() : Adds an element at the end of the list
- insert() : Adds an element at the specified index
- delete() : Removes an element at the specified index
- x[i] = 'some value' : Updates the value of an element at the specified index
'''
str_high = "Didn't have a dime but I always had a vision. \nAlways had high, high hopes"

len(str_high)
str_high.count('high') # count the number of occurrences of the specified value
# !) find, rfind, index, rindex : return the index of the first, last, specified value ⇒ also can be used with a start and end index(범위 지정 가능)
str_high.find('a') # find the index of the first occurrence of the specified value
str_high.rfind('a') # find the index of the last occurrence of the specified value
str_high.index('i') # find the index of the specified value, from the left
str_high.rindex('i') # find the index of the specified value, from the right

str_high1 = str_high.replace('high', 'low') # replace the specified value with another value, returns the new string
str_high1 = str_high.replace('high', 'low', 1) # replace the specified value with another value, only replaces the first occurrence(1)

separator ='/'
str_high1 = "Had to have high, high hopes for a living \nShooting for the stars when I couldn't make a killing"
str_high2 = separator.join(str_high1) # join the elements of the list into a string, with a specified separator
str_fruits = '-'.join(['apple', 'banana', 'cherry']) # join the elements of the list into a string

separator = '.'
list_high = str_high.split(separator) # split the string into a list
len(list_high) # number of elements in the list

str_showman = '         this is me.     '; len(str_showman)
str_showman.strip(), len(str_showman.strip()) # remove leading and trailing whitespaces
str_showman.lstrip(), len(str_showman.lstrip()) # remove leading whitespaces (문자열 앞의 공백 제거)
str_showman.rstrip(), len(str_showman.rstrip()) # remove trailing whitespaces(문자열 끝의 공백 제거)
str_showman.upper(), str_showman.lower()  # convert to lowercase or uppercase
