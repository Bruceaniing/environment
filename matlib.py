import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df = pd.read_excel("https://github.com/chris1610/pbpython/blob/master/data/sample-salesv3.xlsx?raw=true")
df.head()

top_10 = (df.groupby('name')['ext price', 'quantity'].agg({'ext price': 'sum', 'quantity': 'count'})
          .sort_values(by='ext price', ascending=False))[:10].reset_index()
top_10.rename(columns={'name': 'Name', 'ext price': 'Sales', 'quantity': 'Purchases'}, inplace=True)
top_10
plt.style.use('ggplot')
top_10.plot(kind='barh', y="Sales", x="Name");


fig, ax = plt.subplots()                                                      # 向plt.subplots() 添加了一个额外的调用，并将ax传递给绘图函数
top_10.plot(kind='barh', y="Sales", x="Name", ax=ax);


fig, ax = plt.subplots()
top_10.plot(kind='barh', y="Sales", x="Name", ax=ax)
ax.set_xlim([-10000, 140000])
ax.set(title= '2014 Revenue' , xlabel= 'Total Revenue' , ylabel= 'Customer');  # 快捷键，同时设置标题和两个标签


fig, ax = plt.subplots(figsize=(5,6))                                          # 通过figsize()修改图窗大小
top_10.plot(kind='barh', y="Sales", x="Name", ax=ax)
ax.set_xlim([-10000, 140000])
ax.set(title='2014 Revenue', xlabel='Total Revenue', ylabel='Customer')  # 快捷键，同时设置标题和两个标签
ax.legend().set_visible(False);
# def currency(x, pos):
#     if x >= 1000000:
#         return ${:1.1f}M .format(x*1e-6)
#     return ${:1.1f}K .format(x*1e-3)
# fig, ax = plt.subplots()
#
# top_10.plot(kind= barh , y="Sales", x="Name", ax=ax)
#
# ax.set_xlim([-10000, 140000])
#
# ax.set(title= '2014 Revenue' , xlabel= 'Total Revenue' , ylabel= 'Customer' )
#
# formatter = FuncFormatter(currency)
#
# ax.xaxis.set_major_formatter(formatter)
#
# ax.legend().set_visible(False)

