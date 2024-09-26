# Student Grade Management System

students = {}   # Dictionary to store student details in {name = {subject: grade}} format

# Function to add a new student
def add_student():
    name = input("Enter student Name: ").strip() # strip is used to remove spaces in inputs.
    if name in students:
        print(f"{name} already exists. Updating grades")
    else:
        students[name] = {} # if there's no duplicate elements, it will add to the students variable.
    
    try:
        num_subjects = int(input("Enter the number of subjects: "))
                
        for i in range(num_subjects):
            subject = input("Enter subject name: ").strip()
            grade = int(input(f"Enter grade for {subject}: "))
            if (0 <= grade <= 100):
                students[name][subject] = grade
            else:
                print("Grade must be between 0 and 100.")
                return
        print(f"{name} has been added with the provided subjects and grades.")
    
    except ValueError:
        print("Invalid number of subjects! Please enter a numeric value.")
# Function to update an existing student grade
def update_student():
    name = input("Enter the student name whose grades you want to update: ").strip()
    if name in students:
        if not students[name]:
            print(f"No subjects found for {name}. Please add subjects first.")
            return
        
        subject = input("Enter the subject name to update: ").strip()
        if subject in students[name]:
            try:
                grade = float(input(f"Enter new grade for {subject}: ").strip())
                if 0 <= grade <= 100:
                    students[name][subject] = grade
                    print(f"Grade for {subject} has been updated to {grade}.")
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid grade! Please enter a numeric value.")
        else:
            print(f"{subject} not found for {name}.")
    else:
        print(f"{name} is not found in the system.")
# Function to calculate the average grade of all subjects for each student
def calculate_average():
    if students:
        for name, subjects in students.items():
            if subjects:
                average_grade = sum(subjects.values()) / len(subjects)
                print(f"The average grade for {name} is: {average_grade:.2f}")
            else:
                print(f"No subjects to calculate average for {name}.")
    else:
        print("No students in the system to calculate average.")
# Function to display all students and their grades
def display_all_students():
    if students:
        print("Student List:")
        for name, subjects in students.items():
            if subjects:
                print(f"Name: {name}")
                for subject, grade in subjects.items():
                    print(f" Subject: {subject}, Grade: {grade}")
            else:
                print(f"Name: {name} (No subjects)")
    else:
        print("No Students to Display")
# Main function to display the menu and take user input
def main():
    print("Student Grade Management System")
    print("1. Add New Student")
    print("2. Update Student Grades")
    print("3. Calculate Average Grade")
    print("4. Display All Students")
    print("5. Exit")
    while True:  
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            calculate_average()
        elif choice == '4':
            display_all_students()
        elif choice == '5':
            print("Exiting the system, Have a Great Learning.")
            break
        else:
            print("Invalid data. Please select a valid option.")
# Calling the main function to run.
main()
