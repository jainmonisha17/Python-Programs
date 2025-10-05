secret_number = 9
guess_count = 0
guess_limit = 3

while  guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count = guess_count + 1

    if guess == secret_number:
        print("You won! Hurray!!")
        break
    
else:
    print("You exceeded the limit!! Try again next time! Sorry'_'")

'''
> help:
start - to start the car
stop - to stop the car
quit - to exit

like this:
>asd
I don't understand that...
>start
Car started...Ready to go!
>stop
Car stopped.
>quit
'''


