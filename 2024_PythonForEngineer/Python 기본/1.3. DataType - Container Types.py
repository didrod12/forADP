''' # 컨테이너(Container)
- 자료형에 상관없이 여러 개의 데이터를 저장 가능 (즉, n개 이상의 데이터를 저장)

1. 순차 컨테이너(Sequential Container)
- 데이터가 특정 순서(순차적)로 배열된 컨테이너
- Sequence, index를 사용 ⇒ Ordered & Duplicates allowed sequence
- 서로 다른 데이터 타입
- ex) list, tuple, string, bytes, bytearray, etc.

2. 연관 컨테이너((Associative Container)
- 데이터가 특정 키와 연관되어 저장되는 컨테이너
- key-value pair를 사용 ⇒ Unordered & No Duplicates allowed sequence
- 키(key)와 값(value)처럼 관련있는 데이터를 하나의 쌍으로 저장하는 컨테이너
- default 정렬 기준으로 자료 입력과 동시에 모든 자료가 정렬됨 - binary search, hash table
- 이진 탐색 트리(balanced binary search tree)나 해시 테이블(hash table)을 이용하여 구현
- ex) set, dict

'''
# Python 3.3 이상에서는 collections 내의 많은 추상 기본 클래스(예: Container, Iterable, Sequence 등)가 collections.abc 모듈로 이동
from collections import *
from collections.abc import Container

# issubclass(x,y) -> bool: x is a subclass of y (y 클래스를 x가 상속했는 지 확인)--------------------------------------------------------
int_is_container = issubclass(int, Container)
float_is_container = issubclass(float, Container)
complex_is_container = issubclass(complex, Container)
bool_is_container = issubclass(bool, Container)
int_is_container, float_is_container, complex_is_container, bool_is_container   # All False

# Container : Iterable - 반복(iteration)할 수 있는 객체---------------------------------------------------------------------------------
set_is_container = issubclass(set, Container)
dict_is_container = issubclass(dict, Container)
set_is_container, dict_is_container # All True

list_is_container = issubclass(list, Container) # sequence
tuple_is_container = issubclass(tuple, Container) # sequence
str_is_container = issubclass(str, Container) # sequence
list_is_container, tuple_is_container, str_is_container   # All True

# Functions for Container-------------------------------------------------------------------------------------------------------------
## 0. dict - chainmap : apply a function to each item of an iterable (returning a new list)
# TODO : https://docs.python.org/ko/3.12/library/collections.html#deque-objects 확인 후, 작성하기


## 1. tuple - namedtuple : 튜플의 각 위치에 의미를 부여 & 위치 인덱스 대신 이름으로 필드에 액세스하는 기능을 추가
tuple_names = ('박민우', '손아섭', '박건우', '데이비슨', '권희동', '서호철', '김휘집', '박세혁', '천재환', '하트')
tuple_line_up = namedtuple('NC_LineUp', tuple_names)
lineUp = tuple_line_up('박민우', '손아섭', '박건우', '데이비슨', '권희동', '서호철', '김휘집', '박세혁', '천재환', '하트')
print(tuple_line_up[0]) # Class 
print(lineUp[0])   # instance
no1, no2, no3, no4, no5, no6, no7, no8, no9, p = lineUp
print(no1, no2, no3, no4, no5, no6, no7, no8, no9, p)

## 2. literal - Counter : dict subclass for counting hashable objects
list_colors = ['red', 'blue', 'green', 'blue', 'blue', 'green', 'green','purple','blue']
Counter(list_colors)

tuple_colors = tuple(list_colors)
Counter(tuple_colors)   

str_someword = ' abcdeabcdabcaba '
Counter(str_someword)   # blank is also counted

cnt = Counter()
cnt.update(list_colors) # add elements from list to counter
print(cnt)
cnt.update(list_colors) # add elements from list to counter
print(cnt) # 2 repeated list_colors -> Counter({'blue': 8, 'green': 6, 'red': 2, 'purple': 2})

cnt.most_common(3) # return the n most common elements and their counts ⇒ 3일 경우, [('blue', 8), ('green', 6), ('red', 2)]

del cnt['blue'] # remove one element 
cnt.most_common(3) # ⇒ [('green', 6), ('red', 2), ('purple', 2)]

cnt.subtract(list_colors) # remove elements from cnt (cnt - list_colors)

cnt.clear() # remove all elements from the counter
cnt.update(list_colors)
cnt.total() # return the total count of elements in the counter

