import turtle
t = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3= turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t6 = turtle.Turtle()


t.hideturtle()
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
t4.hideturtle()
t5.hideturtle()
t6.hideturtle()

t.speed(0)
t1.speed(0)
t2.speed(0)
t3.speed(0)
t4.speed(0)
t5.speed(0)
t6.speed(0)
############################
#رسم الارض

t.begin_fill()
t.color("lime","limegreen")
t.penup()
t.setposition(-680,-670)
t.pendown()

t.forward(1360)
t.left(90)
t.forward(670)
t.left(90)
t.forward(1360)
t.left(90)
t.forward(670)
t.end_fill()
###############################
#رسم السماء
t.begin_fill()
t.color("cyan","lightblue")
t.penup()
t.setposition(-680,0)
t.pendown()

t.left(90)

t.forward(1360)
t.left(90)
t.forward(670)
t.left(90)
t.forward(1360)
t.left(90)
t.forward(670)
t.end_fill()
######################################
# رسم الفأره

#=========
#رسم القدم
t2.penup()
t2.setposition(220,-170)
t2.pendown()
t2.begin_fill()
t2.color("dimgrey","darkgrey")
t2.forward(95)
t2.left(140)
t2.circle(40,80)
t2.left(280)
t2.circle(38,80)
t2.end_fill()
#--------------------
# رسم الاذنين

t1.penup()
t1.setposition(300,-80)
t1.pendown()
t1.begin_fill()
t1.color("dimgrey","darkgrey")
t1.circle(15)
t1.end_fill()

t1.penup()
t1.setposition(295,-77)
t1.pendown()
t1.begin_fill()
t1.color("dimgrey","pink")
t1.circle(10)
t1.end_fill()
#------------------

t1.penup()
t1.setposition(220,-80)
t1.pendown()
t1.begin_fill()
t1.color("dimgrey","darkgrey")
t1.circle(15)
t1.end_fill()

t1.penup()
t1.setposition(225,-77)
t1.pendown()
t1.begin_fill()
t1.color("dimgrey","pink")
t1.circle(10)
t1.end_fill()
#---------------------
#رسم الجسم
t1.penup()
t1.setposition(300,-100)
t1.pendown()
t1.begin_fill()
t1.color("dimgrey","darkgrey")
t1.left(90)
t1.circle(40,180)
t1.forward(30)
t1.circle(40,180)
t1.forward(30)
t1.end_fill()

t1.penup()
t1.setposition(280,-130)
t1.pendown()
t1.begin_fill()
t1.color("dimgrey","pink")
#t1.left(90)
t1.circle(20,180)
t1.forward(10)
t1.circle(20,180)
t1.forward(10)
t1.end_fill()
#------------------------
#رسم العيون
t1.penup()
t1.setposition(285,-90)
t1.pendown()
t1.begin_fill()
t1.color("dimgrey","black")
t1.circle(7)
t1.end_fill()

t1.penup()
t1.setposition(280,-90)
t1.pendown()
t1.begin_fill()
t1.color("dimgrey","white")
t1.circle(3)
t1.end_fill()

t1.penup()
t1.setposition(250,-90)
t1.pendown()
t1.begin_fill()
t1.color("dimgrey","black")
t1.circle(7)
t1.end_fill()

t1.penup()
t1.setposition(245,-90)
t1.pendown()
t1.begin_fill()
t1.color("dimgrey","white")
t1.circle(3)
t1.end_fill()
#----------------------------
#رسم الانف
t1.penup()
t1.setposition(268,-100)
t1.pendown()
t1.begin_fill()
t1.color("dimgrey","black")
t1.circle(5)
t1.end_fill()

t1.penup()
t1.setposition(263,-102)
t1.pendown()
t1.pencolor("black")
t1.right(180)
t1.width(2)
t1.circle(7,180)

t1.penup()
t1.setposition(263,-102)
t1.pendown()
t1.pencolor("black")
t1.left(180)
t1.width(2)
t1.circle(-7,180)
#---------------------
# رسم الايدينات

t1.penup()
t1.setposition(300,-110)
t1.pendown()
t1.begin_fill()
t1.color("dimgrey","darkgrey")
t1.right(100)
t1.forward(10)
t1.circle(5,180)
t1.forward(13)
t1.end_fill()

