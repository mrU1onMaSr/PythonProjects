global Run
Run = True

global MainList
MainList = []

print("Welcome to SortingInPython \n Commands: \n 'run' to sort \n del to delete \n and stop to stop \n enter number to begin." )

while Run == True:

    UI = input("Enter Command: ")

    if UI == "run":
        for j in range(len(MainList) - 1):
            for i in range(len(MainList)-1-j):
                if MainList[i] > MainList[i+1]:
                    MainList[i],MainList[i+1] = MainList[i+1],MainList[i]
        print(MainList)
    elif UI == "del":
        try:
            MainList.pop()
            print(MainList)
        except:
            print("Can't delete if there are no numbers in list")
    elif UI == "stop":
        Run = False
    else:
        try:
            MainList.append(int(UI))
            print(MainList)
        except:
            print("please enter a valid command or a number.")