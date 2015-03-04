from drawingpanel import *
def main():
    panel = DrawingPanel(750,500)
    canvas = panel.canvas
    sierpinkski(canvas, 400, 100, 450, 50, 500, 100, 1)
    
def create_triangle(canvas, x, y, x2, y2, x3,y3):
    canvas.create_polygon(x, y, x2, y2, x3, y3, fill = "pink", width = '1.0', outline = 'black')

def remove_triangle(canvas, x, y, x2, y2, x3,y3):
    canvas.create_polygon(x, y, x2, y2, x3, y3, fill = "white")

def sierpinkski(canvas, x1, y1, x2, y2, x3, y3, n):
    if n == 0:
        create_triangle(canvas, x1, y1, x2, y2, x3, y3)
        pass
    else:
        remove_triangle(canvas, x1, y1, x2, y2, x3, y3)
        sierpinkski(canvas, (x1+x2)/2, (y1+y2)/2, (x2+x3)/2, (y2+y3)/2, (x1+x3)/2, (y1+y3)/2, n-1)
main()
