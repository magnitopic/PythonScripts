from tkinter import *
import random

# root window
root = Tk()
w = int(root.winfo_screenwidth()/3.5)
h = int(root.winfo_screenheight()/3)
root.geometry(f"{w}x{h}")
root.resizable(False, False)
root.title('Button Demo')
# vars
doors = [0]*3
doors[random.randrange(3)] = 1
roundNum = 0


def selection(i, button):
	""" if roundNum % 2:

		roundNum += 1
	if doors[i]: """
	button.config(text="Presed")


# Buttons and positioning
Button(root, text='Quit', command=lambda: root.quit()).place(x=w*50/100, y=h/1.5)
one = Button(root, text="Left", command=lambda: selection(0, one)).place(x=w*25/100, y=h/2)
two = Button(root, text="Center", command=lambda: selection(1, two)).place(x=w*50/100, y=h/2)
tree = Button(root, text="Right", command=lambda: selection(2, tree)).place(x=w*75/100, y=h/2)
Label(root, text=doors).place(x=w*75/100, y=h/1.6)

if __name__ == "__main__":
    root.mainloop()
