import pandas as pd
from numpy import int64, float64
import numpy as np

'''读入数据并查看前十行'''
data = pd.read_csv("C:\\Users\\李昊儒\\Desktop\\预处理  标准化，可视化，PCA实验数据\\3 movie_metadata.csv")
data10 = data.head(10)

# '''对数据进行粗处理'''
# data.dropna(how='all')
# data.dropna(thresh=20)  # 删除行时保留非空值超过20个的
# data.dropna(subset=['movie_title'])  # 删除电影名为空的行
# data.drop_duplicates()  # 删除重复行
#
# '''规范化数据类型'''
print(data.dtypes)  # 查看各列数据类型
# data['cast_total_facebook_likes'] = data['cast_total_facebook_likes'].astype(float64)  # 将cast_total_facebook_likes改为float64格式
# print(data.dtypes)
# name = ['movie_title', 'director_name','actor_1_name' ,'actor_2_name', 'actor_3_name']
# for i in name:
#     data[i] = data[i].str.upper()  # 电影名和人名大写
#
# '''添加默认值（str型空值赋为NO GIVEN、int64赋为所在列众数、float64赋为所在列平均数）'''
# str_dype_cols = data.select_dtypes(include=object)
# for i in str_dype_cols:
#     data[i] = data[i].fillna('NO GIVEN')
#
# int64_dype_cols = data.select_dtypes(include=int64)
# for i in int64_dype_cols:
#     data[i] = data[i].fillna(data[i].mode())
#
# float64_dype_cols = data.select_dtypes(include=float64)
# for i in float64_dype_cols:
#     data[i] = data[i].fillna(data[i].mean())

'''异常数据处理'''


def normal_distribution_exception_handling(data):
    # data = np.array(data)
    upper = np.mean(data) + 2 * np.std(data)
    lower = np.mean(data) - 2 * np.std(data)
    except_data = []
    for i in data:
        if (upper < i) | (lower > i):
            except_data.append(i)
    print(except_data)

b = [0,1,2,3,55555,87888]
print(data['actor_2_facebook_likes'].head(15))
normal_distribution_exception_handling(data['actor_2_facebook_likes'].head(15))

