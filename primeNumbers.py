# Function to display all factors of a number
def displayFactors(n):
    print(f"Factors of {n} are:", end=" ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()  # for new line


# Function to count how many factors a number has
def countFactors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count = count + 1
    return count


# Main logic
n = int(input("Enter a number: "))

displayFactors(n)
factor_count = countFactors(n)

# Prime number check
if n <= 1:
    print("Not a prime number (numbers ≤ 1 are not prime)")
    print(False)
elif factor_count == 2:
    print(f"{n} is a Prime number ✅")
    print(True)
else:
    print(f"{n} is NOT a Prime number ❌")
    print(False)
