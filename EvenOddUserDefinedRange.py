# •	Enter start range: 10
# •	Enter end range: 16
# •	Expected output: 
#   Even num’s
# 	10     12     14     16

def checkEvenOdd(number):
    return number % 2 == 0

start = int(input("Enter a starting range: "))
end = int(input("Enter an ending range: "))

if start > end:
    print("Invalid input")
else:
    print("Even numbers:", end = " ")

for evenNumbers in range(start, end + 1):
    if checkEvenOdd(evenNumbers):
        print(evenNumbers, end = " ")
