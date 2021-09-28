import turtle as t
import random

tim = t.Turtle()
tim.speed(5)
tim.pensize(5)

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def choose_color():
  tim.color(colours[random.randint(0,7)])

def choose_movement(num):
  if num == 0:
    tim.forward(10)
  if num == 1:
    tim.right(90)
    tim.forward(10)
  if num == 2:
    tim.left(90)
    tim.forward(10)
  if num == 3:
    tim.backward(10)

for i in range (0,255):
  choose_color()
  choose_movement(random.randint(0,4))