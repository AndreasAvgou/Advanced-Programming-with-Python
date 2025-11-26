# File: student.py

class Student:
    """Represents a student with personal details and grades."""
    
    def __init__(self, name, age, student_id):
        # Initialize the student's attributes
        self.name = name
        self.age = int(age)
        self.student_id = student_id
        self.grades = []  # List to store grades

    def add_grade(self, grade):
        """Adds a grade to the student's record (must be between 0 and 10)."""
        try:
            g = float(grade)
            # Check if grade is within valid range
            if 0 <= g <= 10:
                self.grades.append(g)
            else:
                print(f"[Warning] Grade {g} is out of bounds (0-10). Ignored.")
        except ValueError:
            print(f"[Error] Invalid grade format '{grade}'.")

    def get_average(self):
        """Calculates the average grade of the student."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        """Returns a string representation of the student object."""
        avg = self.get_average()
        # Convert grades list to a string separated by commas
        grades_str = ", ".join(map(str, self.grades))
        return (f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | "
                f"Avg: {avg:.2f} | Grades: [{grades_str}]")