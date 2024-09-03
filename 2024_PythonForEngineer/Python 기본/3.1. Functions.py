''' # Python 함수(Functions)

1. 함수 정의
- 키워드 : def [함수명] - 함수명은 스네이크 표기(Snake Case)
- 함수에서 사용하는 변수는 "local scoped variables" 이다.
- !) 함수내에서 함수를 정의해서 사용할 수 있다! 내부함수에서 외부함수의 변수를 마치 전역변수처럼 사용할 수 있다.
<code>
    def [함수명](parameters...):
        - 구현
        reslult = some_value
        return some_value
</code>

2. Immutable  & Mutable 타입
- 1) Immnutable :불린(bool), 정수(int), 실수(float), 복소수(complex), 튜플(tuple), 문자열(str) 등
-- * Call by value : 함수내에서 인자값을 변경하더라도, 호출에 사용한 인자값이 변경되지 않는다. (즉, 내부 변화가 외부 호출에 영향을 주지 않는다.)
- 2) Mutable : 리스트(list), 딕셔너리(dict), 집합(set) 등
--  Call by reference : 함수내에서 인자값이 변경되면, 호출에 사용된 인자값도 변경된다.(즉, 내부 변화가 외부 호출에 영향을 준다.)
'''
# 1) Call by Value
def add(a,b):
    a = 100 # Call by value
    b = 200
    return a + b

def add(str1, str2):
    str1 += "/" # Call by value
    str2 += "\n~~~~~~"
    return str1 + str2

def add(tup1, tup2):
    tup1 += tup1  # Call by value
    tup2 += tup2
    return tup1 + tup2

def printSomething(a, b, c):
    return print(a, b, c)

a = 1
b = 2
c = add(a,b)
printSomething(a,b,c)

str1 = '오늘도'
str2 = '내일도'
str3= add(str1,str2)
printSomething(str1,str2,str3)

tup1 = ('1번', '박민우')
tup2 = ('2번', '손아섭')
tup3 = add(tup1,tup2)
printSomething(tup1, tup2, tup3)

# 2) Call by reference
def append(a,b):
    c = []  # Call by reference
    a.append(100)
    b.append(200)
    c.append(a)
    c.append(b)
    return c 

lst1 = [1,3]
lst2 = [2,4]
lst3 = append(lst1, lst2)

print(lst1, lst2, lst3)  

def computeProps(club, pleyer1, player2):
    club = (pleyer1, player2)
    return club

pl1 = '박건우'
pl2 = '박민우'
pl3 = '손아섭'
pl4 = '권희동'
club = 'NC 다이노스'
players = computeProps(club, pl1, pl2)
건우, 민우 = computeProps(club, pl1, pl2)  # unpack
(아섭, 희동) = computeProps(club, pl3, pl4)  # unpack  

print(f'players - {players}') 
print(f'player1 - {건우} / player2 - {민우}') 
print(f'player3 - {아섭} / player4 - {희동}') 

# 3) Defulat 인자 지정
def setDefulat(str1, str2, sep='/'):
    return str1 + sep + str2

str1 = '1분류'
str2 = '2분류'

print(setDefulat(str1, str2))  # sep default value '/'
print(setDefulat(str1, str2, '&'))  # sep assign default value

# 4) *args 와 **kwargs
# - 인자 개수가 정해지지 않았을 때, 사용
# - 1) *args : 여러개의 인자를 튜플로 묶어서 args 변수를 함수로 전달. (즉, args  = (a,b,c, ...))
# - !) 단, *args 변수는 인자들의 뒤에 와야한다.(always!)
# - 2) **kwargs : Keyword arguments, 여러 인자를 딕셔너리로 묶어서 전달. (즉, kwargs ={a=1,b=2,c=3, ...})
# - !) 단, **kwargs 변수는 *args보다 뒤에 와야한다. (즉, 사용할 경우, 맨 뒤에!)
def sum_args(*args): 
    result = 0
    for num in args:
        result += num
    return result
sum1 = sum_args(1,9,8,2,5)
print(sum1)

def sum_kwargs(**kwargs):
    result = 0
    for key, value in kwargs.items():
        result += value
    return result 
sum2 = sum_kwargs(a=1, b=2, c=3)  
print(sum2)

def sum_func(x, y, *args,**kwargs):
    result = x + y
    print(f'sum_func : x({x}) + y({y}) = {result}')
    for num in args:
        result += num
        print(f'sum_func : x({x}) + y({y}) + num({num}) = {result}')
    for key, value in kwargs.items():
        result += value 
        print(f'sum_func : x({x}) + y({y}) + num({num}) + value({value})= {result}')
    return result


x = 100
y = 1000
a = 2
b = 31
c = 37
d = 24
e = 36
f = 44
g = 5
h = 38

result = sum_func(x,y,10,40,50,60,100,90, one=a, two=b, three=c, four=d, five=e, six=f, seven=g, eight=h)
print(f'sum_func : x({x}) + y({y}) + ... = {result}')

# 5) 함수내 함수 
def outer_function(text):
    def inner_function():
        print(text)  # 외부 함수의 변수에 접근
    inner_function()  # 내부 함수 호출

outer_function("Hello, Python!")


def outer_function(x):
    def inner_function(y):
        return x + y  # 외부 함수의 변수 x에 접근
    return inner_function

# 클로저(Closure) 생성 : 함수를 반환하는 함수를 호출하고, 그 결과를 변수에 할당하는 방식
add_five = outer_function(5) # add_five가 반환되는 함수인 inner_function을 가리키게 됨. →  여기서 add_five는 outer_function(5)시의 상태를 "기억"하고 있음
add_five == outer_function(5)  # False
add_five is outer_function(5)  # False
print(add_five(10))