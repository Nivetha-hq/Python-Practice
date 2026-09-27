students = []
def add_student():
    print("\n--- Add Student ---")
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    department = input("Enter department: ")
    mark = int(input("Enter mark: "))
    student = [name, roll_no, department, mark]
    students.append(student)
    print("\nStudent added successfully!")
def show_students():
    print("\n--- Student List ---")
    if len(students) == 0:
        print("No students have been added yet.")
    else:
        for student in students:
            print("\nName       :", student[0])
            print("Roll No    :", student[1])
            print("Department :", student[2])
            print("Mark       :", student[3])
def find_student():
    print("\n--- Search Student ---")
    roll_no = input("Enter roll number: ")
    for student in students:
        if student[1] == roll_no:
            print("\nStudent found! ")
            print("Name       :", student[0])
            print("Roll No    :", student[1])
            print("Department :", student[2])
            print("Mark       :", student[3])
            return
    print("Sorry, student not found.")
def main():
    while True:
        print("\n ==============================")
        print("\t STUDENT MANAGEMENT")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")
        print("==============================")
        choice = input("What would you like to do? ")
        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            find_student()
        elif choice == "4":
            print("\nThanks for using my Student Management System!")
            break
        else:
            print("\nPlease choose a valid option.")
main()