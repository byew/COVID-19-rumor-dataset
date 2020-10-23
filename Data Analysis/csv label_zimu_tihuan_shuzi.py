import pandas as pd


exa = pd.read_csv('en_dup.csv')





exa.loc[exa['label'] =='F', 'label']= 0
exa.loc[exa['label'] =='T', 'label']= 1


exa.to_csv('train.csv', index=0)
