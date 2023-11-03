from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Select Two Functions")
window.geometry('400x500')

style = Style()
style.configure('W.TButton', font=('calibre', 10, 'bold', 'underline'), foreground='red')

func1 = IntVar()
func2 = IntVar()
func3 = IntVar()
func4 = IntVar()
func5 = IntVar()
func6 = IntVar()

c1 = Checkbutton(window, text='SQUARE', variable=func1, onvalue=1, offvalue=0)
c1.pack()
c2 = Checkbutton(window, text='CUBIC', variable=func2, onvalue=1, offvalue=0)
c2.pack()
c3 = Checkbutton(window, text='LOGX', variable=func3, onvalue=1, offvalue=0)
c3.pack()
c4 = Checkbutton(window, text='SINE', variable=func4, onvalue=1, offvalue=0)
c4.pack()
c5 = Checkbutton(window, text='COSINE', variable=func5, onvalue=1, offvalue=0)
c5.pack()
c6 = Checkbutton(window, text='TANGENT', variable=func6, onvalue=1, offvalue=0)
c6.pack()

draw_button = Button(window, text='DRAW', style='W.TButton', command=window.destroy)
draw_button.pack(pady=20)

window.mainloop()
