student_records=[]

while True:
    print("========================================")
    print("-----  STUDENT DATA ORGANIZER 🗂️-----")
    print("========================================")
    print("SELECT AN OPTION FROM 1 TO 6:")
    print("1. ADD STUDENT DATA.")
    print("2. DISPLAY ALL STUDENT DATA.")
    print("3. UQDATE STUDENT INFORMATION.")
    print("4. DELETE STUDENT RECORD.")
    print("5. DISPLAY STUDENT OFFERED.")
    print("6. EXIT.")
    choice=int(input("enter your choice from (1 to 6):"))

    if choice==1:
        name=input("enter student name:")
        age=int(input("enter student age:"))
        dob=input("enter student date of birth (DD/MM/YYYY):")
        student_id=int(input("enter student ID:"))
        offered_course=input("enter offered course:")
        grade=input("enter student grade:")
        student= {
            "Name": name,
            "Age": age,
            "Student ID": student_id,
            "Offered Course": offered_course,
            "dob": dob,
            "grade": grade,
            }
        student_records.append(student)
        print("student record added successfully.")

    elif choice==2:
         for student in student_records:
                print("---------------------------")
                for k, v in student.items():
                    print(k, ":", v)
    elif choice==3:
        student_id=int(input("enter student ID to update:"))
        for student in student_records:
            if student_id==student.get("Student ID"):
                print("enter new details:")
                name=input("enter student name:")
                age=int(input("enter student age:"))
                dob=input("enter student date of birth (DD/MM/YYYY):")
                offered_course=input("enter offered course:")
                grade=input("enter student grade:")
                student.update({
                    "Name": name,
                    "Age": age,
                    "Offered Course": offered_course,
                    "dob": dob,
                    "grade": grade,
                })
                print("student record updated successfully.")
                break
            else:
             print("student ID not found.")
    elif choice==4:
        student_id=int(input("enter student ID to delete:"))
        for i, student in enumerate(student_records):
            if student_id==student.get("Student ID"):
                del student_records[i]
                print("student record deleted successfully.")
                break
        else:
            print("student ID not found.")
    elif choice==5:
        offered_course=input("enter course offered by student:")
        for student in student_records:
            if offered_course==student.get("Offered Course"):
                for k, v in student.items():
                    print(k, ":", v)
                break
        else:
            print("course not found.")
    elif choice==6:
        print("Thank you for using STUDENT DATA ORGANIZER😇.")
        print("BYE👋🏻")
        break
    else:
        print("invalid choice❌.")