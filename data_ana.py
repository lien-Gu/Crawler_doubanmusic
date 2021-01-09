import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib as mpl
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False

def get_music_data():
    music_data=pd.read_csv('db_music.csv',encoding='utf-8')
    music_data.columns=['name','composer','time','material','type','rating_score','rating_people']
    # print(music_data)
    return music_data

#豆瓣评分top20榜单
def rating_data(music_data):
    rating=music_data.sort_values(by='rating_score',ascending=False)#降序排列
    # print(rating)
    return rating

#豆瓣评价人数top20 折线图
def reviewing_data(music_data):
    music_data['rating_people']=music_data['rating_people'].apply(lambda arg:int(arg[0:-3]))#处理字段格式
    reviewing=music_data.sort_values(by='rating_people',ascending=False)[:20]#降序排列
    plt.plot(reviewing['name'],reviewing['rating_people'])
    plt.xticks(rotation=90)
    # plt.show()#控制台展示
    # plt.savefig('reviewing.png')#保存到当前路径
    basedir = os.path.abspath(os.path.dirname(__file__))
    # print(basedir+'/static/images/')
    plt.savefig(basedir + '/static/images/' + 'reviewing.png')
    # print(reviewing['rating_people'])


# 豆瓣音乐top250年份分布图 柱状图
def year_data(music_data):
    def time_convert(arg):
        arg = arg.strip(' ')
        year = arg[:4]+'年'
        if year == 'Sept':
            year = '2008年'
        return year
    music_data['year'] = music_data['time'].apply(time_convert)
    # print(music_data['year'])
    music_year = music_data['year'].value_counts()
    plt.bar(music_year.index, music_year.values, color='blue')
    plt.xticks(rotation=90)
    plt.xlabel('年份')
    plt.ylabel('专辑数目')
    plt.title('豆瓣音乐top250年份分布图')
    # plt.show()

    basedir = os.path.abspath(os.path.dirname(__file__))
    plt.savefig(basedir + '/static/images/' + 'music_year.png')
    print('bar')


# 评分分布(饼状图)
def rating_counts(music_data):
    music_rating_score = music_data['rating_score'].value_counts()
    plt.pie(music_rating_score.values,
            labels=music_rating_score.index,
            autopct='%1.1f%%',
            shadow=False,
            labeldistance=1.3,
            pctdistance=0.9,
            startangle=150
            )
    plt.axis('equal')
    plt.title('评分分布图')
    # plt.savefig('music_score.png')
    basedir = os.path.abspath(os.path.dirname(__file__))
    # print(basedir+'/static/images/')
    plt.savefig(basedir + '/static/images/' + 'music_score.png')
    print('pie')


# music_data = get_music_data()
# rating_counts(music_data)










