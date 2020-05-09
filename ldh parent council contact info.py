from tkinter import *
import random

#by Peter Mitchell 9-11-2018

window = Tk()
window.title("ldh parent council contact Info")
backgroudColour = "#4d0099"
window.configure(background=backgroudColour)

saveName = "information"

info = []
firstName = ""
lastName = ""
email = ""
#phoneNumberInput
phoneNumber = ""
def enterFunction():
    firstName = firstNameInput.get('1.0', END).replace("\n","")
    lastName = lastNameInput.get('1.0', END).replace("\n","")
    email = emailInput.get('1.0', END).replace("\n","")
    phoneNumber = phoneNumberInput.get('1.0', END).replace("\n","")
    
    if (((firstName != "" and firstName != "Please provide a name.") or lastName != "") and (email != "" and email != "Please provide an email.")):
        info.append([firstName, lastName, email, phoneNumber])
        
        firstNameInput.delete(0.0,END)
        lastNameInput.delete(0.0,END)
        emailInput.delete(0.0,END)
        phoneNumberInput.delete(0.0,END)
        
        i = 0
        i2 = 0
        while i < len(info):
            i2 = 0
            while i2 < len(info):
                try:
                    if i != i2 and info[i] == info[i2]:
                        del info[i2]
                except IndexError:
                    pass
                i2 += 1
            i+= 1
            
        save = open(saveName+str(random.randint(1,10000))+".txt", "w+")
        
        for i in range(len(info)):
            stringSave = info[i][0] + ", " + info[i][1] + ", " + info[i][2] + ", " + info[i][3] + "\n"
        
        save.write(str(stringSave))

        save.close()
    else:
        if firstName == "":
            firstNameInput.insert(END, 'Please provide a name.')

        if email == "":
            emailInput.insert(END, 'Please provide an email.')
    pass

#spaces so it isn't so close to the edges
Label (window, text=("                    \n"), bg=backgroudColour,
       font="none 12 bold").grid(row=0,column=0)

Label (window, text=("                    \n")*4, bg=backgroudColour,
       font="none 12 bold").grid(row=100,column=1000)



Label (window, text="First Name:", bg=backgroudColour, fg="white",
       font="none 24 bold").grid(row=2,column=1, sticky=W)

firstNameInput = Text(window, width = 22, height = 3, bg = "white",
          fg = "black", font = "none 24 bold")
firstNameInput.grid(row=3,column=1,sticky=W)

#--
Label (window, text=(" "*10), bg=backgroudColour,
       font="none 24 bold").grid(row=3,column=2)
#--

Label (window, text="Last Name:", bg=backgroudColour, fg="white",
       font="none 24 bold").grid(row=2,column=3, sticky=W)

lastNameInput = Text(window, width = 22, height = 3, bg = "white",
          fg = "black", font = "none 24 bold")
lastNameInput.grid(row=3,column=3,sticky=W)

#------
Label (window, text=("               \n"), bg=backgroudColour,
       font="none 12 bold").grid(row=4,column=0)
#------

Label (window, text="Email:", bg=backgroudColour, fg="white",
       font="none 24 bold").grid(row=5,column=1, sticky=W)

emailInput = Text(window, width = 22, height = 3, bg = "white",
          fg = "black", font = "none 24 bold")
emailInput.grid(row=6,column=1,sticky=W)

#--
Label (window, text=(" "*10), bg=backgroudColour,
       font="none 24 bold").grid(row=4,column=2)
#--

Label (window, text="Phone Number:", bg=backgroudColour, fg="white",
       font="none 24 bold").grid(row=5,column=3, sticky=W)

phoneNumberInput = Text(window, width = 22, height = 3, bg = "white",
          fg = "black", font = "none 24 bold")
phoneNumberInput.grid(row=6,column=3,sticky=W)

#------
Label (window, text=("               \n"), bg=backgroudColour,
       font="none 12 bold").grid(row=7,column=1)
#------


Button (window, text="Enter", width=10, height=1, command=enterFunction,
        font = "none 32 bold").grid(row=8,column=1,sticky=NW)

#run the program
window.mainloop()





