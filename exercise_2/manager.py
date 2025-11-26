# File: manager.py
import csv
import os
from student import Student  # <-- Importing the Student class from student.py

class StudentManager:
    """Manages a collection of Student objects and file I/O operations."""

    def __init__(self):
        self.students = []

    def add_student(self, student):
        """Adds a Student object to the list."""
        self.students.append(student)
        print(f"[Info] Student '{student.name}' added successfully.")

    def load_from_csv(self, filename):
        """Loads student data from a CSV file."""
        # Check if file exists before trying to open
        if not os.path.exists(filename):
            print(f"[Warning] File '{filename}' not found. Starting with an empty list.")
            return

        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip the header row
                
                for row in reader:
                    # Basic validation to ensure row has enough columns
                    if len(row) < 4: 
                        continue
                    
                    # Create a new Student object using data from CSV
                    # row[0]=Name, row[1]=Age, row[2]=ID
                    new_student = Student(row[0], row[1], row[2])
                    
                    # Parse grades string (assumed to be separated by semicolons)
                    if row[3]:
                        for g in row[3].split(';'):
                            new_student.add_grade(g)
                    
                    self.students.append(new_student)
            
            print(f"[Success] Loaded {len(self.students)} students from '{filename}'.")

        except Exception as e:
            print(f"[Error] Failed to load CSV file: {e}")

    def save_to_csv(self, filename):
        """Saves the current list of students to a CSV file."""
        try:
            with open(filename, mode='w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                # Write the header row
                writer.writerow(["Name", "Age", "StudentID", "Grades"])
                
                for student in self.students:
                    # Join grades with a semicolon for storage
                    grades_str = ";".join(map(str, student.grades))
                    writer.writerow([student.name, student.age, student.student_id, grades_str])
            
            print(f"[Success] Data successfully saved to '{filename}'.")
            
        except Exception as e:
            print(f"[Error] Failed to save to CSV file: {e}")

    def print_all_students(self):
        """Prints the details of all students in the manager."""
        print("\n" + "="*30)
        print("       STUDENT LIST       ")
        print("="*30)
        
        if not self.students:
            print("No students found.")
        else:
            for s in self.students:
                print(s)  # This calls the __str__ method of Student
        
        print("="*30 + "\n")