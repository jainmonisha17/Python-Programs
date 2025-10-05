# Function vs Method

# Function
def print_name():
    print("Inside the function print_name")
print_name()

print("--------------------------------------------------")
# Method
class Demo:
    def display(self):
        print("Inside display method")
d = Demo()
d.display()