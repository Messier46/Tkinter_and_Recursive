# exGUIList.py
import tkinter
import random

ROWS = 2
COLS = 3

class TableGUI:
    def __init__(self) -> None:
        self.mainWindow = tkinter.Tk()

        self.labelR=[]
        for i in range(ROWS):
            self.labelR.append([])
            self.labelR[i] = tkinter.Label(self.mainWindow, width=10, text = f'Row {i+1}').grid(row=i+1, column=0)
        self.labelR.append([])
        self.labelR[ROWS]= tkinter.Label(self.mainWindow, width=10, text = f'Column Sum').grid(row=ROWS+1, column=0)

        self.labelC=[]
        for i in range(COLS):
            self.labelC.append([])
            self.labelC[i] = tkinter.Label(self.mainWindow, width=10, text = f'Column {i+1}').grid(row=0, column=i+1)
        self.labelC.append([])
        self.labelC[COLS] = tkinter.Label(self.mainWindow, width=10, text = f'Row Sum').grid(row=0, column=COLS+1)
        


        self.cells = [[0]*(COLS+1)]*(ROWS+1)
        self.vars = []
        for r in range(ROWS+1):
            self.vars.append([])
            for c in range(COLS+1):
                self.vars[r].append([])
                self.vars[r][c] = tkinter.StringVar()
                self.vars[r][c].set(self.cells[r][c])

        self.entry = []
        for r in range(ROWS+1):
            self.entry.append([])
            for c in range(COLS+1):
                self.entry[r].append([])
                self.entry[r][c] = tkinter.Entry(self.mainWindow, width=10, textvariable=self.vars[r][c]).grid(row=r+1, column = c+1)
        
        self.btnMT = tkinter.Button(self.mainWindow, text='Make Table', command=self.makingTable).grid(row = ROWS+2,column = int(COLS/2+1))
        self.btnCac = tkinter.Button(self.mainWindow, text='Calculate', command=self.calculate).grid(row=ROWS+2, column=int(COLS/2+2))
        tkinter.mainloop()


    def makingTable(self):
        for r in range(ROWS):
            for c in range(COLS):
                self.cells[r][c] = random.randint(1,100)
                self.vars[r][c].set(self.cells[r][c])

    def calculate(self):
        bothSum = 0
        for c in range(COLS):
            total = 0
            for r in range(ROWS):
                total += int(self.vars[r][c].get())
            self.vars[ROWS][c].set(total)
            bothSum += total

        # print(bothSum)

        for r in range(ROWS):
            total = 0
            for c in range(COLS):
                total += int(self.vars[r][c].get())
            self.vars[r][COLS].set(total)
            # bothSum += total

        self.vars[ROWS][COLS].set(bothSum)
        
        # self.vars[0][COLS].set(int(self.vars[0][c].get()) + int(self.vars[0][c].get()) + int(self.vars[0][c].get()))
        # self.cells[1][3] = self.cells[0][0] + self.cells[0][1] + self.cells[0][2]
        # self.vars[0][3].set(self.cells[1][3])
        # self.vars[0][3].set(int(self.vars[0][0].get()) + int(self.vars[0][1].get()) + int(self.vars[0][2].get()))
        # THIS -> print(self.vars[0][0].get())


def main():
    myGUI = TableGUI()

if __name__ == "__main__":
    main()