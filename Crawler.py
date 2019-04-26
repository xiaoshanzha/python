
'''
#爬取中国植物志网站上的植物名称及特称

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

num = []
paint_file =open('paint.txt','a')
for  i in range(1,3):
    html = urlopen("http://frps.iplant.cn/jingji/7?page="+str(i)).read().decode('utf-8')
    soup = BeautifulSoup(html,features='lxml')
    sub_urls = soup.find_all("a",{"href":re.compile("/frps/.*?")})
    num.append(sub_urls)
sum = 510
for i in range(0,14):
    for j in range(1,15):
        temp = "http://frps.iplant.cn"+ num[i][j]['href']
        temp = temp.replace(' ','%20')
        print(temp)
        print("ada")
        html_2 = urlopen(temp).read().decode('utf-8')
        soup = BeautifulSoup(html_2,features='lxml')
        text = soup.find_all(style="font-size:14px; margin-top:10px; ")
        text1 = soup.find_all(style='text-indent:24px')
        if (len(text)&(len(text1))):
            print(text[0].b.string)
            print(text1[2].string)
            paint_file.write(str(sum)+"  :  "+text[0].b.string + "\n")
            paint_file.write(text1[2].string+"\n\n\n")
            sum = sum + 1
paint_file.close()

'''

'''
#使用 urlretrieve下载图片
# from urllib.request import urlretrieve
# import os

#创建文件夹
# os.makedirs('./img/',exist_ok=True)

# image_url = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'
# urlretrieve(image_url,'./img/study.png')



#使用request下载图片

# import requests
# image_url = 'https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'
# r = requests.get(image_url)
# with open('./img/study1.png','wb') as f:
#     for chunk in r.iter_content(chunk_size=32):
#         f.write(chunk)


# 下载国家地理中文网美图实战

from bs4 import BeautifulSoup
import requests

url = "http://www.ngchina.com.cn/animals/"
html = requests.get(url).text
soup = BeautifulSoup(html,'lxml')
img_url = soup.find_all('ul',{'class':'img_list'})
for ul in img_url:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url)
        image_name = url.split('/')[-1]
        with open('./img/%s'% image_name,'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)

'''





























