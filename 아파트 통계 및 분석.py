#_*_coding:utf-8 _*_
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager

font_location="C:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

data2018 = pd.read_excel(u'./주택매매가격지수.xlsx')
df = pd.DataFrame(data2018)
df2 = df[(df[u'기간']==2018)]
print(u"------------2018년 서울 주택매매가격지수------------")
print(df2)
print()

#2018년 서울 주택매매가격지수(바차트)
index = np.arange((df2[u'종합'].shape[0]))
bar_width = 0.35
fig, ax = plt.subplots()  
priceTotal = ax.bar(index, df2[u'종합'], bar_width,label=u"종합")
priceApart = ax.bar(index+bar_width, df2[u'아파트'],bar_width, label=u"아파트")
ax.set_xlabel(u'자치구')
ax.set_ylabel(u'매매가격지수')
ax.set_ylim(100, 115)
ax.set_title(u'서울특별시의 2018년 매매가격지수(기준=2017.11)')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(df2[u'자치구'])
ax.legend()


#년도별 서울 주택매매가격지수(꺾은선)
df2 = df[(df[u'자치구']==u'서울시')]
print(u"------------연도별 서울 주택매매가격지수------------")
print(df2)
print()
index = np.arange((df2[u'기간'].shape[0]))
x = df2[u'기간']
y = df2[u'종합']
y2 = df2[u'아파트']
fig, ax1 = plt.subplots()
ax1.set_xlabel(u'연도')
ax1.set_ylabel(u'종합', color='g')
ax1.plot(x, y, 'g-')
ax1.set_ylim(75, 110)
ax2 = ax1.twinx()
ax2.plot(x, y2, 'b-')
ax2.set_ylabel(u'아파트', color='b')
ax2.set_ylim(75, 110)
plt.title(u'연도별 서울특별시 주택 매매가격지수(기준=2017.11)') 
plt.grid() 
fig.tight_layout()

data_apart = pd.read_excel(u'./서울시아파트매매거래현황.xlsx')
df2 = pd.DataFrame(data_apart)
df2 = df2[(df2[u'자치구']==u'서울시')]
print(u"------------서울 아파트매매거래현황------------")
print(df2)
print()

#아파트 매매거래현황(꺾은선)
index = np.arange((df2[u'기간'].shape[0]))
x = df2[u'기간']
y = df2[u'동(호)수']
fig, ax = plt.subplots()
ax.set_xlabel(u'연도')
ax.set_ylabel(u'동(호)수', color='g')
ax.plot(x, y, 'g-')
ax.set_ylim(25000, 150000)
plt.title(u'연도별 서울특별시 아파트매매거래현황') 
plt.grid() 
fig.tight_layout()


plt.show()
