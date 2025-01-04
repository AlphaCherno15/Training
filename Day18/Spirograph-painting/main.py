from turtle import Turtle, Screen, colormode
import random as rd
import colorgram

rob = Turtle()
rob.shape("arrow")
rob.speed(0)
turtle_colors = [
    "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure",
    "beige", "bisque", "black", "blanchedalmond", "blue",
    "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse",
    "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson",
    "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray",
    "darkgreen", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange",
    "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue",
    "darkslategray", "darkturquoise", "darkviolet", "deeppink", "deepskyblue",
    "dimgray", "dodgerblue", "firebrick", "floralwhite", "forestgreen",
    "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod",
    "gray", "green", "greenyellow", "honeydew", "hotpink",
    "indianred", "indigo", "ivory", "khaki", "lavender",
    "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral",
    "lightcyan", "lightgoldenrodyellow", "lightgreen", "lightgray", "lightpink",
    "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightsteelblue",
    "lightyellow", "lime", "limegreen", "linen", "magenta",
    "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple",
    "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred",
    "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite",
    "navy", "oldlace", "olive", "olivedrab", "orange",
    "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise",
    "palevioletred", "papayawhip", "peachpuff", "peru", "pink",
    "plum", "powderblue", "purple", "red", "rosybrown",
    "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen",
    "seashell", "sienna", "silver", "skyblue", "slateblue",
    "slategray", "snow", "springgreen", "steelblue", "tan",
    "teal", "thistle", "tomato", "turquoise", "violet",
    "wheat", "yellow", "yellowgreen"
]
def colorgb():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    return r, g, b

def color_gram():
    colors = colorgram.extract('image.jpg', 88)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        rgbcolor = (r, g, b)
        rgb_colors.append(rgbcolor)
    return rgb_colors

def draw_objects():
    current_shape = 3
    while current_shape < 11:
        angle = 360 / current_shape
        color = colormode(255)
        rob.pencolor(colorgb())
        for _ in range(current_shape):
            for _ in range(10):
                rob.forward(10)
                rob.penup()
                rob.forward(10)
                rob.pendown()
            rob.left(angle)
        current_shape += 1

def randon_walk():
    color = colormode(1)
    for _ in range(200):
        what_todo = rd.randint(1, 4)
        steps = rd.randint(10, 50)
        color = rd.choice(turtle_colors)
        if what_todo == 1:
            rob.forward(steps)
        elif what_todo == 2:
            rob.back(steps)
        elif what_todo == 3:
            rob.left(90)
        else:
            rob.right(90)
        rob.pencolor(color)

def randon_walk2():
    direction = [0, 90, 180, 270]
    color = colormode(1)
    for _ in range(200):
        steps = rd.randint(10, 50)
        color = rd.choice(turtle_colors)
        rob.forward(steps)
        rob.setheading(rd.choice(direction))
        rob.pencolor(color)

def spirograph(angle):
    rob.pensize(2)
    rob.hideturtle()
    radius = 100
    color = colormode(255)
    for _ in range(3):
        repeat = int(360 / angle)
        for _ in range(repeat):
            rob.pencolor(colorgb())
            rob.circle(radius)
            rob.left(angle)
        angle += 5
        radius *= 1.25

def point_canvas():
    rob.pensize(8)
    cor = color_gram()
    rob.penup()
    rob.hideturtle()
    colormode(255)
    width = 8
    high = 11
    x = -175
    y = -250
    for _ in range(high):
        rob.setx(x)
        rob.sety(y)
        for _ in range(width):
            rob.pencolor(rd.choice(cor))
            rob.dot()
            rob.forward(50)
        y += 50

spirograph(10)
point_canvas()

screen = Screen()
screen.exitonclick()

