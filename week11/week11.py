# def fizz_buzz(n):
#     for i in range(1,n+1):
#         if i % 15 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
# fizz_buzz(16)
# def digit_sum(n):
#     total = 0
#     while n > 0:
#         total = total + n % 10
#         n = n // 10
#     return total
# print(digit_sum(1234))
# def alternate_case(s):
#     result = ""
#     for i in range(len(s)):
#         if i % 2 == 0:
#             result = result + s[i].upper()
#         else:
#             result = result + s[i].lower()
#     return result
# print(alternate_case("Ispanakdiskolandırma"))
# import turtle
# def draw_polygon(t, sides, lenght):
#     for i in range(sides):
#         t.forward(lenght)
#         t.left(360/sides)
#
# screen = turtle.Screen()
# screen.bgcolor("pink")
# t = turtle.Turtle()
# t.pensize(3)
# colors = ["hot pink", "purple", "magenta"]
# for i in range(3):
#     t.penup()
#     t.goto(-150 + i*120,-30)
#     t.pendown()
#     t.color(colors[i])
#     draw_polygon(t, i+3 , 60)
#
# screen.exitonclick()
# import turtle
# def fiiled_squate(t,size,color):
#     t.fillcolor(color)
#     t.begin_fill()
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#     t.end_fill()
#
# wn = turtle.Screen()
# wn.bgcolor("pink")
# t = turtle.Turtle()
#
# for i in range(5):
#     t.penup()
#     t.goto(-165 + i*70,-25)
#     t.pendown()
#     if i %2 == 0:
#         fiiled_squate(t,50,"purple")
#     else:
#         fiiled_squate(t,50,"hotpink")
# wn.exitonclick()
# import turtle
#
#
# def draw_square(t,size):
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
# wn = turtle.Screen()
# wn.bgcolor("pink")
# t = turtle.Turtle()
# t.pensize(2)
# t.color("hotpink")
# for i in range(12):
#     draw_square(t,80)
#     t.left(30)
#
# wn.exitonclick()
# import turtle
# def draw_square(t,size,filled):
#     if filled:
#         t.begin_fill()
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#     if filled:
#         t.end_fill()
#
# wn=turtle.Screen()
# wn.bgcolor("pink")
# t = turtle.Turtle()
# size = 40
# for row in range(6):
#     for col in range(6):
#         t.penup()
#         t.goto(-120 + col * size , -120 + row * size )
#         t.pendown()
#         draw_square(t, size, (row + col) % 2 == 0 )
#
# wn.exitonclick()