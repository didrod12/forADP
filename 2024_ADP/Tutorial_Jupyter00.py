# [Short-cut] Jupyter Notebook cell
'''
* 코드 셀 추가 : [snp] cell 입력
* 현재 셀 실행 : Ctrl + Enter
* 현재 셀 실행 & 다음 셀 이동 : Shift + Enter
* 현재 셀 실행 & new 셀 추가 : Alt + Enter

'''
msg = 'hello world!!!'

# %%
import numpy as np
import pandas as pd
import seaborn as sns

# Create a DataFrame

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 28, 27, 32],
        'Gender': ['Female', 'Male', 'Male', 'Female', 'Female'],
        'City': ['New York', 'London', 'Paris', 'Tokyo', 'Berlin']}

df = pd.DataFrame(data)

# Display the DataFrame

print(df)



