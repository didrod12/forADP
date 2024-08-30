''' # 수치 자료형(Numeric Data Type)
1. 정수형(Integer) : int
- 소수점 없는 정수값, 양/음의 정수 & 0

2. 실수형(Float) : float
- 소수점이 포함된 실수값, mainly used for floating point numbers

3. 복소수형(Complex) : complex
- 실수와 허수부로 구성된 숫자, a(실수) + bj(허수부)
'''
int_one = 1
float_one = 1.0
complex_one = 1 + 1j

''' ## 수치자료형 변환(Type Conversion) --------------------------------------------------------
- int() : To Integer, int() function converts the given value to integer.
- float() : To Float, float() function converts the given value to floating point number.
- complex() : To Complex, complex() function converts the given value to complex number.

- abs() : Returns the absolute value of the given

- str() : str() function converts the given value to string.
'''
int_a = 37
int_b = 31.37

to_int = int(int_b)
to_float = float(int_a)
to_complex = complex(23,73) # 천재환,목지훈(24.08.04)
print(to_int, to_float, to_complex)

''' ## 기본적인 수치 연산 --------------------------------------------------------
- 덧셈(+) : Addition
- 뺄셈(-) : Subtraction
- 곱셉(*) : Multiplication
- 나눗셈(/) : Division
- *정수 나눗셈(//) : Floor Division
- *나머지(%) : Modulus
- *거듭제곱(**) : Exponentiation - [fn] pow(x, r) -> x의r제곱
'''
addition_a = 10 + 5   # 15
subtraction_b = 10 - 3   # 7
multiplication_c = 10 * 3   # 30
division_d = 10 / 2   # 5.0
floor_division_e = 10 // 3  # 3
modulus_f = 10 % 3   # 1
exponentiation_g = 2 ** 3   # 8
exponentiation_h = pow(2, 3)
# exponentiation_g == exponentiation_h

# 단, int & int 연산의 결과는 always : float!!!
int_x = 10
int_y = 5
cal_int = int_x/int_y
type(cal_int)
