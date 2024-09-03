''' # Python 클래스(Classes)

1. 클래스 정의
- 키워드 : class [클래스명] - 클래스명은 파스칼 표기(Pascal Case) 
- !) 클래서 정의 후, 객체 생성하여 멤버변수를 추가할 수도 있음
- ex) class MyClass:
<code>
    class [클래스명]:
        - 구현
        def something(a, b):
            return a + b
</code>

2. Immutable  & Mutable 타입
- 1) Immnutable :불린(bool), 정수(int), 실수(float), 복소수(complex), 튜플(tuple), 문자열(str) 등
-- * Call by value : 함수내에서 인자값을 변경하더라도, 호출에 사용한 인자값이 변경되지 않는다. (즉, 내부 변화가 외부 호출에 영향을 주지 않는다.)
- 2) Mutable : 리스트(list), 딕셔너리(dict), 집합(set) 등
--  Call by reference : 함수내에서 인자값이 변경되면, 호출에 사용된 인자값도 변경된다.(즉, 내부 변화가 외부 호출에 영향을 준다.)
'''
class MyClass(object):
    pass