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
buttons=[]
text="yes"

def selection(i):
	text="no"
	Tk.update()


# Buttons and positioning
Button(root, text='Quit', command=lambda: root.quit()).place(x=w*50/100, y=h/1.5)
buttons.append(Button(root, text=text, command=lambda: selection(0)).place(x=w*25/100, y=h/2))
buttons.append(Button(root, text="Center", command=lambda: selection(1)).place(x=w*50/100, y=h/2))
buttons.append(Button(root, text="Right", command=lambda: selection(2)).place(x=w*75/100, y=h/2))
Label(root, text=doors).place(x=w*75/100, y=h/1.6)

if __name__ == "__main__":
    root.mainloop()
