
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





# temp= temp.replace(' ','20%')
# print(temp)
# html = urlopen("http://frps.iplant.cn"+temp).read().decode('utf-8')
# soup = BeautifulSoup(html,features='lxml')
# text = soup.find_all(style="font-size:14px; margin-top:10px; ")
# text1 = soup.find_all(style='text-indent:24px')
# print(text[0].b.string)
# print(text1[2].string)
# # temp = num[0][0]['href']
# i = 1
# paint_file.write(str(i)+"  :  "+text[0].b.string + "\n")
# paint_file.write(text1[2].string+"\n")



# print(len(num))
# print(num)
# print(num[0][0]['href'])


# sum = len(sub_urls)
# i = 0
# print(sum,'\n')
# while(i < sum):
#     print(sub_urls[i]['href'])
#     i = i + 1
