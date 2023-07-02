
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pyglet
import os

pyglet.font.add_file('D:\\programming\\Virtual-Mouse-using-OpenCV-main\\Virtual-Mouse-using-OpenCV-main\\build\\PlayfairDisplay-Black.ttf')


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1152x700")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    571.0,
    703.0,
    fill="#1C4545",
    outline="")

canvas.create_rectangle(
    571.0,
    0.0,
    1152.0,
    700.0,
    fill="#F68802",
    outline="")

canvas.create_rectangle(
    349.0,
    86.0,
    803.0,
    615.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    413.0,
    177.0,
    anchor="nw",
    text="Smart\nBoard",
    fill="#1C4545",
    font=('PlayfairDisplay-Black', 96 * -1)
)



def run():
    print("button1 clicked")
    os.system('start v_m.py')

def derun():
    exit()
    #os.system('stop D:\\programming\\Virtual-Mouse-using-OpenCV-main\\Virtual-Mouse-using-OpenCV-main\\v_m.py')


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: run(),
    relief="flat"
)
button_1.place(
    x=490.0,
    y=411.0,
    width=172,
    height=46
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=496,
    y=525.0,
    width=150.5,
    height=32.88218688964844
)


button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: derun(),
    relief="flat"
)
button_3.place(
    x=490.0,
    y=466.0,
    width=172,
    height=46
)
window.resizable(False, False)
window.mainloop()
