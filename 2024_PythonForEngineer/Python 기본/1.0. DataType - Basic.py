''' # Python 자료형

1. 기본 자료형 : 불린(bool), 정수(int), 실수(float), 복소수(complex) 등
2. 컨테이너 자료형 : 리스트(list), 튜플(tuple), 딕셔너리(dict), 집합(set) 등
3. 문자열 : 유니코드 문자열(str) 및 ANSI 문자열(bytes) 등의 문자열 등

## Container vs. flat 

1) Container : Data structure that contains multiple values.
- list, tuple, set, dict

2) Flat : Data structure that contains only one value.
- int, float, str, bytes, bytearray, memoryview, etc.
'''
#region 1. 기본 자료형(Basic Data Types)
# 1) 논리형(boolean)
isCheck = True
type(isCheck)   # type of check

# 2) 정수(integer)
num_int = 123
type(num_int)   # type of num_int

# 3) 실수(float)
num_float = 1.23
type(num_float)   # type of num_float

# 4) 복소수(complex)
num_complex = 1 + 2j
type(num_complex) # type of num_complex

#endregion

#region 2. 컨테이너 자료형(Container Data Types)

# 1) List (Vector || Array) : Sequence Container
''' - List is a collection which is ordered and changeable. Allows duplicate members.
    - Elements in a list are indexed, mutable, and can be of different data types.
    - Elements in a list can be accessed by their index.    
'''
ex_list = [1, 'Min woo Park', 3, True, 5.0 , 'Captine' , True]
type(ex_list)   # type of ex_list

ex_list[2]
ex_list[2] = 'Changed'
print(ex_list)

# 2) Tuple (Immutable Sequence) : Read ONLY - Sequence Container
ex_tuple = (1, 'Min woo Park', 3, True, 5.0, True, 'Captain')
type(ex_tuple)   # type of ex_tuple

ex_tuple[2]
ex_tuple[2] = 'Unchanged'   # error : tuple is immutable
print(ex_tuple)

# 3) Dictionary (map || Hash Table) : Associative Array - Key-Value Pairs
''' - Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
    - Elements in a dictionary can be accessed by their key.
    - Elements in a dictionary are indexed, mutable, and can be of different data types. 
'''
ex_dict = {'name': 'Min woo Park', 'age': 31, 'number':2}
type(ex_dict)   # type of ex_dict   

ex_dict['age']

# 4) Set (Unordered Collection of Unique Elements) : Associative Array - Key-Value Pairs        
''' - Set Unordered Collection of Unique Elements
    - Set is an unordered collection of unique elements.
    - Elements in a set are indexed, mutable, and can be of different data types.
'''
ex_set = {1, 'Min woo Park', 3, True, 5.0}
type(ex_set)   # type of ex_set

test = ex_set.pop()  # pop(): remove an arbitrary element from the set
print(ex_set)
#endregion

#region 3. 문자열(String)
''' 
 - 1 character string in Python can be declared either as single quotes (' ') or double quotes (" ").
 - 고정 폭, 고정 길이의 Sequences of characters & Sequences Containers
 - 1) 문자열(str) : 2bytes 크기로 표시
 - 2) ANSI 문자(bytes) : 1byte 크기로 표시
'''
word = 'Hello'
type(word)   # type of string

b_word = b'Hello'
type(b_word)   # type of bytes
#endregion

