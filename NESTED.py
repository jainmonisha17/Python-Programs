def outer():
    print("Inside the outer function. ")

    def inner():
        print("Inside the inner function")
    inner()
outer()
inner()

# inner() 