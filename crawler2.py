import requests
from lxml import etree
import time

'''爬取豆瓣电影信息
url = 'https://movie.douban.com/subject/1292052/'
data = requests.get(url).text
s = etree.HTML(data)

film = s.xpath('//*[@id="content"]/h1/span[1]/text()')
director = s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
actor = s.xpath('///*[@id="info"]/span[3]/span[2]/a/text()')
time = s.xpath('//*[@id="info"]/span[13]/text()')

print('电影名：',film)
print("导演：",director)
print("主演：",actor)
print("时长：",time)
'''



#爬取前10页豆瓣Top250图书信息

'''
Xpath
整本书//*[@id="content"]/div/div[1]/div/table
书名//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[1]/a
链接//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[1]/a
评分//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[2]/span[2]
人数//*[@id="content"]/div/div[1]/div/table/tr/td[2]/div[2]/span[3]
评价//*[@id="content"]/div/div[1]/div/table/tr/td[2]/p[2]/span

第一页https://book.douban.com/top250?start=0
第二页https://book.douban.com/top250?start=25
第三页https://book.douban.com/top250?start=50
'''

for a in range(10):
    url = 'https://book.douban.com/top250?start={}'.format(a*25)
    data = requests.get(url).text

    s = etree.HTML(data)
    file = s.xpath('//*[@id="content"]/div/div[1]/div/table')

    for div in file:
        title = div.xpath('./tr/td[2]/div[1]/a/@title')[0]
        href = div.xpath('./tr/td[2]/div[1]/a/@href')[0]
        score = div.xpath('./tr/td[2]/div[2]/span[2]/text()')[0]
        num = div.xpath('./tr/td[2]/div[2]/span[3]/text()')[0].strip("(").strip().strip(")")
        #这行代码用了几个 strip() 方法，()里面表示要删除的内容，strip(“(”) 表示删除括号， strip() 表示删除空白符。
        scribe = div.xpath('./tr/td[2]/p[2]/span/text()')[0]
        time.sleep(1)

        print("{} {} {} {} {}".format(title,href,score,num,scribe))
