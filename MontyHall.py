from tkinter import *

# root window
root = Tk()
w = int(root.winfo_screenwidth()/3.5)
h = int(root.winfo_screenheight()/3)
root.geometry(f"{w}x{h}")
root.resizable(False, False)
root.title('Button Demo')

def selection():
	

# exit button
Button(root, text='Quit', command=lambda: root.quit()).place(x=w*50/100, y=h/1.5)
Button(root, text="Left", command=selection("left")).place(x=w*25/100, y=h/2)
Button(root, text="Center").place(x=w*50/100, y=h/2)
Button(root, text="Right").place(x=w*75/100, y=h/2)

root.mainloop()