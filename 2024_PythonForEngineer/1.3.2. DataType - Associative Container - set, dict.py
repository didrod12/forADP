''' # 연관 컨테이너(Associative Container type)
- 데이터가 특정 키와 연관되어 저장되는 컨테이너 ⇒ No indexing & No ordering
- key-value pair를 사용 ⇒ Unordered & No Duplicates allowed sequence
- 키(key)와 값(value)처럼 관련있는 데이터를 하나의 쌍으로 저장하는 컨테이너
- default 정렬 기준으로 자료 입력과 동시에 모든 자료가 정렬됨 - binary search, hash table
- 이진 탐색 트리(balanced binary search tree)나 해시 테이블(hash table)을 이용하여 구현
- ex) set, dict

1. 집합(set) - set
- key-value pair ⇒ Unordered collection of unique elements
- using {'value', 'value1', 'value2' ...}

2. 딕셔너리(dict) - dict
- key-value pair ⇒ Unordered collection of unique elements
- using {'key' : 'value', 'key1' : 'value1', 'key2' : 'value2'...}

'''

# 1. 집합(set) : set----------------------------------------------------------------
set_one = {1, 2, 3, 4}
set_empty = set() # create an empty set using set() function, if use {} creates an empty dictionary
not_set_empty = {}
type(set_one), type(set_empty), type(not_set_empty) # set, set, dict

# 2. 딕셔너리(dict) : dict----------------------------------------------------------------
dict_one ={'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5}
dict_empty = {}
dict_empty1 = dict()
type(dict_one), type(dict_empty), type(dict_empty1) 

# 1) pair list로 dictionary 생성 --------------
keys = ['one', 'two', 'three', 'four', 'five']
values = [1, 2, 3, 4, 5]
dict_two = dict(zip(keys, values))  # convert list of keys and values
type(dict_two)

# 2) 키워드로 dictionary 생성 --------------
dict_three= dict(one = 1, two = 2, three = 3, four = 4, five = 5)
type(dict_three)

# 3) dictionary comprehension로 생성 --------------
dict_four = dict({key: value for key, value in zip(keys, values)})
dict_five = dict((key, value) for key, value in zip(keys, values))
type(dict_four), type(dict_five)

# 4) collections모듈의 OrderDict으로 생성 --------------
from collections import OrderedDict # OrderedDict :삽입 순서 유지
keys =  ['two',  'four', 'five', 'one', 'three']
values = [1, 3, 2, 4, 5]
dict_six = OrderedDict({key: value for key, value in zip(keys, values)})

''' ## 요소 다루기(Handling elements) -------------------------------------------------------- 

'''
# 1. 집합(set) : set----------------------------------------------------------------
set_2 = {'박민우', '1993.02.06', '31', 'male', '2B'} # unordered collection
set_31 = {'손아섭', '1998.03.18','36', 'male', 'DH'}
set_37 = {'박건우', '1990.09.08', '33', 'male', 'RF'}
print(set_2,set_31, set_37)

# 1) 요소 추가 : add--------------
set_2.add('in')
set_31.add('out')
set_37.add('out')
print(set_2, set_31, set_37)

# 2) 요소 삭제 : remove, discard, pop--------------
set_2.remove('out') # KeyError: 'out', doesn't exist in set, 요소가 집합에 없으면 KeyError를 발생
set_2.discard('out') # No error, 요소가 집합에 없어도 에러를 발생시키지 않고 조용히 넘어갑니다.

set_number = {'one', 'two', 'three', 'four', 'five'}
random_num = set_number.pop() # randomly removes an element
set_number.clear() # removes all elements

# 4) key 존재 확인 및 반환: 'key' in set--------------
is_position_in_set_2 = '2B' in set_2 # True


# 3) 집합 연산 : 합집합(|), 교집합(&), 차집합(-), 대칭 차집합(^)--------------
set_months = {'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'}
set_days = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}

## Union: 합집합 - union() or | ----------------
set_union = set_months.union(set_days)
set_union2 = set_months | set_days
print(set_union == set_union2) # True

## Intersection: 교집합 - intersection() or & ----------------
set_intersection = set_months.intersection(set_days)
set_intersection2 = set_months & set_days
print(set_intersection == set_intersection2) # True


## Difference: 차집합 - difference() or - ----------------
set_difference = set_union.difference(set_days)
set_difference2 = set_union - set_days
print(set_difference == set_difference2) # True

## Symmetric difference: 대칭 차집합 - symmetric_difference() or ^ ----------------
set_number1 ={1,2,5,6,7}
set_number2= {2,3,5,7,8}

set_number1 - set_number2 # difference, {1, 6}

set_symmetric = set_number1.symmetric_difference(set_number2) # symmetric difference, {1, 3, 6, 8}
set_symmetric2 = set_number1 ^ set_number2
print(set_symmetric == set_symmetric2) # True

## Subset: 부분집합 - issubset() & issuperset or <= & >= / isdisjoint() ----------------
'''
1) issubset() or <= : setObject.issubset(otherSet) - setObject is a subset of otherSet
2) issuperset or >= : setObject.issuperset(otherSet) - setObject is a superset of otherSet
#) isdisjoint() : setObject.isdisjoint(otherSet) - setObject and otherSet have no elements(교집합 없는 지 확인)
'''
is_days_subset = set_days.issubset(set_union) # True
is_months_subset2 = set_months <= set_union # True

