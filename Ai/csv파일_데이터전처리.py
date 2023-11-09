# https://coding-kindergarten.tistory.com/112
import numpy as np
import pandas as pd

df = pd.read_csv('https://bit.ly/ds-house-price')
print(df)

df = df.rename(columns={'분양가격(㎡)': '분양가격'})

#  그냥 0으로 하여도 에러는 나지 않지만 나중에 숫자 0이 어느 순간 NaN 값으로 바뀌어서 계속 NaN 값이 잡초처럼 자라나거든요.
df.loc[ df['분양가격'] == '  ', '분양가격'] = '0'
df['분양가격'] = df['분양가격'].fillna('0')

df['분양가격'] = df['분양가격'].str.replace(',', '')
df['분양가격'] = df['분양가격'].str.replace('-', '0')

# df['분양가격'].astype(int) -> 분양가격이 object로 나옴

df['분양가격'] = df['분양가격'].astype(int) # -> int로 나옴

df.info()

# ValueError: invalid literal for int() with base 10: '  '
# ValueError: cannot convert float NaN to integer
# ValueError: invalid literal for int() with base 10: '6,657'
# ValueError: invalid literal for int() with base 10: '-'