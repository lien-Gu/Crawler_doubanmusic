from flask import Flask, render_template
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys
sys.path.append(r'subfunction')
import data_ana
from time import sleep
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
import os

# 创建Flask对象实例
app = Flask(__name__)


@app.route('/')
def index():
    # return 'hello world!'
    return render_template('index.html')


# 豆瓣评分top20榜单
@app.route('/rating_data_show')
def datashow():
    music_data = data_ana.get_music_data()
    data = data_ana.rating_data(music_data)
    data2 = np.array(data)
    data3 = data2.tolist()
    return render_template('data_rating.html',result=data3[:20])


# 豆瓣评价人数top20 折线图
@app.route('/reviewing_data_show')
def reviewing_show():
    music_data = data_ana.get_music_data()
    data_ana.reviewing_data(music_data)
    return render_template('data_reviewing.html')


# 豆瓣音乐top250年份分布图 柱状图
@app.route('/year_data_show')
def year_counts():
    music_data = data_ana.get_music_data()
    data_ana.year_data(music_data)
    return render_template('data_year.html')


# 豆瓣音乐top250评分分布(饼状图)
@app.route('/rating_counts_data_show')
def rating_counts():
    music_data = data_ana.get_music_data()
    data_ana.rating_counts(music_data)
    return render_template('data_rating_counts.html')


if __name__ == '__main__':
    # 启动web服务器
    app.run()