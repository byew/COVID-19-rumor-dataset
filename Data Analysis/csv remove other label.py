import pandas as pd


exa = pd.read_csv('en_dup.csv')

exa.loc[exa['label'] =='F', 'label']= 0
exa.loc[exa['label'] =='T', 'label']= 1
exa.loc[exa['label'] =='U', 'label']= 2

#不读取label2, 只读取0，1标签

exa0 = exa.loc[exa["label"] == 0]
exa1 = exa.loc[exa["label"] == 1]

exa = [exa0, exa1]
exa = pd.concat(exa)

exa.to_csv('train.csv', index=0)
