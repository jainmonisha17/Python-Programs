print(55 or (66 and False))
print((2 * 0) or (False ** True)) # 2 * 0 times is 0 -> False and False ** True is also False -> False-0, True-1 -> 0 * 1 time is 0
print((10 and 0) or (0 and 1)) # 10 and 0 is 0 -> 10 is a value and 0 is not a value so 0 is False, True and False is False, OR False and 1 is also False -> 0 
print(False ** True) # False ** True is 0 ** 1 is 0 