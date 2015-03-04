from drawingpanel import *
import random
def main():
    panel = DrawingPanel(1200,1200)
    canvas = panel.canvas
    sierpinkski(canvas, 100, 400, 450, 50, 800, 400, 3)

def random_color():
    return '#' + str(random.randint(10,99)) + str(random.randint(10,99)) + str(random.randint(10,99))
def create_triangle(canvas, x, y, x2, y2, x3,y3):
    canvas.create_polygon(x, y, x2, y2, x3, y3, fill = random_color(), width = 1.0, outline = random_color())
def sierpinkski(canvas, x1, y1, x2, y2, x3, y3, n):
    leftx = (x1 + x2) /2
    lefty = (y1 + y2) /2
    rightx = (x1 + x3) /2
    righty = (y1 + y3) /2
    bottomx = (x2 + x3) /2
    bottomy = (y2 + y3) /2
    if(n == 0):
        create_triangle(canvas, x1, y1, x2, y2, x3, y3)
    else:
        sierpinkski(canvas, x1, y1, leftx, lefty, rightx, righty, n - 1)
        sierpinkski(canvas, leftx, lefty, x2, y2, bottomx, bottomy, n - 1)
        sierpinkski(canvas, rightx, righty, bottomx, bottomy, x3, y3, n - 1)

main()