is_union_super = set_union.issuperset(set_days) # True
is_union_super2 = set_union >= set_months # True

is_numbers_disjoint = set_number1.isdisjoint(set_number2) # False, set_number1 and set_number2 have some elements : {2, 5, 7}
print(set_number1 & set_number2)

# 2. 딕셔너리(dictionary) : dict----------------------------------------------------------------
dict_number = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
dict_2 = {'name' : '박민우', 'birth' :  '1993.02.06', 'age': 31, 'gender' :'male', 'position' : '2B'} #1째주 토요일(정월대보름)
dict_31 = {'name' : '손아섭', 'birth' : '1988.03.18', 'age': 36, 'gender' :'male', 'position' : 'DH'} #3째주 금요일
dict_37 =  {'name' : '박건우', 'birth' : '1990.09.08', 'age':33 , 'gender' : 'male' , 'position' : 'RF'} #2째주 토요일(백로)

list_keys_37 = ['name', 'birth', 'age', 'gender', 'position', 'Throws/Bats']
new_key_dict_37 = dict.fromkeys(list_keys_37) # creating a dictionary with all keys as the provided list

print(dict_2,dict_31, dict_37)

# 1) 요소 추가 & 수정 : [key] = value, update--------------
dict_2['status'] = 'in'  # adding a new key-value pair
dict_31['status'] = 'out'
dict_37['status'] = 'out'

dict_2['captain'] = 'Yes'
dict_31['captain'] = 'Yes'
dict_37['captain'] = 'No'
print(dict_2, dict_31, dict_37)

dict_2['gender'] = '남자'  # modifying a value
dict_31['gender'] = '남자'
dict_37['gender'] = '남자'
print(dict_2, dict_31, dict_37)

dict_37.update({'No.': 3})  # adding a new key-value pair
dict_2.update({'status': 'active', 'position': 'DH'})  # updating multiple key-value pairs
print(dict_2)

# 2) 요소 삭제 : del, pop---------------------
del dict_31['captain']  # deleting a specific key, so that key-pair deletion
value_31 = dict_31.pop('status')  # removes a key-value pair & returns the value
key_last_37, value_last_37 = dict_37.popitem()  # removes a key-value, returns the key and value

dict_number.clear()  # removes all elements

# 3) key 존재 확인 및 반환:  'key' in dictionary--------------
is_captain_in_dict_2 = 'captain' in dict_2  # True, key exists in dictionary
position_dict_2 = dict_2.get('position', 'Not found')  # the position exists in dictionary, and returns the value otherwise, returns the default value('Not found')

# 4) 모든 키, 값, 항목 가져오기 : keys(), values(), items()--------------
keys_31 = dict_31.keys()
type_keys_31 = type(keys_31) # dict_keys object 

values_31 = dict_31.values()
type_values_31 = type(values_31) # dict_values object

items_31 = dict_31.items()
type_items_31 = type(items_31) # dict_items object

''' ## 형변환(Convert)  -------------------------------------------------------- 
- list() : tuple/set/dict to(→) list
- set() : list/tuple/dict to(→) set
- dict() : list(tuple type) to(→) dict
'''
## 1) list() : set/dict/tuple to(→) list------------------
tuple_number = ('one', 'two', 'three', 'four', 'five', 'four', 'three', 'two', 'one')

# !) set & dictionary can have unique elements : set(element), dict(key)
set_number = {'one', 'two', 'three', 'four', 'five', 'four', 'three', 'two', 'one'}
dict_number = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five':5 ,'four': '사' , 'three':'삼', 'two': '둘', 'one':'하나'}

list_number1 = list(tuple_number)  # ordering
list_number2 = list(set_number) # random order
list_number3 = list(dict_number) #just keys are preserved, values are not preserved
print(list_number1),  print(list_number2), print(list_number3)
print(type(list_number1), type(list_number2), type(list_number3))
#!) list_number1~3 are not same, they have different values ⇒ bc) list is sequential.

## 2) set() : list/tuple to(→) set------------------------
list_number = [1, 2, 3, 4, 5, 4, 3, 2, 1] # list can have duplicate elements
tuple_number = (1, 2, 3, 4, 5, 4, 3, 2, 1) # tuple can have duplicate elements
dict_number = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five'} # duplicate keys are not allowed

set_number1 = set(list_number)  # remove duplicates
set_number2 = set(tuple_number)  # remove duplicates
set_number3 = set(dict_number.values())  # dictionary values to create a set
print(set_number1),  print(set_number2), print(set_number3)
print(type(set_number1), type(set_number2), type(set_number))

## 3) dict() : list(tuple type) to(→) dict----------------
list_of_tuples = [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('one', 1), ('two', 2), ('three', 3), ('four', 4)] # list can have duplicate elements
dict_number1 = dict(list_of_tuples)  # convert list of tuples to dictionary, removing duplicate elements
type(dict_number1)
