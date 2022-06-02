import pandas as pd

df1 = pd.read_csv('/opt/ml/input/Project/data/Training/train_3label.csv')
df2 = pd.read_csv('/opt/ml/input/Project/data/Validation/validation_3label.csv')

#df = pd.concat([df1,df2])

#df.to_csv('./validation_label.csv',sep=',',index=False)
print(df2)
