from turtle import *
from math import *
import tkinter as TK

speed(0)
bgcolor("black")
goto(0,-40)

# Draw leaves
for i in range(16):
    for j in range(18):
        color('#FFA216'), rt(90)
        circle(150-j*6, 90), lt(90)
        circle(150-j*6, 90), rt(180)
    circle(40,24)

# Draw flower center
color('black') 
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')
golden_ang = 137.508
phi = golden_ang*(pi/180)

for i in range(140):
    r = 4*sqrt(i)
    theta = i*phi
    x = r*cos(theta)
    y = r*sin(theta)
    penup(), goto(x, y)
    setheading(i*golden_ang)
    pendown(), stamp()

# Define points to draw letters
def point(x, y):
    penup(), goto(x, y), pendown()
    color('black'), fillcolor('#FFA216')
    begin_fill(), circle(4), end_fill()

# Función para dibujar la letra 'M'
def draw_M(x, y):
    positions_m = [
        (x, y), (x, y+6), (x, y+12), (x, y+18), (x, y+24), (x, y+30),
        (x+6, y+24), (x+12, y+18), (x+18, y+24),
        (x+24, y+30), (x+24, y+24), (x+24, y+18), (x+24, y+12), (x+24, y+6), (x+24, y)
    ]
    for pos in positions_m:
        point(*pos)

# Function to draw 'I'
def draw_I(x, y):
    positions_l = [(x, y+30), (x, y+24), (x, y+18), (x, y+12), (x, y+6), (x, y),
                   ]
    for pos in positions_l:
        point(*pos)

# Function to draw 'A'
def draw_A(x, y):
    # Lado izquierdo de la "A"
    positions_a = [
        (x, y), (x+4, y+6), (x+6, y+12), (x+8, y+18), (x+10, y+24),
        (x+10, y+24), (x+12, y+18),(x+14, y+12), (x+16, y+6),(x+18, y),
        # (x, y+24), (x+8, y+18), (x+12, y+12), (x+18, y+6), (x+24, y)  # Lado derecho de la "A"
    ]
    
    # Línea horizontal del medio de la "A"
    middle_line = [(x+6, y+12), (x+12, y+12), (x+18, y+12)]

    # Dibuja los puntos de la "A"
    for pos in positions_a:
        point(*pos)
        
    # Dibuja la línea horizontal del medio
    for pos in middle_line:
        point(*pos)


# Function to draw 'R'
def draw_R(x, y):
    positions_r = [(x, y+30), (x+6, y+30), (x+12, y+30), (x+18, y+30),
                   (x, y+24), (x, y+18), (x, y+12), (x, y+6), (x, y),
                   (x+6, y+24), (x+12, y+24), (x+18, y+24), (x+18, y+18),
                   (x+12, y+18), (x+6, y+18), (x+12, y+12), (x+18, y+6), (x+24, y)]
    for pos in positions_r:
        point(*pos)

draw_M(-70, -20)
draw_A(-40, -20)
draw_I(-14, -20)
draw_R(-5, -20)
draw_A(20, -20)
hideturtle()
done()