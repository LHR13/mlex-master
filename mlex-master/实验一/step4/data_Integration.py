import pandas as pd

data1 = pd.read_csv("C:\\Users\\李昊儒\\Desktop\\预处理  标准化，可视化，PCA实验数据\\4 ReaderInformation.csv")
data2 = pd.read_csv("C:\\Users\\李昊儒\\Desktop\\预处理  标准化，可视化，PCA实验数据\\4 ReaderRentRecode.csv")

data3 = data1.merge(data2)

data4 = data3.to_csv("C:\\Users\\李昊儒\\Desktop\\预处理  标准化，可视化，PCA实验数据\\4out.csv")
