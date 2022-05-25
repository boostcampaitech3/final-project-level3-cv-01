import pandas as pd

df1 = pd.read_csv('/opt/ml/input/project/data/Validation/abnormal_label.csv')
df2 = pd.read_csv('/opt/ml/input/project/data/Validation/normal_label.csv')

df = pd.concat([df1,df2])

df.to_csv('./validation_label.csv',sep=',',index=False)