import seaborn as sns

df_iris = sns.load_dataset('iris')
df_peng = sns.load_dataset('penguins')
df_peng.dropna(inplace=True)