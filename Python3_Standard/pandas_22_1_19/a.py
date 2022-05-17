import pandas as pd
import numpy as np

l = []
l2 = []
l3 = []
l4 = []
key_1 = []
df = pd.read_excel('./test.xlsx')

df2 = pd.pivot_table(
    data=df,
    values=['comment_count', 'share_count', 'like_count', 'collect_count'],
    index=['key', 'match_key_word', 'post_id'],
)

for k in list(df2.index):
    if k[0] not in key_1:
        key_1.append(k[0])

for k in key_1:
    sum_ = 0
    tmp_df = df2.loc[f"{k}"]
    shape_ = tmp_df.shape
    key_3 = []
    for k3 in list(tmp_df.index):
        if k3[0] not in key_3:
            key_3.append(k3[0])
    for kk in key_3:
        tmp_df2 = tmp_df.loc[f"{kk}"]
        shape__ = tmp_df2.shape
        sum_num = sum(np.ravel(tmp_df2))
        for _ in range(shape__[0]):
            l.append(sum_num)
            if sum_num not in l3:
                l3.append(sum_num)
            else:
                l3.append(0)
        sum_ += sum_num
    for _ in range(shape_[0]):
        l2.append(sum_)
        if sum_ not in l4:
            l4.append(sum_)
        else:
            l4.append(0)

df2['业'] = l
df2['务'] = l2
df2['事'] = l3
df2['逼'] = l4

df2.to_excel('./r2.xlsx')
