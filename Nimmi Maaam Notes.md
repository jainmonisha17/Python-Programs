Comparision Operation:



 	It helps to compare the given 2 values.

 	Input: Boolean condition

 	Output: Boolean value

 	>, <, ==, !=, >=, <=

 



Note:

Boolean Condition:

 \* Direct True or False

 \* Anything other than zero is True

 \* Zero -> False, 0 -> False

 \* Any num or value -> True

 \* Expression that returns a value or a variable that holds a value



True, False, None: Special kind of keywords that internally holds value



True -> 1

False -> 0

None -> Nothing



Relational Operator: ==, !=

Only equals equals and not equals to



----------------------------------------------------------------------------------------------------------------------





6th oct

Bitwise operator:

1\. Bitwise and (\&)

2\. Bitwise or (|)

3\. Bitwise not / complement / negation (~)

4\. Bitwise XOR (^)

5\. Bitwise left shift (<<)

6\. Bitwise right shift (>>)





Most used and most famous operator is Assignment operator(=) -> helps us to store some value mentioned on RHS to the named memory location on LHS.



Syntax1: Initialization(Storing)

&nbsp;	 named\_memory\_location = value



Syntax2: Re-Initialization(Updation)

&nbsp;	 # initialized variable

&nbsp;	 named\_memory\_location= initialized\_variable\_name / value



named memory location -> variable just a name given to a memory

id and memory address difference



----------------------------------------------------------------------------------------------------------------------



a = 10

print(a) # 10



b = (2  \* 5)

print(b) # 10



c = (10 \*\* 1)

print(c)



print(a == b == c)

print(id(a) == id(b) == id(c)) # True



c = 15

print(id(c)) #140727761360104



c = 20

print(id(c)) # 140727761360264



c = 25

print(id(c)) # 140727761360424



\# id's holds the updated value of c

\# one variable can hold different values at different times

\# multiple value into the same variable it will always points to the latest updated value

\# we think that we are changing the value of c but in reality we are creating a new object in the memory and c is pointing to the new object.



d = 1, 2, 3

print(d)

print(type(d)) # <class 'tuple'>

\# A tuple is a collection data type in Python.

\# It is similar to a list, but with one big difference:

\# Tuples are immutable (once created, you cannot change, add, or remove elements).





Shared memory = multiple processes accessing the same memory space → used for faster communication and avoiding data duplication.



----------------------------------------------------------------------------------------------------------------------

Points to Remember:



Variables: 

⦁ It is a "named memory location" that can hold single valued data

⦁ It is a container to store a value

if the same value is stored into different variables, then internally all the variables will point to the same memory

⦁ If we try to re-initialize a variable which is pointing to the shared memory, then PVM will allocate a new memory for that re-initialized(updataion) variable.

⦁ If we try to store multiple values into the same memory one by one then the variable can only point to the latest updated value.

⦁ If we try to store multiple values at the same time into the same variable, then PVM will store them as a Tuple and return the address to the variable.

⦁ It is compulsory to initialize a variable before utilizing them or else you will get un-defined as an error.





----------------------------------------------------------------------------------------------------------------------





id -> Unique integer representation provided by the PVM during execution time based on the value stored and memroy assigned.



id() -> It is a pre-defined function that returns the ID of the provided value.



type() -> It is a pre-defined function that returns the datatype of the passed value stored into an initialized variable.



varities of assignment operators or compound statements in python.



----------------------------------------------------------------------------------------------------------------------





Arithmetic + Assignment:

-> +=, -=, \*=, \*\*=, //=, /=, %=



Bitwise + Assignment:

-> \&=, |=, ^=, <<=, >>= 



7th oct:



\* Min of two operand and operand on left side should be same as operand on right side.

\* Because operands should be same left and right hand side -> Compound statement in python.

\* One operand for negation operation. 

\* ~= -> Negation operator cannot be converted. Because Bitwise ~ or complement negation requires only 1 operand to perform the operation whereas while using compound statement, it requires minimun of 2 operands.

&nbsp;



5\. Membership Operator:( in, not in):

Input -> It can be used on Iterable object or group of elements.

Output -> Boolean value

It helps to check wheather an element is available in a group of elements or not.



**Iterable Object:  The objects that can hold multiple individual elements into the same shared memory location.**

**Ex: list, tuple, linked list, string.**







**a = (2 \* 4)**

**print(a not in myList) # True**

**# print(8 in a) # Error**



**print(8 in 88) # TypeError: argument of type 'int' is not iterable**

**print("8" in "88") #True**

**print(8 in "88") # False TypeError: arguement of type 'str' is not iterable**

**print("a" in "apple") #True**

**print(8 in 88) # TypeError: arguemnt of type 'int' is not iterable**

**print("a" in \["apple", "strawberry"]) # True**



-------------------------------------------------------------------------------------------



7\. Identity operators:



1. Returns Boolean value

2\. It checks whethe the given 2 operands have the same Id or not.





------------------------------------------------------------------------------------------



**Control Flow Statements:**

* **It controls the execution flow of the program.**
* **Types:** 
* **a. Conditional Statements:**
* 
**&nbsp;	if, if-else, elif**

* **Looping Statements:**
* 
**&nbsp;	1. for** 

		**1. for with range()**

			**a. increment**

			**b. decrement**

		**2. for without range()**



	**2. while** 

		**1. increment**

		**2. decrement**



	**3. Jumping Statements**

		**1. break**

		**2. continue**

		**3. return**



**Jumping statements are used to change the normal flow of program execution — that is, to jump from one part of the code to another.**

	











 

