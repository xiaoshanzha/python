import requests
from lxml import etree
import time

'''爬取豆瓣电影信息(动态加载)

第一页https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E5%8A%B1%E5%BF%97&start=20
第二页https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E5%8A%B1%E5%BF%97&start=40

'''
with open("豆瓣电影.txt",'w',encoding='utf-8')as f:
  for a in range(5):
    url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E5%8A%B1%E5%BF%97&start={}'.format(a*20)
    file = requests.get(url).json()

    for i in range(20):
      dict = file['data'][i]  #取出字典中 'data' 下第 [i] 部电影的信息
      url = dict['url']
      title = dict['title']
      rate = dict['rate']
      cast = dict['casts']

      f.write("{}, {} ,{},{}\n".format(title,url,rate,cast))



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


with open('豆瓣图书.csv','w',encoding='utf-8') as f:
  for a in range(2):
      url = 'https://book.douban.com/top250?start={}'.format(a*25)
      data = requests.get(url).text

      s = etree.HTML(data)
      file = s.xpath('//*[@id="content"]/div/div[1]/div/table')
      time.sleep(1)
      for div in file:
          title = div.xpath('./tr/td[2]/div[1]/a/@title')[0]
          href = div.xpath('./tr/td[2]/div[1]/a/@href')[0]
          score = div.xpath('./tr/td[2]/div[2]/span[2]/text()')[0]
          num = div.xpath('./tr/td[2]/div[2]/span[3]/text()')[0].strip("(").strip().strip(")")
          #这行代码用了几个 strip() 方法，()里面表示要删除的内容，strip(“(”) 表示删除括号， strip() 表示删除空白符。
          scribe = div.xpath('./tr/td[2]/p[2]/span/text()')[0]
          f.write("{},{},{},{},{}\n".format(title,href,score,num,scribe))
'''


'''
标题//*[@id="page_list"]/ul/li[1]/div[2]/div/a/span/text()
图片//*[@id="page_list"]/ul/li[1]/a/img/@src
价格//*[@id="page_list"]/ul/li[1]/div[2]/span[1]/i/text()
描述//*[@id="page_list"]/ul/li[1]/div[2]/div/em/text()
'''
'''
url = "http://cd.xiaozhu.com/"
data = requests.get(url).text
s = etree.HTML(data)

file=s.xpath('//*[@id="page_list"]/ul/li')
for div in file:
  title=div.xpath("./div[2]/div/a/span/text()")[0]
  price=div.xpath("./div[2]/span[1]/i/text()")[0]
  scrible=div.xpath("./div[2]/div/em/text()")[0].strip()
  pic=div.xpath("./a/img/@lazy_src")[0]
  print("{} {} {} {}".format(title, price, scrible, pic))

topic = s.xpath('//*[@id="page_list"]/ul/li[1]/div[2]/div/a/span/text()')
img = s.xpath('//*[@id="page_list"]/ul/li[1]/a/img/@lazy_src')
price = s.xpath('//*[@id="page_list"]/ul/li[1]/div[2]/span[1]/i/text()')
des = s.xpath('//*[@id="page_list"]/ul/li[1]/div[2]/div/em/text()')

print('主题：',topic)

'''

