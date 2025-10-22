def displayFactors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

def countFactors(n):
    count = 0
    countCycles = 0
    for i in range(1, n + 1):
        countCycles += 1
        if n % i == 0:
            count += 1
    return count, countCycles

def displayFactorsLowerNearSquareRoot(n):
    i = 1
    countFactors1 = 0
    while i * i <= n:
        countFactors1 += 1
        if n % i == 0:
            print(i, end = " ")

            if i != (n // i):
                print((n // i), end = " ")
        i += 1

def countFactorsLowerNearSquareRoot(n):
    count1 = 0
    countCycles1 = 0
    for i in range(1, n + 1):
        countCycles1 += 1
        if n % i == 0:
            count1 += 1
            if i != (n // i):
                i = i + 1
    return count1, countCycles1

def count_factors(n):
    countfactors = 0
    countCycles = 0
    i = 1
    while i * i <= n:
        countCycles = countCycles + 1

        if n % i == 0:
            countfactors = countfactors + 1
            print(i, end = "")
            if i != (n // i):
                countfactors = countfactors + 1

        i += 1
    return countfactors, countCycles

def isPrime(n):
    countFact = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            countFact += 1
            if i != (n // i):
                countFact += 1
        i += 1

    return countFact == 2


n = int(input("Enter a number: "))

print("Factors of", n, "are:", end=" ")
displayFactors(n)


restultFactors, resultCycles = countFactors(n)
resultFactors1, resultCycles1 = count_factors(n)
print("\nTotal number of factors:", restultFactors)
print("\n Total count cycle are: ", resultCycles)
print("\nTotal number of factors:", resultFactors1)
print("\n Total count cycle are: ", resultCycles1)
print("--------------------------------------------------------- ")

flag = isPrime(n)
if flag:
    print(f"{n} is Prime")
else:
    print(f"{n} is not a prime number")

