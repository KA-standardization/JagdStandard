import pandas as pd

df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print(df1)
df2 = pd.DataFrame({'a': [2, 2, 4], })
print(df2)
df=pd.merge(df1,df2,how='left')
print(df)






