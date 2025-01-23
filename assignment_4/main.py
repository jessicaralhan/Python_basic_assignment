#Assignment 4: Write a python program which keeps reading content from command line until the content is 'quit', and then writes the content before quit to a file.



output_file = "user_input.txt"

inputs = []

print("Enter text:")

while True:
    user_input = input() 
    if user_input.lower() == "quit":  
        print(f"Saving inputs to '{output_file}' and exiting.")
        break  
    else:
        inputs.append(user_input)  


with open(output_file, "w") as file:
    for line in inputs:
        file.write(line + "\n")

print(f"Content saved to '{output_file}'.")
