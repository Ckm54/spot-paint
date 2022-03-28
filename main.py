# import colorgram
import random
import turtle
import turtle as t

# rgb_colors = []
# colors = colorgram.extract('spots.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
turtle.colormode(255)
drawer = t.Turtle()
drawer.speed("fastest")
drawer.penup()
color_list = [(239, 234, 226), (220, 158, 84), (39, 109, 150), (120, 163, 191), (150, 63, 87), (217, 232, 222), (203, 134, 157), (180, 160, 34), (32, 131, 95), (122, 179, 152), (235, 218, 225), (161, 79, 52), (213, 87, 61), (197, 85, 112), (208, 223, 231), (229, 199, 114), (57, 166, 135), (141, 33, 42), (8, 104, 80), (47, 158, 182), (234, 163, 181), (117, 115, 162), (32, 62, 111), (236, 171, 157), (126, 38, 34), (156, 210, 197), (32, 57, 78), (70, 41, 37), (25, 65, 56), (74, 37, 47)]

drawer.setheading(225)
drawer.forward(300)
drawer.setheading(0)
num_dots = 100

for dot_count in range(1, num_dots + 1):
    drawer.dot(20, random.choice(color_list))
    drawer.forward(50)

    if dot_count % 10 == 0:
        drawer.setheading(90)
        drawer.forward(50)
        drawer.setheading(180)
        drawer.forward(500)
        drawer.setheading(0)

screen = t.Screen()
screen.exitonclick()


