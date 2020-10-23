import pandas as pd





train = train[['content', 'label']]
train_1 = train.sample(frac=0.7, random_state=0, axis=0)
dev_1 = train[~train.index.isin(train_1.index)]

train_1.to_csv('train.csv')
dev_1.to_csv('dev.csv')
