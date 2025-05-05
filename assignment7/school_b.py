
import sqlite3

def enroll_student(cursor, student, course):    
    cursor.execute("SELECT * FROM Students WHERE name = ?", (student,)) # For a tuple with one element, you need to include the comma
    result = cursor.fetchone()
    if result:
        student_id = result[0]
    else:
        print(f"There is no student named {student}.")
        return

    cursor.execute("SELECT * FROM Courses WHERE course_name = ?", (course,))
    result = cursor.fetchone()
    if result:
        course_id = result[0]
    else:
        print(f"There is no course named {course}.")
        return

    cursor.execute(
        "INSERT INTO Enrollments (student_id, course_id) VALUES (?, ?)",
        (student_id, course_id)
    )

with sqlite3.connect("../db/school.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Alice', 20, 'Computer Science')")
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Bob', 22, 'History')")
    cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Charlie', 19, 'Biology')")

    cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Math 101', 'Dr. Smith')")
    cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('English 101', 'Ms. Jones')")
    cursor.execute("INSERT INTO Courses (course_name, instructor_name) VALUES ('Chemistry 101', 'Dr. Lee')")

    enroll_student(cursor, "Alice", "Math 101")
    enroll_student(cursor, "Alice", "Chemistry 101")
    enroll_student(cursor, "Bob", "Math 101")
    enroll_student(cursor, "Bob", "English 101")
    enroll_student(cursor, "Charlie", "English 101")

    conn.commit()
    print("Sample data inserted successfully.")
