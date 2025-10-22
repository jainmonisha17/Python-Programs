def print_message():
    print("Hello Everyone")

def outer(print1):
    print("Entering outer")

    def inner():
        print("Entering inner")
        reference1 = print1
        reference1
        print("Leaving inner")
    return inner
ptr1 = print_message
reference = outer(ptr1)
reference()
print("After ececuting inner using refenece")