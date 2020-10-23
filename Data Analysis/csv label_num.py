import pandas as pd


exa = pd.read_csv('en_dup.csv')

exa = exa[['label']]
print("label", exa['label'].value_counts())
print(exa)
