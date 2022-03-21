from tkinter import *

WHITE = "#FFFFFF"
BUTTON_PADX = 30
BUTTON_PADY = 32
BUTTON_WIDTH = 20

window = Tk()
window.title("Tic Tac Toe")
window.config(padx=50, pady=50, bg=WHITE)

blank_img = PhotoImage(file='blank.png')
circle_img = PhotoImage(file='circle.png')
cross_img = PhotoImage(file='cross.png')

canvas = Canvas(width=600, height=600, bg=WHITE)
grid_img = PhotoImage(file='grid.png')
canvas.create_image(250, 250, image=grid_img)
canvas.place(x=0, y=0)

active = [None, None]


class Btn:
    def __init__(self, i, j):
        self.placement = [i, j]
        self.grid_btn = Button(command=self.press, image=blank_img)
        self.grid_btn.grid(padx=BUTTON_PADX, pady=BUTTON_PADY, column=i, row=j)

    def press(self):
        print(self.placement)


for i in range(3):
    for j in range(3):
        button = Btn(i, j)

window.mainloop()
