import xlrd
from pyecharts.charts import Bar

data = xlrd.open_workbook("C:\\Users\\李昊儒\\Desktop\\\预处理  标准化，可视化，PCA实验数据 (1)\ 1 某县广电宽度数据.xls")

table = data.sheets()[0]

print(table.nrows)
print(table.ncols)
row0 = table.row_values(0)
row1 = table.row_values(1)
print(row0)
print(row0[6])
print(row1)



