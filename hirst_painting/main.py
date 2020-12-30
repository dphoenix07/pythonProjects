import colorgram
import turtle as turtle_module
import random

# Extract 20 colors from an image.
# colors = colorgram.extract("iu.jpeg", 20)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

turtle_module.colormode(255)
tim = turtle_module.Turtle()

color_list = [(229, 225, 221),
              (219, 228, 221),
              (230, 221, 225),
              (232, 206, 83),
              (225, 150, 88),
              (216, 223, 229),
              (119, 167, 187),
              (161, 13, 20),
              (32, 110, 159),
              (234, 82, 45),
              (122, 176, 144),
              (172, 19, 14),
              (7, 98, 37),
              (202, 65, 26),
              (186, 186, 26),
              (29, 130, 46),
              (11, 41, 76),
              (14, 64, 40),
              (243, 202, 4),
              (138, 80, 95)]

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()