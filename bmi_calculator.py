from tkinter import *

class bmiCalculator:
    
    def __init__(self):

        self.main = Tk()
        self.main.title('BMI Calculator')
        self.main.geometry('800x800')
        
        self.age = DoubleVar()
        self.height = DoubleVar()
        self.weight = DoubleVar()
        self.bmi = DoubleVar()

        self.ageLabel = Label(self.main, text = 'Age:')
        self.ageEntry = Entry(self.main, textvariable = self.age, cursor = 'xterm', justify = CENTER)

        self.heightLabel = Label(self.main, text = 'Height:')
        self.heightEntry = Entry(self.main, textvariable = self.height, cursor = 'xterm', justify = CENTER)

        self.weightLabel = Label(self.main, text = 'Weight:')
        self.weightEntry = Entry(self.main, textvariable = self.weight, cursor = 'xterm', justify = CENTER)

        self.calcButton = Button(self.main, text = 'Calculate', cursor = 'hand2', command = self.calculate)

        self.bmiLabel = Label(self.main)        

    def calculator(self):
        
        self.ageLabel.place(relx = 0.2, rely = 0.1)
        self.ageEntry.place(relx = 0.3, rely = 0.1)

        self.heightLabel.place(relx = 0.2, rely = 0.2)
        self.heightEntry.place(relx = 0.3, rely = 0.2)

        self.weightLabel.place(relx = 0.2, rely = 0.3)
        self.weightEntry.place(relx = 0.3, rely = 0.3)

        self.calcButton.place(relx = 0.25, rely = 0.4)

        self.main.mainloop()

    def calculate(self):
        
        self.bmi = float(self.weight.get())/(float(self.height.get())*float(self.height.get()))
        self.bmiLabel.config(text = 'Your BMI is {}'.format(self.bmi))
        self.bmiLabel.place(relx = 0.2, rely = 0.5)

if __name__ == '__main__':
    
    bmiCalc = bmiCalculator()
    bmiCalc.calculator()


