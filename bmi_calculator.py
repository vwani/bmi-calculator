from tkinter import *


class bmiCalculator:
    def __init__(self):
        self.age = DoubleVar()
        self.height = DoubleVar()
        self.weight = DoubleVar()
        self.bmi = DoubleVar()

    def calculate(self):
        self.bmi = float(self.weight.get())/(float(self.height.get())*float(self.height.get()))
        bmiLabel.config(text = 'Your BMI is {}'.format(self.bmi))
        bmiLabel.place(relx = 0.2, rely = 0.5)
        

if __name__ == '__main__':
    
    main = Tk()
    main.title('BMI Calculator')
    main.geometry('800x800')

    bmiCalc = bmiCalculator()

    ageLabel = Label(main, text = 'Age:')
    ageLabel.place(relx = 0.2, rely = 0.1)

    ageEntry = Entry(main, textvariable = bmiCalc.age, cursor = 'xterm', justify = CENTER)
    ageEntry.place(relx = 0.3, rely = 0.1)

    heightLabel = Label(main, text = 'Height:')
    heightLabel.place(relx = 0.2, rely = 0.2)

    heightEntry = Entry(main, textvariable = bmiCalc.height, cursor = 'xterm', justify = CENTER)
    heightEntry.place(relx = 0.3, rely = 0.2)

    weightLabel = Label(main, text = 'Weight:')
    weightLabel.place(relx = 0.2, rely = 0.3)

    weightEntry = Entry(main, textvariable = bmiCalc.weight, cursor = 'xterm', justify = CENTER)
    weightEntry.place(relx = 0.3, rely = 0.3)

    calcButton = Button(main, text = 'Calculate', cursor = 'hand2', command = bmiCalc.calculate)
    calcButton.place(relx = 0.25, rely = 0.4)

    bmiLabel = Label(main)


    main.mainloop()
