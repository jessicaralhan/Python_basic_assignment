#Assignment 1: Write a python script which will be able to accept the data on command line as input and will be able to identify and 
# print out the datatype of the given input.



user_input = input("Enter the data")


if user_input.isdigit():
    print("yes it is a digit")
elif user_input.count(".")==1:
    print("it is float")
elif user_input.lower()=="true" or user_input.lower()=="false":
    print("bool")
elif user_input.startswith("[") and user_input.endswith("]"):
    print("list")
elif user_input.startswith("{") and user_input.endswith("]"):
    print("dict")
elif user_input.startswith("(") and user_input.endswith(")"):
    print("touple")
else:
    print("string")