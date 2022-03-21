from tkinter import *

WHITE = "#FFFFFF"

window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=300, height=400, bg=WHITE)
grid_img = PhotoImage(file='grid_img')
canvas.create_image(300, 300, image=grid_img)

# lt = Button(command=press, text="Start")
# lt.grid(column=0, row=0)
# mt = Button(command=press, text="Start")
# mt.grid(column=0, row=1)
# rt = Button(command=press, text="Start")
# rt.grid(column=0, row=2)
# lm = Button(command=press, text="Start")
# lm.grid(column=1, row=0)
# mm = Button(command=press, text="Start")
# mm.grid(column=1, row=1)
# rm = Button(command=press, text="Start")
# rm.grid(column=1, row=2)
# lb = Button(command=press, text="Start")
# lb.grid(column=2, row=0)
# mb = Button(command=press, text="Start")
# mb.grid(column=2, row=1)
# rb = Button(command=press, text="Start")
# rb.grid(column=2, row=2)

window.mainloop()