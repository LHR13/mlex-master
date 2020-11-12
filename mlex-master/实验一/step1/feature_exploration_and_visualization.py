import pandas as pd
import datetime as dt
from pyecharts.charts import Radar

data = pd.read_excel("C:\\Users\\李昊儒\\Desktop\\预处理  标准化，可视化，PCA实验数据\\1 某县广电宽度数据.xls")

def date_to_week(data):
    day = pd.to_datetime(data)
    week = [0] * 7
    for i in day:
        weekday = dt.date.weekday(i)
        if weekday == 0:
            week[0] += 1
        elif weekday == 1:
            week[1] += 1
        elif weekday == 2:
            week[2] += 1
        elif weekday == 3:
            week[3] += 1
        elif weekday == 4:
            week[4] += 1
        elif weekday == 5:
            week[5] += 1
        else:
            week[6] += 1
    return week


week = date_to_week(data['入网时间'])
week1 = [week]
radar = Radar()
schema = [{"name":'星期天', "max":1000}, {"name":'星期一', "max":1000}, {"name":'星期二', "max":1000},
          {"name":'星期三', "max":1000}, {"name":'星期四', "max":1000}, {"name":'星期五', "max":1000}, {"name":'星期六', "max":1000}]
radar.add(data=week1, series_name='入网时间')
radar.add_schema(schema)
radar.render('render.html')
