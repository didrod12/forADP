# 1. 데이터 핸들링
''' # 1) 판다스 데이터 구조 
    * Series : 1차원 labeled array
        - 각 값에 레이블이 있고, 하나의 데이터 형식으로 이루어짐
    * DataFrame : 2차원 labeled data structure with columns of potentially different types
        - 2차원 행렬, like an 엑셀 형태 구조
        - 각 행은 인덱스를 가지고, 각 열은 서로 다른 데이터 형식을 가질 수 있음
'''
# %%
import pandas as pd
import numpy as np

# 1-1. Series 생성 : pd.Series()
ex_series = pd.Series([1, 2, 3, 4, 5], name="numbers")
ex_series2 = pd.Series({'idx1':1, 'idx2': 2}, name="numbers2")
print(ex_series)
print(ex_series2)

# 1-2. DataFrame 생성 : pd.DataFrame()  
ex_list = [1,2,3,4,5,6,7,8,9]
ex_arr = np.array(['Min Woo',2], ['Hart', 30 ], ['Davidson', 24])



# 2) DataFrame


# 3) row/column 선택 / 추가 / 삭제

# 4) 데이터 조건 탐색 & 수정

# 5) 데이터 정렬

# 6) 데이터 결합

# 7) 데이터 요약

# 8) 데이터 재구조화

# 9) 데이터 프레임: 함수 사용

# 10) 변환     : 문자열 데이터

# 11) 날짜 데이터 핸들링