students = []

def add_student():
    s_id = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")
    
    student = {"ID": s_id, "Name": name, "Age": age, "Course": course, "Marks": marks}
    students.append(student)
    print("Student added!")

def view_all():
    if len(students) == 0:
        print("No students found.")
    else:
        for s in students:
            print(f"ID: {s['ID']} | Name: {s['Name']} | Age: {s['Age']} | Course: {s['Course']} | Marks: {s['Marks']}")

def search_student():
    search = input("Enter ID or Name to search: ")
    found = False
    for s in students:
        if s["ID"] == search or s["Name"].lower() == search.lower():
            print(f"Found! ID: {s['ID']} | Name: {s['Name']} | Age: {s['Age']} | Course: {s['Course']} | Marks: {s['Marks']}")
            found = True
    if not found:
        print("Student not found.")

def update_student():
    search_id = input("Enter Student ID to update: ")
    found = False
    for s in students:
        if s["ID"] == search_id:
            s["Name"] = input(f"Enter new Name ({s['Name']}): ")
            s["Age"] = input(f"Enter new Age ({s['Age']}): ")
            s["Course"] = input(f"Enter new Course ({s['Course']}): ")
            s["Marks"] = input(f"Enter new Marks ({s['Marks']}): ")
            print("Student updated!")
            found = True
            break
    if not found:
        print("Student ID not found.")

def delete_student():
    search_id = input("Enter Student ID to delete: ")
    found = False
    for s in students:
        if s["ID"] == search_id:
            students.remove(s)
            print("Student deleted!")
            found = True
            break
    if not found:
        print("Student ID not found.")

while True:
    print("\n--- STUDENT MENU ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    
    choice = input("Enter choice (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please choose 1 to 6.")
