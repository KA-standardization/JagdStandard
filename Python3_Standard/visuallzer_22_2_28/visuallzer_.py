# -*- coding:utf-8 -*-
import visualizer as ver
import pandas as pd
import numpy as np

data = np.random.randn(2, 3)
df = pd.DataFrame(data)
print(df)

v = ver.Visualizer(df, target_col=[0, 1])
v.visualize_all()
