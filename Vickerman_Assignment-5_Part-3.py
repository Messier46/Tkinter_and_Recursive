# Vickerman_Assignment-5_Part-3.py

import tkinter
import tkinter.messagebox

class guiWindow():

    def __init__(self):
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title('Calculator')
        self.mainWindow.geometry('300x400')

        self.topFrame = tkinter.Frame(self.mainWindow)
        self.bottomFrame = tkinter.Frame(self.mainWindow)
        
        self.ValueLabel1 = tkinter.Label(self.topFrame, text='Enter value one')
        self.Box1 = tkinter.Entry(self.topFrame, width=10)
        self.ValueLabel2 = tkinter.Label(self.topFrame, text='Enter value two')
        self.Box2 = tkinter.Entry(self.topFrame, width=10)
        self.TotalLabel = tkinter.Label(self.bottomFrame, text='Total')
        self.value = tkinter.StringVar()
        self.resultLabel = tkinter.Label(self.bottomFrame, textvariable=self.value)
        
        self.PlusButton = tkinter.Button(self.bottomFrame, text='+', command=self.add)
        self.MinusButton = tkinter.Button(self.bottomFrame, text='-', command=self.subtract)
        self.MultiplyButton = tkinter.Button(self.bottomFrame, text='*', command=self.multiply)
        self.DivideButton = tkinter.Button(self.bottomFrame, text='/', command=self.divide)
        self.quitButton = tkinter.Button(self.bottomFrame, text='Quit', command=self.mainWindow.destroy)



        self.ValueLabel1.grid(row=1, column=1)
        self.Box1.grid(row=1, column=2)
        self.ValueLabel2.grid(row=2, column=1)
        self.Box2.grid(row=2, column=2)
        self.TotalLabel.grid(row=6, column=1)
        self.resultLabel.grid(row=6, column=2)
        self.PlusButton.grid(row=7, column=2)
        self.MinusButton.grid(row=7, column=3)
        self.MultiplyButton.grid(row=7, column=4)
        self.DivideButton.grid(row=7, column=5)
        self.quitButton.grid(row=8, column=1)

        self.topFrame.pack()
        self.bottomFrame.pack()

        tkinter.mainloop()

    def add(self):
        try:
            box1 = float(self.Box1.get())
            box2 = float(self.Box2.get())
        
            self.value.set(f'{box1 + box2}')

        except:
            self.value.set(f'N/A')

    def subtract(self):
        try:
            box1 = float(self.Box1.get())
            box2 = float(self.Box2.get())
        
            self.value.set(f'{box1 - box2}')
            
        except:
            self.value.set(f'N/A')
    def multiply(self):
        try:
            box1 = float(self.Box1.get())
            box2 = float(self.Box2.get())
        
            self.value.set(f'{box1 * box2}')
            
        except:
            self.value.set(f'N/A')
    def divide(self):
        try:
            box1 = float(self.Box1.get())
            box2 = float(self.Box2.get())
        
            if box2 != 0:
                self.value.set(f'{box1 / box2}')
            else:
                self.value.set(f'N/A')
        except:
            self.value.set(f'N/A')






def main():
    myGUI = guiWindow()

if __name__ == "__main__":
    main()