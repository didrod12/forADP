''' # Python 클래스(Classes)
1. 클래스 주요 개념
- 1) Class : 객체를 생성에 필요한 설계도. 객체의 속성과 메서드를 정의
- 2) Object : 클래스로 부터 만들어진 실체. 클래스에서 정의한 속성과 메서드를 가짐
- 3) Attributes : 클래스나 객체가 가지는 변수
- 4) Methods : 클래스나 객체가 수행/기능하는 함수
- 5) Constructor : 객체 생성 시, 자동으로 호출되는 메서드 → __init__() 메서드

2. 클래스 정의
- 키워드 : class [클래스명] - 클래스명은 파스칼 표기(Pascal Case) 
- !) 클래서 정의 후, 객체 생성하여 멤버변수를 추가할 수도 있음
- ex) class MyClass:
<code>
    class [클래스명]:
        - 구현
        def something(a, b):
            return a + b
</code>

3. Immutable  & Mutable 타입
- 1) Immnutable :불린(bool), 정수(int), 실수(float), 복소수(complex), 튜플(tuple), 문자열(str) 등
-- * Call by value : 함수내에서 인자값을 변경하더라도, 호출에 사용한 인자값이 변경되지 않는다. (즉, 내부 변화가 외부 호출에 영향을 주지 않는다.)
- 2) Mutable : 리스트(list), 딕셔너리(dict), 집합(set) 등
--  Call by reference : 함수내에서 인자값이 변경되면, 호출에 사용된 인자값도 변경된다.(즉, 내부 변화가 외부 호출에 영향을 준다.)
'''

class Dog:
    # 클래스 속성
    species = '개과 동물'
    
    # 생성자 메서드 (객체 초기화) 
    def __init__(self, name, age):
        self.name = name
        self.age = age  # return 안해도 됨!
        print(f'{self.name}가 포함되었습니다.')
        
    # 소멸자 메서드 (객체 소멸) - GC아닌, 수동 제거시 사용.
    def __del__(self):
        print(f'{self.name}가 제외되었습니다.')
        
        
    # 메서드 정의
    def bark(self):
        return f'{self.name}가 짖는다. 왈왈 / 컹컹 / 왕왕?'
    
    # 메서드 정의2
    def get_age(self):
        return self.age * 7    
    
dog1 = Dog('행복이', 9)
    

    
    