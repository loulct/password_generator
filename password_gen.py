import random
import string
from tkinter import *

class Interface(Frame):
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, **kwargs)

        self.length = Spinbox(fenetre, from_=0, to=26)
        self.length.pack()

        self.checkValue=BooleanVar()
        self.checkValue.set(True)
        self.checkValue1=BooleanVar()
        self.checkValue1.set(True)
        self.checkValue2=BooleanVar()
        self.checkValue2.set(True)
        self.checkValue3=BooleanVar()
        self.checkValue3.set(True)
        
        self.chiffre = Checkbutton(fenetre, text="Avec des chiffres [ 0 1 2 3 4 5 6 7 8 9 ]", var=self.checkValue,  onvalue=True, offvalue=False)
        self.chiffre.pack()
        self.mini = Checkbutton(fenetre, text="Avec des lettres minuscules [ a b c ... x y z ]", var=self.checkValue1,  onvalue=True, offvalue=False)
        self.mini.pack()
        self.maj = Checkbutton(fenetre, text="Avec des lettres majuscules [ A B C ... X Y Z ]", var=self.checkValue2,  onvalue=True, offvalue=False)
        self.maj.pack()
        self.spec = Checkbutton(fenetre, text="Avec des caractères spéciaux [ ~ ! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : , . < > / ? | ]", var=self.checkValue3,  onvalue=True, offvalue=False)
        self.spec.pack()
        self.gen = Button(fenetre, text="Generer", command=self.Generate)
        self.gen.pack()
        self.value = StringVar() 
        self.entree = Entry(fenetre, textvariable=string, width=30)
        self.entree.pack()

    def Generate(self):
        mdp=[]
        letters=[]
        if(self.checkValue.get()):
            letters.append(string.digits)
        if(self.checkValue1.get()):
            letters.append(string.ascii_lowercase)
        if(self.checkValue2.get()):
            letters.append(string.ascii_uppercase)
        if(self.checkValue3.get()):
            letters.append(string.punctuation)

        taille=int(self.length.get())
        for k in range(0, taille):
            mdp.append(random.choice(letters[random.randint(0, len(letters)-1)]))

        print(mdp)
        self.entree.insert(0,mdp)



fenetre = Tk()
interface = Interface(fenetre)
interface.mainloop()
interface.destroy()
