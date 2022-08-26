from tkinter import *

root = Tk()
root.title("SortingInPython")
root.geometry("500x500")

MainInput = Entry(root)
MainInput.place(relx=0.5,rely=0.2,anchor=CENTER)

label1 = Label(root,text="enter numbers to add")
label1.place(relx=0.5,rely=0.13,anchor=CENTER)

MainOutput = Label(root,text = "List: ")
MainOutput.place(relx=0.5,rely=0.7,anchor=CENTER)

global MainList
MainList = []

def AddToList():
    global MainList

    MainList.append(str(MainInput.get())) 
    MainInput.delete(0, END)
    MainOutput["text"] = str(MainList)

def Main():
    global MainList

    for j in range(len(MainList) - 1):
        for i in range(len(MainList)-1-j):
            if MainList[i] > MainList[i+1]:
                MainList[i],MainList[i+1] = MainList[i+1],MainList[i]
    MainOutput["text"] = str(MainList)

sortButton = Button(root,text = "add",command = AddToList)
sortButton.place(relx=0.25,rely=0.5,anchor=CENTER)

sortButton = Button(root,text = "sort",command = Main)
sortButton.place(relx=0.75,rely=0.5,anchor=CENTER)

root.mainloop()