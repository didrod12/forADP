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

## 1-2. 조건 설정(Condition Setting) - comparison operator, etc.
'''
1-1) Comparison Operator : 비교 연산자
- comparison operators are used to compare two values and determine their relationship. 
- Examples : a > b, a < b, a == b, a!= b, a >=
- 1) == : equal to
- 2) != : not equal to
- 3) > : greater than
- 4) < : less than
- 5) >= : greater than or equal to
- 6) <= : less than or equal to

1-2) Logical Operator : 논리 연산자
- logical operators are used to combine boolean values.
- examples : a and b, a or b, not a
- 1) and : logical AND (true if both operands are true)
- 2) or : logical OR (true if either operand is true)
- 3) not : logical NOT (true if the operand is false)

1-3) Membership Operator(sequence membership operator) : 멤버 연산자
- membership operators are used to check if a value exists in a sequence.
- examples : a in b, a not in b
-1) in : sequence/object membership (true if the value/object is in the sequence)
-2) not in : sequence/object membership (true if the value/object is not in the sequence)
-*3) isinstance : type membership (true if the value is an instance of the specified type)

1-4) Identity Operator : 식별 연산자
- identity operators are used to compare the memory locations of two objects.
- examples : a is b, a is not b
- 1) is : object identity (same memory location)
- 2) is not : object identity (different memory location)


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