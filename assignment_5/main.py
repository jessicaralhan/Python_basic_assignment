#Assignment 5: Write a program in Python which will be able to accept any number of arguments in the same function and can process it.





def my_function(*fname):
    print("Processing names")

    for name in fname:
        print(f"- {name}")

    if len(fname) > 7:
        print("My name is" + " " + fname[5])
    else:
        print("cannot access names")


        
my_function("jessica", "yachika", "vishwas", "monika", "lemon", "matcha")
