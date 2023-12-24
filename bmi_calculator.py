from tkinter import *


class bmiCalculator:
    def __init__(self):

        self.main = Tk()
        self.main.title('BMI Calculator')
        self.main.geometry('800x800')

        self.uname = StringVar()
        self.pswd = StringVar()
        self.age = IntVar()
        self.height = DoubleVar()
        self.weight = DoubleVar()
        self.bmi = DoubleVar()
        self.logged = False

        self.unameLabel = Label(self.main, text = 'User Name:')
        self.unameEntry = Entry(self.main, textvariable = self.uname, cursor = 'xterm', justify = CENTER)

        self.pswdLabel = Label(self.main, text = 'Password:')
        self.pswdEntry = Entry(self.main, textvariable = self.pswd, cursor = 'xterm', justify = CENTER)

        self.ageLabel = Label(self.main, text = 'Age:')
        self.ageEntry = Entry(self.main, textvariable = self.age, cursor = 'xterm', justify = CENTER)

        self.heightLabel = Label(self.main, text = 'Height:')
        self.heightEntry = Entry(self.main, textvariable = self.height, cursor = 'xterm', justify = CENTER)

        self.weightLabel = Label(self.main, text = 'Weight:')
        self.weightEntry = Entry(self.main, textvariable = self.weight, cursor = 'xterm', justify = CENTER)

        self.calcButton = Button(self.main, text = 'Calculate', cursor = 'hand2', command = self.calculate)
        self.loginButton = Button(self.main, text = 'Login', cursor = 'hand2')

        self.bmiLabel = Label(self.main)
        self.loginLabel = Label(self.main)

    def calculator(self):
        for widget in [self.ageEntry, self.heightEntry, self.weightEntry]:
            widget.delete(0, END)

        for widget in [self.unameLabel, self.pswdLabel, self.unameEntry, self.pswdEntry, self.loginLabel]:
            widget.place_forget()
            
        self.ageLabel.place(relx = 0.2, rely = 0.1)
        self.ageEntry.place(relx = 0.3, rely = 0.1)

        self.heightLabel.place(relx = 0.2, rely = 0.2)
        self.heightEntry.place(relx = 0.3, rely = 0.2)

        self.weightLabel.place(relx = 0.2, rely = 0.3)
        self.weightEntry.place(relx = 0.3, rely = 0.3)

        self.calcButton.place(relx = 0.25, rely = 0.4)
        self.loginButton.place(relx = 0.35,rely = 0.4)

        if not self.logged:
            self.loginButton.config(text = 'Login', command = self.login)

        if self.logged:
            self.loginButton.config(text = 'Logout', command = self.logout)

    def login(self):

        for widget in [self.ageEntry, self.heightEntry, self.weightEntry, self.ageLabel, self.heightLabel, self.weightLabel, self.calcButton, self.bmiLabel]:
            widget.place_forget()

        self.unameLabel.place(relx = 0.2, rely = 0.1)
        self.unameEntry.place(relx = 0.3, rely = 0.1)
        
        self.pswdLabel.place(relx = 0.2, rely = 0.2)
        self.pswdEntry.place(relx = 0.3, rely = 0.2)

        self.loginButton.place(relx = 0.25, rely = 0.3)
        self.loginButton.config(command = self.validate)

        
    def calculate(self):
        
        self.bmi = float(self.weight.get())/(float(self.height.get())*float(self.height.get()))
        self.bmiLabel.config(text = 'Your BMI is {0:.2f}'.format(self.bmi))
        self.bmiLabel.place(relx = 0.2, rely = 0.5)

        if not self.logged:
            self.loginLabel.config(text = 'Login to save your results and to view your history.')
            self.loginLabel.place(relx = 0.2, rely = 0.55)
            self.main.after(1000, self.loginLabel.place_forget)

    def validate(self):
        
        self.logged = True
        self.loginLabel.config(text = 'Logged In Successfully.')
        self.loginLabel.place(relx = 0.2, rely = 0.4)
        self.main.after(1000, self.calculator)
        
    def logout(self):
        
        self.logged = False
        self.uname.set('')
        self.pswd.set('')
        
        self.loginLabel.config(text = 'Logged Out Successfully.')
        self.loginLabel.place(relx = 0.2, rely = 0.55)
        self.main.after(1000, self.loginLabel.place_forget)

        self.loginButton.config(text = 'Login', command = self.login)

if __name__ == '__main__':


    bmiCalc = bmiCalculator()
    bmiCalc.calculator()
    bmiCalc.main.mainloop()


