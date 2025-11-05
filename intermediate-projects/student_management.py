studnts_management = {}

while True:
    
    choose = input("""
Choose an option:   
1) Add student
2) View all students
3) Search student
4) See average
5) Delete student
6) Exit
    
Enter your choice: """).lower()
    match choose:
        case "1" | "add student":
            name = input("Enter your name: ")
            enrollment= {}
            
            while True:
                age_input = input("Enter your age: ")
                try:
                    age = int(age_input)
                    if age > 0:
                        break
                    else:
                        print("Age must be a positive number. Try again.")
                except:
                    print("Enter a valid number")

            while True:       
                course_input = input("Enter your course. Type Done when you are finished: ").title()
                if course_input == "Done":
                    break
                grade_input = input(f"Enter your grade for {course_input.title()} (0-100): ")
           
                try:
                    grade = int(grade_input)
                    if 0 <= grade <= 100:
                        enrollment[course_input] = grade
                    else:
                        print("Grade must be between 0 and 100. Try again.")
                except ValueError:
                    print("Please enter a valid number.")
           
            if enrollment:
                studnts_management[name] = {
                     "age": age,
                     "enrollment": enrollment,
                     }
                print(f"{name.title()} registered successfully")

                # print(studnts_grade_management)
            else:
                print(f"{name.title()} was not registered because no courses were entered.")
        
        case "2" | "view all students":
            if studnts_management:
                for name, detail in studnts_management.items():
                    print(f"\nName: {name.title()}\n Age: {detail['age']}\n Enrollments(Course:Grade): {detail['enrollment']}")

            else:
                print("There are no students registered")

        case "3" | "search student":
            search_name = input("Enter student name: ").lower()
            
            if search_name in studnts_management:
                student = studnts_management[search_name]
                print(f"\nName: {search_name.title()}")
                print(f"Age: {student['age']}")
                print("Courses and Grades:")
                for course, grade in student["enrollment"].items():
                    print(f"  - {course}: {grade}")
            else:
                print("Student not found")

        case "4" | "see average":
            average_name = input("Enter the name of student you are searching to see the average : ").lower()
            if average_name in studnts_management:
                grades = studnts_management[average_name]['enrollment'].values()
                if grades:
                    avr = sum(grades) / len(grades)
                    studnts_management[average_name]['average'] = avr
                    print(f"{average_name.title()}'s average grade is {avr}")

                    if avr >= 50:
                        print(f"Status: Passed")
                    else:
                        print(f"Status: Failed")

                else:
                    print("No courses enrolled. Cannot calculate the average.")

            else:
                print(f"Student not found")

        case "5" | "delete student":
            delete_name = input("Enter the name of student you wnat to delete: ")
            if delete_name in studnts_management:
                studnts_management.pop(delete_name)
                print(f"{delete_name.title()} is deleted.") 
            else:
                print("Student not found")

        case "6" | "exit":
            print("Exiting... Goodbye!")
            break

        case _:
            print("Invalid input. Try again")
            