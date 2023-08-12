from tkinter import *

canvas_color = "white"
pen_color = "black"
pen_size = 2
tool = "pen"

# 캔버스에 그림 그리는 함수
def paint(event): 
    global pen_size, pen_color
    x1, y1 = event.x, event.y
    x2, y2 = event.x + pen_size, event.y + pen_size
    canvas.create_line(x1, y1, x2, y2, width = pen_size, fill = pen_color)

# 색깔 변경 함수
def change_color(color) :
    global pen_color, tool
    if tool == "pen" :
        pen_color = color
        btn_pen['bg'] = pen_color
        if pen_color == "white" or pen_color == "yellow":
            btn_pen['fg'] = "black"
        if pen_color == "black" :
            btn_pen['fg'] = "white"
    else :
        canvas_color = color
        btn_canvas['bg'] = canvas_color
        canvas['bg'] = canvas_color
        if canvas_color == "white" or canvas_color == "yellow":
            btn_canvas['fg'] = "black"
        if canvas_color == "black" :
            btn_canvas['fg'] = "white"

# 도구 변경 함수
def change_tool(t) :
    global tool
    tool = t
    
# 펜 크기 변경 함수
def change_size(btn) :
    global pen_size
    if btn == "plus" :
        pen_size += 1
    else :
        pen_size -= 1

# 캔버스 초기화하는 함수
def clear_canvas() :
    canvas.delete("all")

w, h = 11, 2

win = Tk()
win.title("My paint")
win.geometry("525x555+200+200")
canvas = Canvas(win, width = 522, height = 470, bg = "white")
canvas.bind("<B1-Motion>", paint)    # 마우스 왼쪽 버튼을 누르면서 움직일 때

btn_white = Button(win, text = "white", bg = "white", width = w, height = h, command = lambda : change_color("white"))
btn_black = Button(win, text = "black", bg = "black", fg = "white", width = w, height = h, command = lambda : change_color("black"))
btn_blue = Button(win, text = "blue", bg = "blue",  fg = "white", width = w, height = h, command = lambda : change_color("blue"))
btn_green = Button(win, text = "green", bg = "green",  fg = "white", width = w, height = h, command = lambda : change_color("green"))
btn_yellow = Button(win, text = "yellow", bg = "yellow", width = w, height = h, command = lambda : change_color("yellow"))
btn_red = Button(win, text = "red", bg = "red",  fg = "white", width = w, height = h, command = lambda : change_color("red"))

btn_canvas = Button(win, text = "canvas\ncolor", bg = "white", fg = "black", width = w, height = h, command = lambda : change_tool("canvas"))
btn_pen = Button(win, text = "pen\ncolor", bg = "black", fg = "white", width = w, height = h, command = lambda : change_tool("pen"))

btn_plus = Button(win, text = "+", bg = "white", width = w, height = h, command = lambda : change_size("plus"))
btn_minus = Button(win, text = "-", bg = "white", width = w, height = h, command = lambda : change_size("minus"))
btn_clear = Button(win, text = "clear", bg = "white", width = w, height = h, command = clear_canvas)

canvas.grid(row = 0, column = 0, columnspan = 6)
btn_canvas.grid(row = 1, column = 0)
btn_black.grid(row = 1, column = 1)
btn_blue.grid(row = 1, column = 2)
btn_green.grid(row = 1, column = 3)
btn_plus.grid(row = 1, column = 4)
btn_pen.grid(row = 2, column = 0)
btn_white.grid(row = 2, column = 1)
btn_red.grid(row = 2, column = 2)
btn_yellow.grid(row = 2, column = 3)
btn_minus.grid(row = 2, column = 4)
btn_clear.grid(row = 2, column = 5)

win.mainloop()
