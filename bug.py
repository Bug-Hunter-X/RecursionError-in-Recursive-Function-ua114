def my_function(x):
    if x == 0:
        return 1
    else:
        return x * my_function(x - 1)

print(my_function(5)) #This will work fine
print(my_function(-1)) #This will cause a RecursionError