t1.penup()
t1.setposition(219,-110)
t1.pendown()
t1.begin_fill()
t1.color("dimgrey","darkgrey")
t1.left(60)
t1.forward(10)
t1.circle(5,180)
t1.forward(6)
t1.end_fill()
#########################################################################
# رسم باندا

# رسم القدمين

t3.penup()
t3.setposition(-110,-190)
t3.pendown()
t3.begin_fill()
t3.color("silver","black")
t3.right(120)
t3.forward(20)
t3.circle(30,190)
t3.forward(30)
t3.end_fill()


t3.penup()
t3.setposition(-40,-210)
t3.pendown()
t3.begin_fill()
t3.color("silver","black")
t3.right(150)
t3.forward(20)
t3.circle(30,190)
t3.forward(20)
t3.end_fill()
#------------------------------------
#رسم الجسم

t4.penup()
t4.setposition(70,-135)
t4.pendown()
t4.begin_fill()
t4.color("silver","black")
t4.right(270)
t4.circle(120,180)
t4.circle(20,180)
t4.penup()
t4.setposition(30,-135)
t4.pendown()
t4.left(180)
t4.circle(20,180)
t4.end_fill()


t4.penup()
t4.setposition(-140,-135)
t4.pendown()
t4.begin_fill()
t4.color("silver","white")
t4.right(180)
t4.circle(90,180)
t4.circle(10,90)
t4.forward(160)
t4.circle(10,90)
t4.end_fill()
#-------------------------------
# رسم الاذانات
t5.penup()
t5.setposition(-110,60)
t5.pendown()
t5.begin_fill()
t5.color("silver","black")
t5.circle(40)
t5.end_fill()

t5.penup()
t5.setposition(10,60)
t5.pendown()
t5.begin_fill()
t5.color("silver","black")
t5.circle(40)
t5.end_fill()
#-------------------------------
# رسم الرأس
t5.penup()
t5.setposition(-50,-70)
t5.pendown()
t5.begin_fill()
t5.color("silver","white")
t5.circle(90)
t5.end_fill()

#-------------------------------
# رسم العيون

t5.penup()
t5.setposition(10,45)
t5.pendown()
t5.begin_fill()
t5.color("silver","black")
t5.left(90)
t5.circle(20,180)
t5.forward(10)
t5.circle(20,180)
t5.forward(10)
t5.end_fill()

t5.penup()
t5.setposition(5,40)
t5.pendown()
t5.begin_fill()
t5.color("silver","white")
t5.circle(15)
t5.end_fill()

t5.penup()
t5.setposition(2,40)
t5.pendown()
t5.begin_fill()
t5.color("silver","black")
t5.circle(10)
t5.end_fill()
#@@@@@@@@@@@@@@@@@@

t5.penup()
t5.setposition(-105,35)
t5.pendown()
t5.begin_fill()

t5.color("silver","black")
t5.left(180)
t5.circle(20,180)
t5.forward(10)
t5.circle(20,180)
t5.forward(10)
t5.end_fill()

t5.penup()
t5.setposition(-100,38)
t5.pendown()
t5.begin_fill()
t5.color("silver","white")
t5.circle(15)
t5.end_fill()

t5.penup()
t5.setposition(-93,38)
t5.pendown()
t5.begin_fill()
t5.color("silver","black")
t5.circle(10)
t5.end_fill()
#---------------------------------
# رسم الانف
t5.penup()
t5.setposition(-40,0)
t5.pendown()
t5.begin_fill()
t5.color("silver","black")
t5.left(90)
t5.circle(7,180)
t5.forward(10)
t5.circle(7,180)
t5.forward(10)
t5.end_fill()

#--------------------------------
# رسم الفم
t5.width(5)
t5.pencolor("black")
t5.penup()
t5.setposition(-45,0)
t5.pendown()
t5.right(90)
t5.forward(10)
t5.circle(10,180)

t5.penup()
t5.setposition(-45,0)
t5.pendown()
t5.right(180)
t5.forward(10)
t5.left(0)
t5.circle(-10,180)



############################################################
# رسم الشمس
t6.penup()
t6.setposition(-200,200)
t6.pendown()
t6.begin_fill()
t6.color("whitesmoke","yellow")
t6.circle(80)
t6.end_fill()


############################################################
turtle.done()