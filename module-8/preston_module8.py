# Brian Preston
# CSD 324 - Module 8
# This program works with a JSON file containing student data. It loads the data,
# prints the original student list, adds a new student (myself, Brian Preston),
# prints the updated list, and saves the changes back to the JSON file.

import json

# Define the JSON file name
file_name = "students.json"

# Load JSON data into a Python list
def load_students(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found. Please ensure the JSON file is in the same directory.")
        return []
    except json.JSONDecodeError:
        print("Error reading JSON file. Please ensure it is formatted correctly.")
        return []

# Print the student list
def print_students(students, message):
    print("\n" + message)
    for student in students:
        print(f"{student['F_Name']} , {student['L_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

# Add a new student to the list
def add_student(students):
    new_student = {
        "F_Name": "Brian",
        "L_Name": "Preston",
        "Student_ID": 12345,  # Replace this with another fictional ID if needed
        "Email": "bpreston@my365.bellevue.edu"
    }
    students.append(new_student)
    return students

# Save updated students list back to JSON
def save_students(file_name, students):
    with open(file_name, 'w') as file:
        json.dump(students, file, indent=4)
    print("\nThe student.json file has been updated.")

# Main program logic
def main():
    # Load the students list from the file given
    students = load_students(file_name)
    
    if not students:
        return
    
    # Print the original student list
    print_students(students, "Original Student List:")
    
    # Add a new student to the list
    students = add_student(students)
    
    # Print the updated student list
    print_students(students, "Updated Student List:")
    
    # Save the updated list back to the JSON file
    save_students(file_name, students)

# Run the program
if __name__ == "__main__":
    main()

