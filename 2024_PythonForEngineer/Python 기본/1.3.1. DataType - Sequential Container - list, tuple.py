''' # 순차 컨테이너(Sequential Container type)
- 모든 요소를 특정 순서대로 저장한 컨테이너 ⇒ 요소를 선형적 순차열(Linear Sequence)에 저장
- 요소 저장 위치와 요소 값은 서로 독립적, also 서로 다른 데이터 타입을 담을 수 있다.
- list, tuple, string 등이 있다.

1. 리스트(List) : list
- Sequence, index를 사용 ⇒ 가변길이 시퀀스 자료형(mutable sequence)
- 서로 다른 데이터 타입, 중복 가능
- like a array

2. 튜플(Tuple) : tuple
- read-only : elements cannot be changed after creation 
- Sequence. index를 사용 ⇒ 불변한 시퀀스 자료형(immutable sequence)
- 서로 다른 데이터 타입, 중복 가능

'''
# 1. 리스트(list) : list----------------------------------------------------------------
list_one = [1, '박민우', '2', True, {'Position' : '2B'}]
list_two = [2, '손아섭', '31', True, {'Position' : 'DH'}]
list_three = [3, '박건우', '37', True, {'Position' : 'RF'}]
list_empty = []
type(list_one), type(list_two), type(list_three)
type(list_empty)  # type of list_empty == <class 'list'>

# 2. 튜플(Tuple) : tuple----------------------------------------------------------------
tuple_one = (1, '박민우', '2', True, {'Position' : '2B'})
tuple_two = (2, '손아섭', '31', True, {'Position' : 'DH'})
tuple_three = (3, '박건우', '37', True, {'Position' : 'RF'})
tuple_empty = ()
type(tuple_one), type(tuple_two), type(tuple_three)
type(tuple_empty)  # type of tuple_empty == <class 'tuple'>
tuple_three[1] ='천재환'  # modifying tuple element is not allowed

''' ## 인덱싱(Indexing) & 슬라이싱(Slicing) -------------------------------------------------------- 
- indexing is used to access the value of an element in a list.
- i starts from 0 to n-1 where n is the length of the list.
- list, tuple, str, etc.
- ex) x[i:j] : x[i] to x[j-1] (inclusive)  -> Accessing elements in a range

'''
# 1. 리스트(list) : list----------------------------------------------------------------
list_one[1], list_two[1], list_three[1]  # Accessing element in list_one, list_two, list_three
list_one[-1], list_two[-1], list_three[-1]  # Accessing last element in list_one, list_two, list_three
len(list_one), list_one[1:3]  # slicing list_one from index 1 to index 2 (exclusive)
list_one[1:-1]  # until the "second" last element

# 2. 튜플(Tuple) : tuple----------------------------------------------------------------
tuple_one[1], tuple_two[1], tuple_three[1]
tuple_one[-1], tuple_two[-1], tuple_three[-1]
len(tuple_one), tuple_one[1:3]  # slicing list_one from index 1 to index 2 (exclusive)
tuple_one[1:-1]  # until the "second" last element

''' ## 형변환(Convert)  -------------------------------------------------------- 
- list() : tuple to(→) list
- tuple() : list to(→) tuple
'''
tuple_number = ('one', 'two', 'three', 'four', 'five')
list_number = list(tuple_number)
print(list_number)

list_number = [1, 2, 3, 4, 5]
tuple_number = tuple(list_number)
print(tuple_number)

''' ## 연산  -------------------------------------------------------- 
- + : each list and tuple can be concatenated using the + operator
- * : list and tuple can be multiplied using the * operator

'''
# 1. 리스트(list) : list----------------------------------------------------------------
list_table_setter = list_one + list_two # concatenate list_one, list_two
str_table_setter = list_one[1] + ' and ' + list_two[1]  # concatenate string and elements 
type(list_one[0]*2)  # integer
list_three_multi =  list_three*2  # multiply list_three by 2

