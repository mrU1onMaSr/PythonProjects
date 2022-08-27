from tkinter import *

root = Tk()
root.title("Encoder")
root.geometry("500x500")

Input1 = Entry(root)
Input1.place(relx = 0.3,rely = 0.4 , anchor = CENTER)

Input1Label = Label(root,text = "text:")
Input1Label.place(relx = 0.3,rely = 0.3 , anchor = CENTER)

Input2 = Entry(root)
Input2.place(relx = 0.7,rely = 0.4 , anchor = CENTER)

Input2Label = Label(root,text = "Ciper Shift:")
Input2Label.place(relx = 0.7,rely = 0.3 , anchor = CENTER)

MainLabel = Label(root)
MainLabel.place(relx = 0.5,rely = 0.5 , anchor = CENTER)

def Main():
    UnEncodeedMesage = Input1.get()
    CipherShift = Input2.get()

    ASCII_values = []
    for character in UnEncodeedMesage:
        ASCII_values.append(ord(character))

    for i in range(len(ASCII_values)):
        ASCII_values[i] += int(CipherShift)
    
    fin = ''.join(chr(i) for i in ASCII_values)

    MainLabel["text"] = fin

    print(str(ASCII_values))
    print(fin)

Button1 = Button(root,text = "encode",command = Main)
Button1.place(relx = 0.5,rely = 0.7 , anchor = CENTER)

root.mainloop()