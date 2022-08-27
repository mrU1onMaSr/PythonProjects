try:
    global number
    number = int(input("Enter number: "))

    if number > 1:
        for i in range(2, int(number/2)+1):
            if (number % i) ==0:
                print(str(number)+" is not a prime number.")
            else:
                print(str(number)+" is a prime number.")
    else:
        print(str(number) +" is not a prime number.")
except:
    print("Pls enter a valid number")


