#用turtle库绘制蟒蛇图形
import turtle
turtle.setup(650,350,200,200)
turtle.penup()#提起笔移动，不绘制图形，用于另起一个地方绘制
turtle.fd(-250)#直线爬行，正的为向左，负的为向右爬行
turtle.pendown()#放下画笔，开始作图
turtle.pensize(25)#设置画笔宽度
turtle.pencolor("purple")#设置画笔颜色
turtle.seth(-40)#设置画笔的起始角度
for i in range(4):
    turtle.circle(40,80)  #turtle.circle(半径，圆弧度)
    turtle.circle(-40,80)#半径为正(负)，表示圆心在画笔的左边(右边)画圆；
turtle.circle(40,80/2)
turtle.fd(40) #表示直线爬行40个像素
turtle.circle(-16,180)
turtle.fd(40 * 2/3)


# 绘制五角星
import turtle
turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("red")
turtle.begin_fill()  #准备开始填充图形
for _ in range(5):
    turtle.forward(200)
    turtle.right(144) #顺时针移动144度，left为逆时针移动
turtle.end_fill()   #填充完成。
turtle.penup()
turtle.goto(-150, -120)  #将画笔移动到x,y的位置
turtle.color("violet")
turtle.write("Done", font=('Arial', 40, 'normal'))

turtle.mainloop()

'''
circle(50) # 整圆;
circle(50,steps=3) # 三角形;
circle(120, 180) # 半圆
turtle.speed()：设置绘制的速度，1-10，1最慢，10最快；

turtle.clear()  #清空turtle窗口，但是turtle的位置和状态不会改变
turtle.reset()   #清空窗口，重置turtle状态为起始状态

turtle.write(s,font=(“font-name”,font_size,”font_type”))：写文本，s为文本内容，font是字体的参数，里面分别为字体名称，大小和类型；
turtle.hideturtle()：隐藏箭头显示；
'''
#绘制小猪配奇
import turtle as t

t.pensize(4)
t.hideturtle()
t.colormode(255)
t.color((255,155,192),"pink")
t.setup(840,500)
t.speed(10)

#鼻子
t.pu()
t.goto(-100,100)
t.pd()
t.seth(-30)
t.begin_fill()
a=0.4
for i in range(120):
    if 0<=i<30 or 60<=i<90:
        a=a+0.08
        t.lt(3) #向左转3度
        t.fd(a) #向前走a的步长
    else:
        a=a-0.08
        t.lt(3)
        t.fd(a)
t.end_fill()

t.pu()
t.seth(90)
t.fd(25)
t.seth(0)
t.fd(10)
t.pd()
t.pencolor(255,155,192)
t.seth(10)
t.begin_fill()
t.circle(5)
t.color(160,82,45)
t.end_fill()

t.pu()
t.seth(0)
t.fd(20)
t.pd()
t.pencolor(255,155,192)
t.seth(10)
t.begin_fill()
t.circle(5)
t.color(160,82,45)
t.end_fill()

#头
t.color((255,155,192),"pink")
t.pu()
t.seth(90)
t.fd(41)
t.seth(0)
t.fd(0)
t.pd()
t.begin_fill()
t.seth(180)
t.circle(300,-30)
t.circle(100,-60)
t.circle(80,-100)
t.circle(150,-20)
t.circle(60,-95)
t.seth(161)
t.circle(-300,15)
t.pu()
t.goto(-100,100)
t.pd()
t.seth(-30)
a=0.4
for i in range(60):
    if 0<=i<30 or 60<=i<90:
        a=a+0.08
        t.lt(3) #向左转3度
        t.fd(a) #向前走a的步长
    else:
        a=a-0.08
        t.lt(3)
        t.fd(a)
t.end_fill()

#耳朵
t.color((255,155,192),"pink")
t.pu()
t.seth(90)
t.fd(-7)
t.seth(0)
t.fd(70)
t.pd()
t.begin_fill()
t.seth(100)
t.circle(-50,50)
t.circle(-10,120)
t.circle(-50,54)
t.end_fill()

t.pu()
t.seth(90)
t.fd(-12)
t.seth(0)
t.fd(30)
t.pd()
t.begin_fill()
t.seth(100)
t.circle(-50,50)
t.circle(-10,120)
t.circle(-50,56)
t.end_fill()

#眼睛
t.color((255,155,192),"white")
t.pu()
t.seth(90)
t.fd(-20)
t.seth(0)
t.fd(-95)
t.pd()
t.begin_fill()
t.circle(15)
t.end_fill()

t.color("black")
t.pu()
t.seth(90)
t.fd(12)
t.seth(0)
t.fd(-3)
t.pd()
t.begin_fill()
t.circle(3)
t.end_fill()

t.color((255,155,192),"white")
t.pu()
t.seth(90)
t.fd(-25)
t.seth(0)
t.fd(40)
t.pd()
t.begin_fill()
t.circle(15)
t.end_fill()

t.color("black")
t.pu()
t.seth(90)
t.fd(12)
t.seth(0)
t.fd(-3)
t.pd()
t.begin_fill()
t.circle(3)
t.end_fill()

#腮
t.color((255,155,192))
t.pu()
t.seth(90)
t.fd(-95)
t.seth(0)
t.fd(65)
t.pd()
t.begin_fill()
t.circle(30)
t.end_fill()

#嘴
t.color(239,69,19)
t.pu()
t.seth(90)
t.fd(15)
t.seth(0)
t.fd(-100)
t.pd()
t.seth(-80)
t.circle(30,40)
t.circle(40,80)

#身体
t.color("red",(255,99,71))
t.pu()
t.seth(90)
t.fd(-20)
t.seth(0)
t.fd(-78)
t.pd()
t.begin_fill()
t.seth(-130)
t.circle(100,10)
t.circle(300,30)
t.seth(0)
t.fd(230)
t.seth(90)
t.circle(300,30)
t.circle(100,3)
t.color((255,155,192),(255,100,100))
t.seth(-135)
t.circle(-80,63)
t.circle(-150,24)
t.end_fill()

#手
t.color((255,155,192))
t.pu()
t.seth(90)
t.fd(-40)
t.seth(0)
t.fd(-27)
t.pd()
t.seth(-160)
t.circle(300,15)
t.pu()
t.seth(90)
t.fd(15)
t.seth(0)
t.fd(0)
t.pd()
t.seth(-10)
t.circle(-20,90)

t.pu()
t.seth(90)
t.fd(30)
t.seth(0)
t.fd(237)
t.pd()
t.seth(-20)
t.circle(-300,15)
t.pu()
t.seth(90)
t.fd(20)
t.seth(0)
t.fd(0)
t.pd()
t.seth(-170)
t.circle(20,90)

#脚
t.pensize(10)
t.color((240,128,128))
t.pu()
t.seth(90)
t.fd(-75)
t.seth(0)
t.fd(-180)
t.pd()
t.seth(-90)
t.fd(40)
t.seth(-180)
t.color("black")
t.pensize(15)
t.fd(20)

t.pensize(10)
t.color((240,128,128))
t.pu()
t.seth(90)
t.fd(40)
t.seth(0)
t.fd(90)
t.pd()
t.seth(-90)
t.fd(40)
t.seth(-180)
t.color("black")
t.pensize(15)
t.fd(20)

#尾巴
t.pensize(4)
t.color((255,155,192))
t.pu()
t.seth(90)
t.fd(70)
t.seth(0)
t.fd(95)
t.pd()
t.seth(0)
t.circle(70,20)
t.circle(10,330)
t.circle(70,30)
t.done()