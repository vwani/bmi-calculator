from tkinter import *
from pymongo import MongoClient

# TO-DO: Create save, history button
# TO-DO: Different units for input
# TO-DO: Add Classification

class bmiCalculator:
    
    def __init__(self):

        self.root = Tk()
        self.root.title('BMI Calculator')
        self.root.geometry('800x800')

        self.uname = StringVar()
        self.pswd = StringVar()
        self.age = IntVar()
        self.height = DoubleVar()
        self.weight = DoubleVar()
        self.bmi = DoubleVar()
        self.logged = False

        self.unameLabel = Label(self.root, text = 'User Name:')
        self.unameEntry = Entry(self.root, textvariable = self.uname, cursor = 'xterm', justify = CENTER)

        self.pswdLabel = Label(self.root, text = 'Password:')
        self.pswdEntry = Entry(self.root, textvariable = self.pswd, cursor = 'xterm', justify = CENTER)

        self.ageLabel = Label(self.root, text = 'Age:')
        self.ageEntry = Entry(self.root, textvariable = self.age, cursor = 'xterm', justify = CENTER)

        self.heightLabel = Label(self.root, text = 'Height:')
        self.heightEntry = Entry(self.root, textvariable = self.height, cursor = 'xterm', justify = CENTER)

        self.weightLabel = Label(self.root, text = 'Weight:')
        self.weightEntry = Entry(self.root, textvariable = self.weight, cursor = 'xterm', justify = CENTER)

        self.calcButton = Button(self.root, text = 'Calculate'.center(15), cursor = 'hand2', command = self.calculate)
        self.loginButton = Button(self.root, text = 'Login'.center(15), cursor = 'hand2')
        self.signupButton = Button(self.root, text = 'Sign Up'.center(15), cursor = 'hand2', command = self.adduser)
        self.backButton = Button(self.root, text = 'Back'.center(15), cursor = 'hand2', command = self.calculator)

        self.bmiLabel = Label(self.root)
        self.loginLabel = Label(self.root)

        self.client = MongoClient('localhost', 27017)
        self.users = self.client.bmi.users

    def calculator(self):
        
        for widget in [self.ageEntry, self.heightEntry, self.weightEntry]:
            widget.delete(0, END)

        for widget in [self.unameLabel, self.pswdLabel, self.unameEntry, self.pswdEntry, self.loginLabel, self.signupButton, self.backButton]:
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
            self.loginButton.config(text = 'Login'.center(15), command = self.login)

        if self.logged:
            self.loginButton.config(text = 'Logout'.center(15), command = self.logout)

    def login(self):

        for widget in [self.ageEntry, self.heightEntry, self.weightEntry, self.ageLabel, self.heightLabel, self.weightLabel, self.calcButton, self.bmiLabel]:
            widget.place_forget()

        self.unameLabel.place(relx = 0.2, rely = 0.1)
        self.unameEntry.place(relx = 0.3, rely = 0.1)
        self.unameEntry.delete(0, END)
        
        self.pswdLabel.place(relx = 0.2, rely = 0.2)
        self.pswdEntry.place(relx = 0.3, rely = 0.2)
        self.pswdEntry.delete(0, END)

        self.loginButton.place(relx = 0.2, rely = 0.3)
        self.loginButton.config(command = self.validate)

        self.signupButton.place(relx = 0.3, rely = 0.3)
        self.backButton.place(relx = 0.4, rely = 0.3)
        
    def calculate(self):
        
        self.bmi = float(self.weight.get())/(float(self.height.get())*float(self.height.get()))
        self.bmiLabel.config(text = 'Your BMI is {0:.2f}'.format(self.bmi))
        self.bmiLabel.place(relx = 0.2, rely = 0.5)

        if not self.logged:
            self.loginLabel.config(text = 'Login to save your results and to view your history.')
            self.loginLabel.place(relx = 0.2, rely = 0.55)
            self.root.after(1000, self.loginLabel.place_forget)

    def adduser(self):

        if self.uname.get() == '' or self.pswd.get() == '':
            self.loginLabel.config(text = 'Invalid Sign Up Attempt. Cannot leave fields empty.')
            self.loginLabel.place(relx = 0.2, rely = 0.4)
            self.root.after(1000, self.loginLabel.place_forget)            

        elif self.users.find_one({'uname': f'{self.uname.get()}'}):
            self.loginLabel.config(text = 'This user already exists. Please try again.')
            self.loginLabel.place(relx = 0.2, rely = 0.4)
            self.root.after(1000, self.loginLabel.place_forget)

            
        else:
            self.users.insert_one({'uname': f'{self.uname.get()}', 'pswd': f'{self.pswd.get()}'})
            self.logged = True
            self.loginLabel.config(text = 'User Created Successfully.')
            self.loginLabel.place(relx = 0.2, rely = 0.4)
            self.root.after(1000, self.calculator)

    def validate(self):

        if self.users.find_one({'uname': f'{self.uname.get()}', 'pswd': f'{self.pswd.get()}'}):
            print(self.users.find_one({'uname': f'{self.uname.get()}', 'pswd': f'{self.pswd.get()}'}))
            self.logged = True
            self.loginLabel.config(text = 'Logged In Successfully.')
            self.loginLabel.place(relx = 0.2, rely = 0.4)
            self.root.after(1000, self.calculator)

        else:
            self.loginLabel.config(text = 'Login Unsuccessful. Please try again.')
            self.loginLabel.place(relx = 0.2, rely = 0.4)
            self.root.after(1000, self.loginLabel.place_forget)
                 
    def logout(self):
        
        self.logged = False
        self.uname.set('')
        self.pswd.set('')
        
        self.loginLabel.config(text = 'Logged Out Successfully.')
        self.loginLabel.place(relx = 0.2, rely = 0.55)
        self.root.after(1000, self.loginLabel.place_forget)

        for widget in [self.ageEntry, self.heightEntry, self.weightEntry]:
            widget.delete(0, END)

        self.loginButton.config(text = 'Login'.center(15), command = self.login)

if __name__ == '__main__':

    bmiCalc = bmiCalculator()
    bmiCalc.calculator()
    bmiCalc.root.mainloop()
