import requests
from lxml import etree
from time import sleep
import pandas as pd
#豆瓣网250榜单
def get_urls(i):
    url="https://music.douban.com/top250?start={}".format(str(i))
    return url
    # print(music_urls)
def get_content(url):
    # 获取网页内容
    db_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    m_r = requests.get(url, headers=db_headers).text
    m_tree = etree.HTML(m_r)
    contents=m_tree.xpath('//tr[@class="item"]')
    return contents


def get_info(content):
    #抓取所需内容
    m_info=[]

    m_info.append(content.xpath('td[2]/div/a/text()')[0].replace('\n','').replace(' ','').replace(',','，'))#专辑名字
    temp=content.xpath('td[2]/div/p/text()')[0].split('/')
    m_info.append(temp[0].strip('\n').strip(' ').replace(',','和'))#歌手
    m_info.append(temp[1].replace(',','，'))#发行时间
    m_info.append(temp[2].replace(',','，'))#专辑类型
    m_info.append(temp[3].replace(',','，'))#专辑介质
    # m_info.append(temp[0].split('/')[4])#专辑流派
    m_info.append(content.xpath('td[2]/div/div/span[2]/text()')[0]) #豆瓣评分
    m_info.append(content.xpath('td[2]/div/div/span[3]/text()')[0].replace('\n','').replace(' ','').replace('(','').replace(')',''))# 评论人数

    # 存入文件
    with open('db_music.csv','a',encoding='utf-8-sig') as file:
        for item in m_info:
           if item==m_info[-1]:
               file.write(str(item)+'\n')
           else:
               file.write(str(item)+',')
    #打印到控制台
    # print(m_info[1:5])
    # for item in m_info:
    #     print(item,end='')
    # print(m_info[0])
    # print('\n')

for i in  range(0,250,25):#获取豆瓣top250的专辑
    music_urls=get_urls(i)
    music_contents=get_content(music_urls)
    for content in music_contents:
        get_info(content)

# music_data=pd.read_csv('db_music.csv')
# print(music_data)



