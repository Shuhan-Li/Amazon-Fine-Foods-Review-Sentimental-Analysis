import pandas as pd

# 加载数据集
df = pd.read_csv('Reviews.csv')

# 分别处理不同的Rate类别
df_1 = df[df['Score'] == 1].sample(n=10000, random_state=1)  # 对Rate为1的抽取1000条
df_2 = df[df['Score'] == 2].sample(n=10000, random_state=1)  # 对Rate为2的抽取1000条
df_3 = df[df['Score'] == 3].sample(n=20000, random_state=1)  # 对Rate为3的抽取2000条
df_4 = df[df['Score'] == 4].sample(n=10000, random_state=1)  # 对Rate为4的抽取1000条
df_5 = df[df['Score'] == 5].sample(n=10000, random_state=1)  # 对Rate为5的抽取1000条

# 将所有抽取的部分合并成一个新的DataFrame
df_extract = pd.concat([df_1, df_2, df_3, df_4, df_5])

# 将抽取的数据保存到新的CSV文件
df_extract.to_csv('Reviews_20000.csv', index=False)
