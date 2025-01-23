#Assignment 6: Write a program which will be able to accept Student data with help of different functions, to eventually 
# store all data in one dictionary, and finally print out all content of that dictionary variable.




# def dict(my_dict):
#     for key, value in my_dict.items():
#         print(f"{key} : {value}")

# dict({"Name": "Jessica", "Age": "21"})

def get_student_name():
    return input("enter student's name")

def get_student_age():
    return int(input("enter student's age"))

def get_student_grade():
    return input("enter student's grade")

def collect_student_data():
    student_data = {
        "name": get_student_name(),
        "age": get_student_age(),
        "grade": get_student_grade(),

    }
    return student_data

def main():
    students = []
    while True:
        print("collecting new student data")
        student = collect_student_data()
        students.append(student)

        another = input("Do you want to add another student? (yes/no): ").strip().lower()
        if another != "yes":
            break

    print("\nFinal student data:")
    for student in students:
        print("\nStudent:")
        for key, value in student.items():
            print(f"{key.capitalize()}: {value}")

if __name__=="__main__":
    main()

















































