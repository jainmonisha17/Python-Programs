def outer():
    print("Entering outer")

    def inner():
        print("Entering inner function")
        print("Processing")
        print("Leaving inner function")
    return inner 
referenceVariable = outer()
print("After executing outer function")
referenceVariable()
print("After executing inner using reference variable")