# 2. 튜플(Tuple) : tuple----------------------------------------------------------------
tuple_table_setter = tuple_one + tuple_two # concatenate tuple_one, tuple_two
str_table_setter = tuple_one[1] + ' and ' + list_two[1]  # concatenate string and elements 
type(tuple_one[0]*2)  # integer
tuple_three_multi =  tuple_three*2  # multiply tuple_three by 2
tuple_three_multi[1] = '데이비슨'  # modifying tuple element is not allowed

''' ## List - 요소 추가 / 변경 / 삭제 -------------------------------------------------------- 
1. 리스트(list) : list
- append() : Adds an element at the end of the list
- insert() : Adds an element at the specified index
- remove() : Removes an element at the specified value, not its index
- x[i] = 'some value' : Updates the value of an element at the specified index

2. 튜플(Tuple) : tuple
- read-only : elements cannot be changed after creation
'''
# 리스트(list) : list----------------------------------------------------------------
list_something = ['test', 1, 2, 3, 4, 5, 6, 7, 8, 9,True, {'key' : 'value'}]
list_something.append('new!') # append an element at the end of the list, so if you want to add at a specific index, use insert()
list_something.insert(0, '0 index')  # insert an element at the specified index
list_something.insert(-1, '-1 index')  # !) -1 index is the second last index

list_something.insert(0, 'test')  
list_something.append('test')  
list_something.remove('test')  # remove an element from the list using the value, not its index & removes the first occurrence
list_something[1] = '1 index'  # update the value of an element at the specified index
print(list_something)

''' ## Tuple - 언패킹(Unpacking)  -------------------------------------------------------- 
- unpacking. Unpacking allows us to assign multiple values from a tuple into multiple variables.
- starred expression : *tuple_name unpacks the elements of the tuple into the variables in the list
'''
# 튜플(Tuple) : tuple----------------------------------------------------------------
one, two, three, four = ('one', 'two', 'three', 'four') #tuple unpacking
t, h, i, s = 'this' # string unpacking
full_name = "박건우"
last_name, *first_name = full_name  # unpacking full name into last_name('박') and first_name(['건','우'])
type(last_name), type(first_name)

''' ## 기타 Function -------------------------------------------------------- 
- append() : Adds an element at the end of the list
- insert() : Adds an element at the specified index
- delete() : Removes an element at the specified index
- x[i] = 'some value' : Updates the value of an element at the specified index
'''
# 1. 리스트(list) : list----------------------------------------------------------------
list_something.clear() # remove all items from the list
list_something = ['test', 1, 2, 3, 4, 5, 6, 7, 8, 9,True, {'key' : 'value'}]
print(list_something)

list_something.index('test')  # find the index of the first occurrence of the specified value
list_something.append('test')
list_something.count('test') # count the number of occurrences of the specified value
list_something.pop() # remove the last item from the list and return it

list_integers = [1, 2, 3, 4, 5]
list_integers.sort() # sort the elements of the list in ascending order
list_integers.sort(reverse=True) # sort the elements of the list in descending order
list_integers.reverse() # find the index of the last occurrence of the specified value

list_something.reverse() # find the index of the last occurrence of the specified value
list_something.extend('test2') # extend the list by appending elements from the iterable => concatenate string [t,e,s,t,2]
list_copy = list_something.copy() # return a shallow copy of the list => values of the list are copied, not the objects
print(list_something == list_copy)  # True, compare the values of the list
print(list_something is list_copy)  # False, compare the objects of the list

list_copy = ['clear copy']
print(list_something == list_copy)  # False, compare the values of the list

# 2. 튜플(Tuple) : tuple----------------------------------------------------------------
tuple_something = ('test', 1, 2, 3, 4, 5, True, {'key': 'value'})
tuple_something.count('test')  # count the number of occurrences of the specified value
tuple_something.index('test')  # find the index of the first occurrence of the specified value