''' # 순차 컨테이너(Sequence Container type)
- 모든 요소를 저장한 순서대로 저장하는 컨테이너 ⇒ 요소를 선형적 순차열(Linear Sequence)에 저장
- 요소 저장 위치와 요소 값은 서로 독립적, also 서로 다른 데이터 타입을 담을 수 있다.
- list, tuple 등이 있다.

1. 리스트(List) : list
- Sequence, index를 사용
- 서로 다른 데이터 타입
- like a array

2. 튜플(Tuple) : tuple
- Sequence. index를 사용
- 서로 다른 데이터 타입
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

''' ## 인덱싱(Indexing)  -------------------------------------------------------- 
- indexing is used to access the value of an element in a list.
- i starts from 0 to n-1 where n is the length of the list.
- list, tuple, str, etc.
- ex) x[i:j] : x[i] to x[j-1] (inclusive)  -> Accessing elements in a range

'''
# 1. 리스트(list) : list----------------------------------------------------------------
list_one[1], list_two[1], list_three[1]  # Accessing element in list_one, list_two, list_three
list_one[-1], list_two[-1], list_three[-1]  # Accessing last element in list_one, list_two, list_three
len(list_one), list_one[1:3]  # slicing list_one from index 1 to index 2 (exclusive)
list_one[1:-1]  # until the second last element

# 2. 튜플(Tuple) : tuple----------------------------------------------------------------



''' ## 연산  -------------------------------------------------------- 
- indexing is used to access the value of an element in a list.
- i starts from 0 to n-1 where n is the length of the list.
- list, tuple, str, etc.
- ex) x[i:j] : x[i] to x[j-1] (inclusive)  -> Accessing elements in a range

'''
list_one[1], list_two[1], list_three[1]  # Accessing element in list_one, list_two, list_three
list_one[-1], list_two[-1], list_three[-1]  # Accessing last element in list_one, list_two, list_three
len(list_one), list_one[1:3]  # slicing list_one from index 1 to index 2 (exclusive)
list_one[1:-1]  # until the second last element


''' ##  Tuple --------------------------------------------------------



'''

''' ## 요소 추가 / 변경 / 삭제 -------------------------------------------------------- 
- append() : Adds an element at the end of the list
- insert() : Adds an element at the specified index
- delete() : Removes an element at the specified index
- x[i] = 'some value' : Updates the value of an element at the specified index
'''
list_something = ['test', 1, 2, 3, 4, 5, 6, 7, 8, 9,True, {'key' : 'value'}]
list_something.append('new!') # append an element at the end of the list, so if you want to add at a specific index, use insert()
list_something.insert(0, '0 index')  # insert an element at the specified index
list_something.insert(-1, '-1 index')  # !) -1 index is the second last index

list_something.insert(0, 'test')  
list_something.append('test')  
list_something.remove('test')  # remove an element from the list using the value, not its index & removes the first occurrence
list_something[1] = '1 index'  # update the value of an element at the specified index
print(list_something)




''' ## 기타 Function -------------------------------------------------------- 
- append() : Adds an element at the end of the list
- insert() : Adds an element at the specified index
- delete() : Removes an element at the specified index
- x[i] = 'some value' : Updates the value of an element at the specified index
'''
list_something.clear() # remove all items from the list
list_something.index('test')  # find the index of the first occurrence of the specified value
list_something.count('test') # count the number of occurrences of the specified value
list_something.pop() # remove the last item from the list and return it
list_something.sort() # sort the elements of the list in ascending order
list_something.reverse() # find the index of the last occurrence of the specified value
list_something.extend('test') # extend the list by appending elements from the iterable
list_something.copy() # return a shallow copy of the list







''' ##  Tuple --------------------------------------------------------



'''