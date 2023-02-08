# Vickerman_Assignment-5_Part-4.py

import tkinter
import tkinter.messagebox

class guiWindow():
    def __init__(self):
        self.processor = 0
        self.memory = 0
        self.HDD = 0
        self.monitor = 0

        self.mainWindow = tkinter.Tk()
        self.mainWindow.title('Computer Picking')
        self.mainWindow.geometry('400x200')

        self.topFrame = tkinter.Frame(self.mainWindow)
        self.middleFrame = tkinter.Frame(self.mainWindow)
        self.bottomFrame = tkinter.Frame(self.mainWindow)

        
        self.valueProc = tkinter.IntVar()
        self.valueMem = tkinter.IntVar()
        self.valueHDD = tkinter.IntVar()
        self.valueMon = tkinter.IntVar()



        self.proc1 = tkinter.Radiobutton(self.middleFrame, text='Intel Core i5 ($250)', variable=self.valueProc, value=1, command=self.procMethod1)
        self.proc2 = tkinter.Radiobutton(self.middleFrame, text='Intel Core i7 ($350)', variable=self.valueProc, value=2, command=self.procMethod2)

        self.mem1 = tkinter.Radiobutton(self.middleFrame, text='16GB ($150)', variable=self.valueMem, value=1, command=self.memMethod1)
        self.mem2 = tkinter.Radiobutton(self.middleFrame, text='32GB ($250)', variable=self.valueMem, value=2, command=self.memMethod2)

        self.HDD1 = tkinter.Radiobutton(self.middleFrame, text='512GB ($100)', variable=self.valueHDD, value=1, command=self.hddMethod1)
        self.HDD2 = tkinter.Radiobutton(self.middleFrame, text='1TB ($150)', variable=self.valueHDD, value=2, command=self.hddMethod2)
        self.HDD3 = tkinter.Radiobutton(self.middleFrame, text='2TB ($225)', variable=self.valueHDD, value=3, command=self.hddMethod3)

        self.monitor1 = tkinter.Radiobutton(self.middleFrame, text='19" ($200)', variable=self.valueMon, value=1, command=self.monitMethod1)
        self.monitor2 = tkinter.Radiobutton(self.middleFrame, text='21" ($300)', variable=self.valueMon, value=2, command=self.monitMethod2)
        self.monitor3 = tkinter.Radiobutton(self.middleFrame, text='24" ($400)', variable=self.valueMon, value=3, command=self.monitMethod3)

        self.checkButton = tkinter.Button(self.bottomFrame, text='OK', command=self.checkPrice)
        self.quitButton = tkinter.Button(self.bottomFrame, text='Quit', command=self.mainWindow.destroy)

        
        self.proc1.grid(row=1, column=1)
        self.proc2.grid(row=1, column=2)
        self.mem1.grid(row=2, column=1)
        self.mem2.grid(row=2, column=2)
        self.HDD1.grid(row=3, column=1)
        self.HDD2.grid(row=3, column=2)
        self.HDD3.grid(row=3, column=3)
        self.monitor1.grid(row=4, column=1)
        self.monitor2.grid(row=4, column=2)
        self.monitor3.grid(row=4, column=3)

        self.checkButton.grid(row=5, column=1)
        self.quitButton.grid(row=5, column=2)

        self.topFrame.pack()
        self.middleFrame.pack()
        self.bottomFrame.pack()
        tkinter.mainloop()

    def procMethod1(self):
        self.processor = 250
    def procMethod2(self):
        self.processor = 350

    def memMethod1(self):
        self.memory = 150
    def memMethod2(self):
        self.memory = 250

    def hddMethod1(self):
        self.HDD = 100
    def hddMethod2(self):
        self.HDD = 150
    def hddMethod3(self):
        self.HDD = 200

    def monitMethod1(self):
        self.monitor = 200
    def monitMethod2(self):
        self.monitor = 300
    def monitMethod3(self):
        self.monitor = 400

    def checkPrice(self):
        self.total = self.processor + self.memory + self.HDD + self.monitor
        tkinter.messagebox.showinfo('Total', f'Your total for the parts picked is: ${self.total}')

def main():
    myGUI = guiWindow()

if __name__ == "__main__":
    main()