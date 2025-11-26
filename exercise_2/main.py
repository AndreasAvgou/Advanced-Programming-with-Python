# File: main.py
from student import Student        # Import the model
from manager import StudentManager # Import the controller logic

def main():
    FILENAME = "students.csv"
    
    # 1. Initialize the Manager
    manager = StudentManager()

    # 2. Load existing data from CSV
    print("--- Starting Application ---")
    manager.load_from_csv(FILENAME)

    # 3. Display currently loaded data
    manager.print_all_students()

    # 4. Interactive section: Add a new student
    print("--- Add New Student ---")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    st_id = input("Enter Student ID: ")
    
    # Create the Student object
    new_student = Student(name, age, st_id)
    
    # Add grades
    grades_input = input("Enter grades separated by space (e.g., 8 9.5 10): ")
    for g in grades_input.split():
        new_student.add_grade(g)
        
    # Add the new student to the manager
    manager.add_student(new_student)

    # 5. Show the updated list
    manager.print_all_students()

    # 6. Save changes option
    save_choice = input("Do you want to save changes to CSV? (yes/no): ").lower()
    if save_choice == 'yes' or save_choice == 'y':
        manager.save_to_csv(FILENAME)
    else:
        print("Changes discarded.")

# Entry point check
if __name__ == "__main__":
    main()