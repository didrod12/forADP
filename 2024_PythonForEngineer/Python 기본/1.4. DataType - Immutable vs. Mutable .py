'''# 불변(Immutable) vs. 가변(Mutable) Types
# 1. 불변(Immutable)
- Immutable types cannot be changed after they are created.
- Immutable types have faster access times compared to mutable types.
- copying an immutable type creates a new object.
- ex) int, float, complex, str, bytes, frozenset, tuple, range, etc

# 2. 가변(Mutable) : list, dict, set  
 - Mutable types can be changed after they are created.
 - Mutable types have slower access times compared to immutable types.
 - copying a mutable type creates a new object. shallow copy - copied reference(address)
 - ex) list, dict, set, bytearray, memoryview, etc.
 - ex) list_one[2] = 'Changed'
 - ex) dict_one['key'] = 'Changed'
 - ex) set_one.add('Changed')
 
'''
number = 10
number2 = 10
number3 = number
id(number)  # id() : return the identity of an object
id(number2) 
id(number) == id(number2)  # True
id(number) == id(number3)  # True, deep copy - directly copied object(value)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
days2 = days
id(days) , id(days2)  # True
days is days2  # True, shallow copy - copied reference(address)
days2.append('Saturday')
print(days) # days also added 'Saturday'

days_deep_copy = days.copy()
days_deep_copy.append('Sunday')
print(days) # days not added 'Sunday'

# comparison : is() & == ----------------------------
'''
- is() : identity comparison (True if the two objects are the same object)
- == : equality comparison (True if the two objects have the same value)
'''
word = 'happy'
emotion =['happy', 'joyful', 'excited']
feeling = emotion

feeling == emotion  # True
feeling is emotion  # True, shallow copy - copied reference(address)
id(feeling) , id(feeling) # True

feeling2 = emotion.copy()
feeling2 is emotion  # False, deep copy - directly copied object(value)
feeling2 == emotion  # True, comparing values
id(feeling2), id(emotion) # both point to different



