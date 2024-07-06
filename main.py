import random
import string
from tkinter import *

class Interface(Frame):
    def __init__(self, window, **kwargs):
        Frame.__init__(self, window, **kwargs)

        self.length = Spinbox(window, from_=0, to=26)
        self.length.pack()

        self.checkDigits=BooleanVar()
        self.checkDigits.set(True)
        self.checkLowercaseLetters=BooleanVar()
        self.checkLowercaseLetters.set(True)
        self.checkUppercaseLetters=BooleanVar()
        self.checkUppercaseLetters.set(True)
        self.checkSpecificChars=BooleanVar()
        self.checkSpecificChars.set(True)
        
        self.digits = Checkbutton(window, text="Digits [ 0 1 2 3 4 5 6 7 8 9 ]", var=self.checkDigits,  onvalue=True, offvalue=False)
        self.digits.pack()
        self.lowercaseLetters = Checkbutton(window, text="Lowercase letters [ a b c ... x y z ]", var=self.checkLowercaseLetters,  onvalue=True, offvalue=False)
        self.lowercaseLetters.pack()
        self.uppercaseLetters = Checkbutton(window, text="Uppercase letters [ A B C ... X Y Z ]", var=self.checkUppercaseLetters,  onvalue=True, offvalue=False)
        self.uppercaseLetters.pack()
        self.specificChars = Checkbutton(window, text="Specific characters [ ~ ! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : , . < > / ? | ]", var=self.checkSpecificChars,  onvalue=True, offvalue=False)
        self.specificChars.pack()
        self.generateButton = Button(window, text="Generate", command=self.Generate)
        self.generateButton.pack()
        self.value = StringVar() 
        self.output = Entry(window, textvariable=string, width=30)
        self.output.pack()

    def Generate(self):
        password=[]
        chars=[]

        if(self.checkDigits.get()):
            chars.append(string.digits)
        if(self.checkLowercaseLetters.get()):
            chars.append(string.ascii_lowercase)
        if(self.checkUppercaseLetters.get()):
            chars.append(string.ascii_uppercase)
        if(self.checkSpecificChars.get()):
            chars.append(string.punctuation)

        for index in range(0, int(self.length.get())):
            password.append(random.choice(chars[random.randint(0, len(chars)-1)]))

        self.output.insert(0,''.join(password))



window = Tk()
window.title("Password generator")
interface = Interface(window)
interface.mainloop()
interface.destroy()
