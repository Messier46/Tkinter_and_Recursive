# Vickerman_Assignment-5_Part-2.py

import tkinter
import tkinter.messagebox

class guiWindow():
    def __init__(self):
        self.mainWindow = tkinter.Tk()
        self.mainWindow.geometry('600x600')

        self.topFrame = tkinter.Frame(self.mainWindow)
        self.bottomFrame = tkinter.Frame(self.mainWindow)

        self.topLabel = tkinter.Label(self.topFrame, text="Welcome to Python", fg='green')

        self.myButton1 = tkinter.Button(self.topFrame, text='Hello', fg='red', font='Arial 30')
        self.myButton2 = tkinter.Button(self.topFrame, text='Hello', fg='blue', font='Impact 14')
        self.myButton3 = tkinter.Button(self.topFrame, text='Hello', fg='yellow', font='Georgia 22')


        self.myButtonB1 = tkinter.Button(self.bottomFrame, text='Click 1')
        self.myButtonB2 = tkinter.Button(self.bottomFrame, text='Click 2')
        self.myButtonB3 = tkinter.Button(self.bottomFrame, text='Click 3')

        self.quitButton = tkinter.Button(self.bottomFrame, text = 'Quit', command= self.mainWindow.destroy)

        self.topLabel.pack(side='top')
        self.myButton1.pack(side='bottom')
        self.myButton2.pack(side='bottom')
        self.myButton3.pack(side='bottom')

        self.myButtonB1.pack(side='left')
        self.myButtonB2.pack(side='left')
        self.myButtonB3.pack(side='left')
        self.quitButton.pack(side='left')

        self.topFrame.pack(side='top')
        self.bottomFrame.pack(side='bottom')

        tkinter.mainloop()

def main():
    myGui = guiWindow()

if __name__ == '__main__':
    main()