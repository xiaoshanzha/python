'''
mess = 'hEllo world'
print(mess.title())  #仅首字母大写
print(mess.upper())   #字符串全部大写
print(mess.lower())   #字符串全部小写
'''

'''
first_name = "feng"
last_name = " shanzha "
full_name = first_name + " " + last_name
print("hello" + " " + full_name.title())     #字符串拼接
print(full_name)
print(last_name.rstrip())  #删除右边空白
print(last_name.lstrip())  #删除左边空白
print(last_name.strip())   #删除全部空白
'''
'''
age = 18
message = "hello " + str(age) +"rd Birthday"
print(message)

fruit = ['apple','banana','orange']
print(fruit[-1])
print(fruit[-3])


num_list = ["a","c","b","zz","shanzha"]
print(sorted(num_list))
print(sorted(num_list,reverse=True))

#列表解析式，推导式
a=[i*2 for i in range(1,11)]  #for前面是我们想要放在列表中的元素，for后面是循环的元素本身
print(a)

#字典推倒式
g = {i:j for i,j in zip(range(1,6),'abcde')}
print(g)
g = {i:j.upper() for i,j in zip(range(1,6),'abcde')}
print(g)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for num,letter in enumerate(letters):
    print(letter,'is',num+1)
    '''
#测试一段文本中各单词出现的次数
#53行 列表解析式 ：去除单词前后的标点并将其小写存入列表当中 54行：去除重复的单词
#55  字典解析式  56  在重排后的字典中循环。key=lambda x: counts_dict[x]为lambda表达式，以字典中的值作为排序参数
'''
import string
path = '\Python\python代码/测试文本.txt'
with open(path,'r') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    counts_dict = {index:words.count(index) for index in words_index}
    for word in sorted(counts_dict,key=lambda x: counts_dict[x],reverse=True):#将字典的键值对按照键出现次数的多少进行排序
        print('{} -- {} times'.format(word,counts_dict[word]))
'''


'''
#列表
修改：列表名【索引】='修改值'
添加： 末尾添加：列表名.append('元素')
       中间插入：列表名.insert(目标索引，'元素')
删除：知道索引：del语句：del 列表名[索引]
      删除列表末尾元素：方法pop()，并能接着使用该值。
            eg:   list = ['a','b','c']
                  poped_list = list.pop()
                  print(poped_list)
      poped_list = list.pop(索引)可删除任何位置的元素
      跟据值删除：列表名.remove('值')，也可以接着使用
            注意：remove()方法只删除列表中的第一个该值，可用循环将其全部删除
排序：永久性排序：列表名.sort()将列表中的元素按照首字母顺序进行永久性排序
                        向sort()方法传入参数reverse = True，反序排列
      临时排序：函数sorted(列表名),不改变原始的顺序，也可以传入参数。
反转列表：列表名.reverse()   len(列表名)可获知列表名的长度
创建数字列表：使用函数list()将range()的结果直接转换为列表。
                    range(1,6)表示;1,2,3,4,5
                    range(2,11,2)表示2为初始值，每次加2，加到10。
min(列表名);max();sum();
列表解析式，推导式:
            a=[i*2 for i in range(1,11)]  #for前面是我们想要放在列表中的元素，for后面是循环的元素本身
            print(a)
使用列表一部分：切片：
        print(列表名[起始索引：终止索引])。若没有起始索引，则从第一个开始；若没终止索引，则到最后一个结束
复制列表：列表名b = 列表名a[:],a,b为两个不同的列表，改变一个，另一个不受影响
          列表名b = 列表名a,   a,b为两个完全相同的列表，一个变，另一个也变
元组：将列表的方括号改为圆括号，所有值不可以修改，但可以重新定义元组。'''







