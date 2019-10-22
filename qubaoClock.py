# -*- encoding: utf-8 -*-
'''
@File    :   qubaoClock.py
@Time    :   2019/10/23 02:59:28
@Author  :   Jerry Lee
@Version :   1.0
@Desc    :   draw clock with turtle
'''
import turtle
from datetime import *
  
# 操作画笔，向前运动一段距离放下
def Move(step):
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()

# 注册Turtle形状，建立表针Turtle
def mkHand(name, length):
    turtle.reset()
    Move(-length * 0.1)
    turtle.begin_poly()
    turtle.forward(length * 1.1)
    turtle.end_poly()
    handForm = turtle.get_poly()
    turtle.register_shape(name, handForm)

# 建立三个表针Turtle并初始化
def Init():
    global secHand, minHand, hurHand, printer
    turtle.mode("logo")
    mkHand("secHand", 135)
    mkHand("minHand", 125)
    mkHand("hurHand", 90)
    secHand = turtle.Turtle()
    secHand.color('orange')
    secHand.shape("secHand")
    minHand = turtle.Turtle()
    minHand.color('blue')
    minHand.shape("minHand")
    hurHand = turtle.Turtle()
    hurHand.color('red')
    hurHand.shape("hurHand")
    
    for hand in secHand, minHand, hurHand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)

    printer = turtle.Turtle()
    printer.hideturtle()
    printer.penup()

# 建立表的外框   
def SetupClock(radius):
    turtle.reset()
    turtle.pensize(7)
    for i in range(60):
        Move(radius)
        if i % 5 == 0:
            turtle.forward(20)
            Move(-radius - 20)
            
            Move(radius + 20)
            if i == 0:
                turtle.write(int(12), align="center", font=("微软雅黑", 15, "bold"))
            elif i == 30:
                Move(25)
                turtle.write(int(i/5), align="center", font=("微软雅黑", 15, "bold"))
                Move(-25)
            elif (i == 25 or i == 35):
                Move(20)
                turtle.write(int(i/5), align="center", font=("微软雅黑", 15, "bold"))
                Move(-20)
            else:
                turtle.write(int(i/5), align="center", font=("微软雅黑", 15, "bold"))
            Move(-radius - 20)
        else:
            turtle.dot(5)
            Move(-radius)
        turtle.right(6)

# 星期         
def Week(t):  
    week = ["Monday", 
            "Tuesday", 
            "Wednesday",
            "Thursday", 
            "Friday", 
            "Saturday", 
            "Sunday"]
    return week[t.weekday()]

# 日期  
def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s/%d/%d" % (y, m, d)

# 动态显示表针
def Tick():
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    
    secHand.setheading(6 * second)
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)
    
    turtle.tracer(False)
    printer.forward(65)
    printer.write(Week(t), align="center",
                  font=("Century", 18, "normal"))
    printer.back(130)
    printer.write(Date(t), align="center",
                  font=("Century", 16, "normal"))
    printer.home()
    turtle.tracer(True)

    turtle.ontimer(Tick, 100)

# 显示祝福文字
def DrawWord():
	turtle.penup()
	turtle.goto(330, 200)
	turtle.pendown()
	turtle.color("green")
	turtle.hideturtle()
	turtle.penup()
	turtle.write("趣宝祝各位程序猿/媛们节日快乐!\n\n", align="right", font=("微软雅黑", 20, "bold"))
	turtle.write("by Jerry Lee", align="right", font=("Century", 16, "normal"))
 
def main():
    turtle.bgpic(r'qubao.png')
    turtle.tracer(False)
    Init()
    SetupClock(160)
    turtle.tracer(True)
    Tick()
    DrawWord()
    turtle.mainloop()
  
if __name__ == "__main__":
    main()