#Assignment 8: Perform the same task as in assignment 5, but with the help of class and its object.





class StudentProcessor:
    def __init__(self):
        self.students = []

    def add_students(self, *students):
        self.students.extend(students)

    def display_students(self):
        print("\n list of students-")
        for student in self.students:
            print(student)

processor = StudentProcessor()

processor.add_students("jessica", "yachika")
processor.add_students("lemon", "matcha")
processor.display_students()