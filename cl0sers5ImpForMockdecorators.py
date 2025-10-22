def print_message():
    message = "Hello Everyone" # printing the message
    return message
def outer(print1):  # 
    print("Entering outer")
    def inner():  # 
        print("Entering inner")
        reference1 = print1
        message2 = reference1()
        new_value = message2.upper()
        print(new_value)
        print("Leaving inner funciton")

    return inner
reference = outer(print_message)
reference()