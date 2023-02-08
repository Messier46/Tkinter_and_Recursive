# Vickerman_Assignment-5_Part-5.py

import tkinter
import tkinter.messagebox

class myGUI:
    re = ''
    def __init__(self) -> None:

        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry('600x600')

        self.topFrame = tkinter.Frame(self.mainWindow)
        self.bottomFrame = tkinter.Frame(self.mainWindow)

        self.canvas = tkinter.Canvas(self.topFrame,width=300,height=200)
        self.canvas.pack()

        self.rdbShape = tkinter.IntVar()
        self.cbVar = tkinter.IntVar()
        # self.cbFill2 = tkinter.IntVar()

        self.rdbShape1 = tkinter.Radiobutton(self.topFrame, text='Rectangle', variable=self.rdbShape, value=1, command=self.reShape1)
        self.rdbShape2 = tkinter.Radiobutton(self.topFrame, text='Oval', variable=self.rdbShape, value=2, command=self.reShape2)

        self.cbFill1 = tkinter.Checkbutton(self.bottomFrame, text='Fill', variable= self.cbVar, command=self.fillCheck)
        # self.cbFill2 = tkinter.Checkbutton(self.bottomFrame, text='Oval', variable= self.cbFill2)

        self.quitButton = tkinter.Button(self.bottomFrame, text='Quit', command= self.mainWindow.destroy)

        self.rdbShape1.pack()
        self.rdbShape2.pack()
        self.cbFill1.pack()
        # self.cbFill2.pack()


        self.quitButton.pack(side='left')

        self.topFrame.pack()
        self.bottomFrame.pack()

        tkinter.mainloop()

    def reShape1(self):
        self.displayClear()
        self.re = self.canvas.create_rectangle(20,20,280,180, tags='rect' )
        self.fillCheck()
    def reShape2(self):
        self.displayClear()
        self.re = self.canvas.create_oval(40,40,180,100, tags='oval')
        self.fillCheck()
    def displayClear(self):
        self.canvas.delete('rect', 'oval')
    
    def fillCheck(self):
        if self.cbVar.get() == 1:
            self.canvas.itemconfig(self.re, fill='red')
        else:
            self.canvas.itemconfig(self.re, fill='')

def main():
    myGui = myGUI()

if __name__ == '__main__':
    main()