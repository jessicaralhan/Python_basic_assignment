#Assignment 7: Write a python program which contains a dictionary with specific data. The script should accept the key name 
# from command line and output its value from the dict. When specific key is not present in dict, it should give a specific 
# message rather than throwing error and abruptly stopping execution and ask for next input.






data_dict = {
    "name": "jessica",
    "age": 21,
    "profession": "engineer",
    "city": "chandigarh"
}

def main():
    print("Enter a key to get the value")

    while True:

        key = input("Enter a key to search ").strip()

        if key.lower() == "quit":
            print("exit program")
            break

        if key in data_dict:
            print(f" value for '{key}': {data_dict[key]}")
        else:
            print(f"{key} is not found in dictionary")
        
if __name__ == "__main__":
    main()

