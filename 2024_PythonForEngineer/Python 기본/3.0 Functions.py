''' # Python 함수(Functions)

1. 함수 정의
<code>
    def [함수명](parameters...):
        - 구현
        reslult = some_value
        return some_value
</code>

2. 연관 컨테이너((Associative Container)
- 데이터가 특정 키와 연관되어 저장되는 컨테이너
- key-value pair를 사용 ⇒ Unordered & No Duplicates allowed sequence
- 키(key)와 값(value)처럼 관련있는 데이터를 하나의 쌍으로 저장하는 컨테이너
- default 정렬 기준으로 자료 입력과 동시에 모든 자료가 정렬됨 - binary search, hash table
- 이진 탐색 트리(balanced binary search tree)나 해시 테이블(hash table)을 이용하여 구현
- ex) set, dict
'''
def add(a,b):
    return a + b

def printSomething(a, b, c):
    return print(a, b, c)

a = 1
b = 2
c = add(a,b)
printSomething(a,b,c)


def computeProps(club_name, pleyer1, player2):
    club_name = (pleyer1, player2)
    
    return club_name

pl1 = '박건우'
pl2 = '박민우'
club_name = 'NC 다이노스'
players = computeProps(club_name, pl1, pl2)
건우, 민우 = computeProps(club_name, pl1, pl2)
print(f'players - {players}') 
print(f'player1 - {건우} / player2 - {민우}') 