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


class Grid:
    def __init__(self):
        self.values = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def check_hzn(self, i):
        return self.values[i][0] == self.values[i][1] and self.values[i][1] == self.values[i][2]

    def check_vrt(self, i):
        return self.values[0][i] == self.values[1][i] and self.values[1][i] == self.values[2][i]

    def check_cross(self, i):
        if i % 2 == 1:
            return False
        elif i == 2:
            return self.values[0][2] == self.values[1][1] and self.values[1][1] == self.values[2][0] and \
                   self.values[0][2] != 0
        else:
            return self.values[0][0] == self.values[1][1] and self.values[1][1] == self.values[2][2] and \
                   self.values[2][2] != 0

    def check_value(self, i, j):
        if self.values[i][j] == 0:
            return True
        else:
            return False

    def change_value(self, i, j, value):
        self.values[i][j] = value

    def print(self):
        print(self.values[0])
        print(self.values[1])
        print(self.values[2])


logic = Grid()


class Btn:
    def __init__(self, i, j):
        self.row = j
        self.column = i
        self.grid_btn = Button(command=self.press, image=blank_img)
        self.grid_btn.grid(padx=BUTTON_PADX, pady=BUTTON_PADY, column=i, row=j)

    def press(self):
        if logic.check_value(self.row, self.column):
            self.grid_btn.configure(image=cross_img)
            logic.change_value(self.row, self.column, 5)
            logic.print()
            print(f"{self.row} {self.column}")
            if logic.check_hzn(self.row) or logic.check_vrt(self.column) or logic.check_cross(self.row+self.column):
                print('You Win!')
                print(logic.check_hzn(self.row))
                print(logic.check_vrt(self.column))
                print(logic.check_cross(self.row+self.column))
        else:
            print("Error")


for i in range(3):
    for j in range(3):
        button = Btn(i, j)

window.mainloop()
