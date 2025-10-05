print("Welcome to ATM")
print("Insert the card here:")
input()
print("Enter the 4 digits pin:")
pin = int(input())

if pin == 8888:
    print("Select the language:")
    print("1.English \n 2. Hindi \n 3. Kannada")
    lang = int(input("Enter your prefered language:"))

    if lang == 1:
        print("1. Savings \n 2. Current")
        option = int(input("Select your option:"))

        if option == 1:
            print("1. 1000 \n 2. 2000 \n 3. 5000 \n 4. 10000")
            amount = int(input("Select the amount:"))
            print("Collect your cash")
            print("Please wait")
            print("collect the cash and card")
            print("Thank you for using our ATM service")
            

