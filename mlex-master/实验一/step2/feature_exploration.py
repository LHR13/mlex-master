import xlrd
import numpy as np
from scipy import stats as sts
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

new_data_set = xlrd.open_workbook("C:\\Users\\李昊儒\\Desktop\\预处理  标准化，可视化，PCA实验数据\\2 西安北京年薪 数据.xlsx")

table = new_data_set.sheets()[0]

col2 = table.col_values(2)
del col2[0], col2[0]
col3 = table.col_values(3)
del col3[0], col3[0]

# 西安
data = np.array([i for i in col2], dtype=float)
print('以下是西安数据的集中趋势度量')
print('众数为：', sts.mode(data)[0][0])
print('中位数为：', np.median(data))
print('上四分位数为：', sts.scoreatpercentile(data, 25, interpolation_method='lower'))
print('下四分位数为：', sts.scoreatpercentile(data, 75, interpolation_method='fraction'))
print('简单算数平均数为：', sts.tmean(data))
print('调和平均数为：', sts.hmean(data))
print('几何平均数为：', sts.gmean(data))
print('以下是西安数据的离散趋势度量')
print('级差为：', np.ptp(data))
print('四分位间距为：', sts.scoreatpercentile(data, 75, interpolation_method='lower') -
      sts.scoreatpercentile(data, 25, interpolation_method='lower'))
print('方差为：', sts.tvar(data))
print('标准差为：', sts.tstd(data))
print('变异系数：', sts.tstd(data) / sts.tmean(data))
print('偏度为：', sts.skew(data))
print('峰度为：', sts.kurtosis(data))

# 北京
data2 = np.array([i for i in col3], dtype=float)
print('以下是北京数据的集中趋势度量')
print('众数为：', sts.mode(data2)[0][0])
print('中位数为：', np.median(data2))
print('上四分位数为：', sts.scoreatpercentile(data2, 25, interpolation_method='lower'))
print('下四分位数为：', sts.scoreatpercentile(data2, 75, interpolation_method='fraction'))
print('简单算数平均数为：', sts.tmean(data2))
print('调和平均数为：', sts.hmean(data2))
print('几何平均数为：', sts.gmean(data2))
print('以下是北京数据的离散趋势度量')
print('级差为：', np.ptp(data2))
print('四分位间距为：', sts.scoreatpercentile(data2, 75, interpolation_method='lower') -
      sts.scoreatpercentile(data2, 25, interpolation_method='lower'))
print('方差为：', sts.tvar(data2))
print('标准差为：', sts.tstd(data2))
print('变异系数：', sts.tstd(data2) / sts.tmean(data2))
print('偏度为：', sts.skew(data2))
print('峰度为：', sts.kurtosis(data2))

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df_data = pd.DataFrame(data, columns=['西安'])
df_data2 = pd.DataFrame(data2, columns=['北京'])

fig, axes = plt.subplots(1, 2)
sns.boxplot(x="西安", data=df_data, ax=axes[0])
sns.boxplot(x="北京", data=df_data2, ax=axes[1])

# fig, axes = plt.subplots(1, 2)
# sns.violinplot(x="西安", data=df_data, ax=axes[0])
# sns.violinplot(x="北京", data=df_data2, ax=axes[1])

plt.show()
