import numpy as np    # numpy
import pandas as pd   # pandas
import seaborn as sns # seaborn : 예제 데이터셀 제공


# msg = "vs code tutorial"
# print(msg)
# print(np.random.randint(1,6))


# 인터넷에 있는 CSV 파일 URL : 붓꽃 예제
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'

# CSV 파일 읽기
df = pd.read_csv(url)

# 데이터프레임 출력
print(df)






