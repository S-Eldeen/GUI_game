from tkinter import *
from random import *


class Game:
    def __init__ (self,name,strength,health,number):

        self.name=name
        self.strength=strength
        self.number=number
        self.health=health
    
    def print_character(self):
        print(f"Character Name {self.name} and his power is {self.strength} and the health is {self.health}")

class Character(Game):

    def attack(self, target):
        target.health -= self.strength
        return target.health
    
    def isAlive(self):
        if (self.health > 0):
            return True
        else:
            return False
    
    def win_display(character1,character2):
        if(character1.isAlive()):
            print(f"the Wineer is {character1}")
        elif(character2.isAlive()):
            print(f"the Wineer is {character2}")


# 2 object (player) 
character1=Character("Seif Eldeen",21,100,1)
character2=Character("Hamed",13,100,2)

# playing function
def play():

    if character1.health<0 or character2.health<0:
        return
 
    listbox1.delete(0, "end")
    done = randint(character1.number,character2.number)
    listbox1.insert(END, done)
    if done==character1.number:
        listbox2.insert(END,"Attack")
        character1.attack(character2)
    else:
        listbox3.insert(END,"Attack")
        character2.attack(character1)
    
    text2.insert(END,f"{character1.health} & ")
    text2.insert(END,f"{character2.health} \n")
  
    if character1.health>0 and character2.health<0:
        text1.delete(0.0,"end")
        text1.insert(END,f"{character1.name}")
        return
    elif character1.health<0 and character2.health>0:
        text1.delete(0.0,"end")
        text1.insert(END,f"{character2.name}")
        return
    

           
           
# to start the game
def start():
    character1.health=100
    character2.health=100
    listbox1.delete(0, "end")
    listbox2.delete(0, "end")
    listbox3.delete(0, "end")
    text1.delete(0.0,"end")
    text2.delete(0.0,"end")


# GUI implmentation
root = Tk()
root.geometry('802x445+500+200')
root.title('Simple GAME...')
root.resizable(width=False, height=False)



#to make background
# Add image file 
bg = PhotoImage(file = r"C:\Users\DELL\Desktop\python\GUI_project_finish\1234.png") 
# Show image using label 
label1 = Label( root, image = bg) 
label1.place(x = 0, y = 0) 
######################################








# for Knowing who play and startgame
frame1=Frame(root)
frame1.place(x=98,y=403)
Button1=Button(frame1,text="Player",command=play)
Button1.pack(fill=BOTH, expand=True, side=LEFT)
listbox1 = Listbox(
    frame1,
    height=2,
    width=10,
    font=('Times', 10),
    activestyle="none",
    # bg="#F73528"
)
listbox1.pack(side=LEFT, fill=BOTH)
Button2=Button(frame1,text="Start",command=start)
Button2.pack(fill=BOTH, expand=True, side=LEFT)

# for show player1
labelframe1=LabelFrame(root,text=character1.name,width=60, height=200)
labelframe1.place(x=5,y=5)
listbox2 = Listbox(
    labelframe1,
    height=26,
    width=10,
    font=('Times', 10),
    activestyle="none",
    bg="#F73528"
)
listbox2.pack(side=LEFT, fill=BOTH)

# for show player2
labelframe2=LabelFrame(root,text=character2.name,width=60, height=200)
labelframe2.place(x=729,y=5)
listbox3 = Listbox(
    labelframe2,
    height=26,
    width=10,
    font=('Times', 10),
    activestyle="none",
    bg="#F73528"
)
listbox3.pack(side=LEFT, fill=BOTH)


# the winer
labelframe4=LabelFrame(root,text="The Hero",width=10, height=10)
labelframe4.place(x=550,y=385)

text1=Text(labelframe4,height=2,width=20)
text1.pack(side=LEFT, fill=BOTH)

# the health
labelframe5=LabelFrame(root,text="The Health",width=20, height=10)
labelframe5.place(x=265,y=350)

text2=Text(labelframe5,height=4,width=31)
text2.pack(side=LEFT, fill=BOTH)

scroll = Scrollbar(labelframe5)
scroll.pack(side=RIGHT, fill=BOTH)

text2.config(yscrollcommand=scroll.set)
scroll.config(command=text2.yview)


root.mainloop()
