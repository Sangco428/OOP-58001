from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Enter your fullname')
        self.txt1=Entry(bd=3)
        self.txt2=Entry()
        self.btn1 = Button(win, text="Click to display")
        self.lbl1.place(x=70, y=50)
        self.txt1.place(x=200, y=50)
        self.txt2.place(x=200, y=100)
        self.b1=Button(win, text='Click to display', command=self.name)
        self.b1.place(x=70, y=100)

    def name(self):
        fname=str(self.txt1.get())
        result= fname
        self.txt2.insert(END, str(result))

window=Tk()
mywin=MyWindow(window)
window.title('Midterm in OOP')
window.geometry("400x300+10+10")
window.mainloop()