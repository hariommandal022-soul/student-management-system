print("===== Student Management System =====")

students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        students.append([roll, name, marks])

        print("Student Added Successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No Students Found")

        else:
            print("\nStudent Records")

            for student in students:
                print(
                    "Roll:", student[0],
                    "Name:", student[1],
                    "Marks:", student[2]
                )

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
