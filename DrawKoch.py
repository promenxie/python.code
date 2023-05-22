科赫曲线雪花效果
import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size/3, n-1)
def main():
    turtle.setup(600, 600)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    l = eval(input("请输入科赫曲线的阶数："))
    koch(400, l)
    turtle.right(120)
    koch(400, l)
    turtle.right(120)
    koch(400, l)
    turtle.hideturtle()
    turtle.done()
main()
