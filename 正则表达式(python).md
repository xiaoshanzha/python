# 正则表达式

[TOC]

### 简单匹配
```
首先需要调用一个 python 的内置模块 re.如果 re.search() 找到了结果, 
它会返回一个 match 的 object. 如果没有匹配到, 它会返回 None. 
```
``` python
import re

pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(re.search(pattern1, string))  # <_sre.SRE_Match object; span=(12, 15),match='cat'>
print(re.search(pattern2, string))  # None
```
### 灵活匹配
```
 使用 [] 将可能的字符囊括进来. 比如 [ab] 就说明我想要找的字符可以是 a 也可以是 b. 
 建立正则规则时，在 pattern 的 “” 前面需要加上一个 r 用来表示这是正则表达式, 而不是普通字符串. 
 eg: pattern = r"d[oa]g",表示匹配的字符串为“dog”或“dag”
[A-Z]表示所有大写的英文字母
[0-9a-z]表示可以是数字也可以是任何小写字母.
```

``` python
pattern3 = r"c[ab]t"
string = "dog and pig is cat"
print(re.search(pattern3,string))  # <_sre.SRE_Match object; span=(15, 18), match='cat'>
```
### 字符匹配

![](https://upload-images.jianshu.io/upload_images/10460153-d59264aac3a18a84.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
``` python

print(re.search(r"a.c","abc")) # <_sre.SRE_Match object; span=(0, 3), match='abc'>

print(re.search(r"a\\c","a\c"))  # <_sre.SRE_Match object; span=(0, 3), match='a\\c'>

```

![](https://upload-images.jianshu.io/upload_images/10460153-db088c7968fec153.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

``` python
print(re.search(r"a\dc","a1c"))  # <_sre.SRE_Match object; span=(0, 3), match='a1c'>

print(re.search(r"a\Dc","a1cabc"))  #  <_sre.SRE_Match object; span=(3, 6), match='abc'>

print(re.search(r"a\sc","a1ca c"))  #  <_sre.SRE_Match object; span=(3, 6), match='a c'>

print(re.search(r"a\Sc","a1ca c"))  #  <_sre.SRE_Match object; span=(0, 3), match='a1c'>

print(re.search(r"a\wc","a1ca c"))  #  <_sre.SRE_Match object; span=(0, 3), match='a1c'>

print(re.search(r"a\Wc","a1ca c"))  #  <_sre.SRE_Match object; span=(3, 6), match='a c'>

```
![](https://upload-images.jianshu.io/upload_images/10460153-74fc3d013b2d1c17.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

``` python 

print(re.search(r"^abc","abca c"))  #  <_sre.SRE_Match object; span=(0, 3), match='abc'>

print(re.search(r"^abc","acabc"))  #  None

print(re.search(r"abc$","abcabc"))  #  <_sre.SRE_Match object; span=(3, 6), match='abc'>

print(re.search(r"\Aabc","abcabc"))  #  <_sre.SRE_Match object; span=(0, 3), match='abc'>

print(re.search(r"abc\Z","abcabc"))  #  <_sre.SRE_Match object; span=(3, 6), match='abc'>

print(re.search(r"a\bbc","a!bcabc"))  #  None

print(re.search(r"a\b!bc","a!bcabc"))  #  <_sre.SRE_Match object; span=(0, 4), match='a!bc'>

print(re.search(r"a\Bbc","a!cabc"))  #  <_sre.SRE_Match object; span=(3, 6), match='abc'>
```

```python
若字符串有多行，我们想使用 ^ 形式来匹配行开头的字符，或 $ 匹配行结尾,
用通常的形式是不成功的. 这时候, 我们要使用 另外一个参数, 让 re.search() 可以对每一行单独处理.
这个参数就是 flags=re.M, 或者这样写也行 flags=re.MULTILINE.

string = """
dog run to pig.
you run to pig
"""
print(re.search(r"^you", string))  #  None

print(re.search(r"^you", string, flags=re.M))  #  <_sre.SRE_Match object; span=(17, 20), match='you'>

print(re.search(r"pig.$", string))   #  None

print(re.search(r"pig$", string))   #<_sre.SRE_Match object; span=(17, 20), match='you'>

print(re.search(r"pig$", string, flags=re.M))    #<_sre.SRE_Match object; span=(28, 31), match='pig'>

```
### 重复匹配

![](https://upload-images.jianshu.io/upload_images/10460153-1401e3d04ab59586.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

``` python 
print(re.search(r"abc*","aabcccc"))  #  <_sre.SRE_Match object; span=(1, 7), match='abcccc'>

print(re.search(r"abc+","aabcccc"))  #  <_sre.SRE_Match object; span=(1, 7), match='abcccc'>

print(re.search(r"abc?","abccab"))   #  <_sre.SRE_Match object; span=(0, 3), match='abc'>

print(re.search(r"ab{2}c","abbccabbbc"))  #  <_sre.SRE_Match object; span=(0, 4), match='abbc'>

print(re.search(r"ab{2,3}c","abccabbbc"))  #  <_sre.SRE_Match object; span=(4, 9), match='abbbc'>
```
### 分组匹配
```
我们也可以给需要查找的内容分组，使用 () 来实现 ,

如下所示代码，目标串为：  "一堆数字,Date: 一堆字符"

注意：目标串中空格的数量
```
``` python 
match = re.search(r"(\d+), Date: (.+)", ": 17070142, Date: 22/4/2019")

print(match.group())  #  17070142, Date: 22/4/2019

#用数字找到想要的组

print(match.group(1))  #  17070142

print(match.group(2))  #  22/4/2019

# 若组数很多，用数字很难找到，可以用索引，
# 在括号的开头写上这样的形式 ?P<名字> 就给这个组定义了一个名字. 然后就能用这个名字找到这个组的内容.

match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)", ": 17070142, Date: 22/4/2019")

print(match.group())  #  17070142, Date: 22/4/2019

print(match.group('id'))  #  17070142

print(match.group('date'))  #  22/4/2019

```
### (.*?)惰性匹配
``` python
+ 或 * 后面跟 ？ 表示非贪婪匹配，即尽可能少的匹配，匹配最短的，匹配到就结束一次匹配，不会继续向后匹配

如下为：匹配以a开始，以c结束的字符串，不会出现'abccabdc'的匹配结果

print(re.findall(r"a.*?c","abccabdc"))  # ['abc', 'abdc']

```
### findall()全部匹配
```
前面我们说的都是只找到了最开始匹配上的一项而已, 如果需要找到全部的匹配项, 
我们可以使用 findall 功能. 然后返回一个列表.
```
``` python
print(re.findall(r"p[ia]g", "pig pcg pag"))  #['pig', 'pag']

| 是或者的意思

print(re.findall(r"(pig|pag)", "pig pcg pag"))  # ['pig', 'pag']
```

### split()分割
``` python
#将字符串进行分割，如下所示为遇到 , ; . \ ? 都将进行分割

print(re.split(r"[,;.\\?]","aa,bb;cc.dd\ee?ff*gg"))  # ['aa', 'bb', 'cc', 'dd', 'ee', 'ff*gg']
```

### sub()模式替换
``` python
#通过正则表达式匹配上一些形式的字符串然后再替代掉这些字符串

print(re.sub(r"p[ia]g","dog","pig  and pag is a dog"))   # dog  and dog is a dog
```
