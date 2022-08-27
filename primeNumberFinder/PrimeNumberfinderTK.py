from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("PrimeNumberFinder")

entry1 = Entry()
entry1.pack(pady=60)

Label1 = Label()
Label1.pack(pady=60)

def Main():
    try:
        number = int(entry1.get())
        if number > 1:
            for i in range(2, int(number/2)+1):
                if (number % i) ==0:
                    Label1["text"] = str(number)+" is not a prime number."
                else:
                    Label1["text"] = str(number) + " is a prime number"
        else:
            Label1["text"] = str(number) +" is not a prime number."
    except:
        Label1["text"] = "plesae enter a valid number."

Button1 = Button(text = "Check",command = Main)
Button1.pack(pady=20)

root.mainloop()