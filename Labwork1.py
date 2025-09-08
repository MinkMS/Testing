students = []
courses = []
marks = {}

def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_info():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth (DD/MM/YYYY): ")
    students.append((student_id, student_name, student_dob))

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    courses.append((course_id, course_name))

def input_marks_for_course(course_id):
    print(f"Entering marks for course {course_id}")
    for student_id, _, _ in students:
        mark = float(input(f"Enter mark for student {student_id}: "))
        marks[(student_id, course_id)] = mark

def list_courses():
    for course_id, course_name in courses:
        print(f"{course_id}: {course_name}")

def list_students():
    for student_id, student_name, student_dob in students:
        print(f"{student_id}: {student_name}, Date of birth: {student_dob}")

def show_marks(course_id):
    print(f"Marks for course {course_id}:")
    for (student_id, cid), mark in marks.items():
        if cid == course_id:
            print(f"Student {student_id}: {mark}")

def main():
    num_students = input_number_of_students()
    for _ in range(num_students):
        input_student_info()

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        input_course_info()

    for course_id, _ in courses:
        input_marks_for_course(course_id)

    list_courses()
    list_students()

    selected_course_id = input("Enter the course ID to show marks: ")
    show_marks(selected_course_id)

if __name__ == "__main__":
    main()