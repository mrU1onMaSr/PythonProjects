from tkinter import *
import datetime as dt

root = Tk()
root.title("DateCountDown")
root.geometry("500x500")

#Year inputs
label1 = Label(root,text = "Year")
label1.place(relx=0.25,rely=0.2,anchor = CENTER)
input1 = Entry(root,width=10)
input1.place(relx=0.25,rely=0.3,anchor = CENTER)

#Month inputs
label2 = Label(root,text = "Month")
label2.place(relx=0.50,rely=0.2,anchor = CENTER)
input2 = Entry(root,width=10)
input2.place(relx=0.50,rely=0.3,anchor = CENTER)

#Day inputs
label3 = Label(root,text = "Day")
label3.place(relx=0.75,rely=0.2,anchor = CENTER)
input3 = Entry(root,width=10)
input3.place(relx=0.75,rely=0.3,anchor = CENTER)

#results
ResLabel = Label(root)
ResLabel.place(relx=0.5,rely=0.6,anchor = CENTER)

def Main():
    MainDate = dt.datetime.now()

    #User Inputs
    U_Year = int(input1.get())
    U_Month = int(input2.get())
    U_Day = int(input3.get())

    #current
    Year = int(MainDate.strftime("%Y"))
    Month = int(MainDate.strftime("%m"))
    Day = int(MainDate.strftime("%d"))

    #Result calculation
    R_Year = str(U_Year - Year)
    R_Month = str(U_Month - Month)
    R_Day = str(U_Day - Day)

    ResLabel["text"] = R_Year + " Years " + R_Month + " Months and " + R_Day + " days until date."

    print(R_Year + " Years " + R_Month + " Months and " + R_Day + " days until date.")

Button1 = Button(root,text="Calculate",command = Main)
Button1.place(relx=0.5,rely=0.5,anchor = CENTER)
root.mainloop()