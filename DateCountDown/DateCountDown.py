import datetime as dt

MainDate = dt.datetime.now()

#User Inputs
U_Year = int(input("Year: "))
U_Month = int(input("Month: "))
U_Day = int(input("Day: "))

#current
Year = int(MainDate.strftime("%Y"))
Month = int(MainDate.strftime("%m"))
Day = int(MainDate.strftime("%d"))

#Result calculation
R_Year = str(U_Year - Year)
R_Month = str(U_Month - Month)
R_Day = str(U_Day - Day)

print(R_Year + " Years " + R_Month + " Months and " + R_Day + " days until date.")