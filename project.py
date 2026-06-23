print("# --------- STUDENT MANAGEMNET SYSTEM --------- #")

print("\n WELCOME TO THE STUDENT DATA ORGANIZER ! ")

student_data = []

while True :
    print()
    print("Select an Option : ")
    print("1 . Add Student")
    print("2 . Display All Student ")
    print("3 . Update Student Information")
    print("4 . Delete Student Record")
    print("5 . Display Subject Offered")
    print("6 . Exit")

    choice = int(input("\nEnter Your Choice : "))

    match choice :
        case 1 :
            print("\nEnter Studets Detail : ")
            s_id = int(input("Student Id : "))
            name = str(input("Name : "))
            age = int(input("Age : "))
            grade = input("Grade : ")
            dob = input("Date Of Birth(YYYY-MM-DD) : ")
            subject = input("Subjects (Seprate by comma) : ")

            id_dob = (s_id,dob)
            sub_set = set(subject.split(","))

            student = {"Id_dob" : id_dob,
                       "Name" : name,
                       "Age" : age,
                       "Grade" : grade,
                       "Subjects" : sub_set}

            student_data.append(student)

            print("\nStudent %d's Details Added succesfully ! "%student['Id_dob'][0])

        case 2 :
            
            print("\n-------DISPLAY STUDENT DETAILS--------")
            for student in student_data :
                print(f"\nStudent ID : {student[ 'Id_dob'][0]} | Name : {student['Name']} | Age : {student['Age']} | Grade : {student['Grade']} | DoB : {student['Id_dob'][1]} | Subject : {','.join(student['Subjects'])}")

        case 3 :

            print("\nUPDATE STUDENT DETAILS : ")
            
            search_id = int(input("\nSearch Student Id : "))
            found = False

            for student in student_data :
                if student['Id_dob'][0] == search_id :
                    found = True
                    
                    new_age = int(input("\nEnter New Age : "))
                    new_grade = input("Enter New Grades : ")
                    new_sub = input("Enter New subjects : ")

                    new_sub_set=set(new_sub.split(","))

                    student['Age'] = new_age
                    student['Grade'] = new_grade
                    student['Subjects'] = new_sub_set

                    print("\nStudents {}'s Details Updated Successfully ! ".format(student['Id_dob'][0]))

                    break
                    
            if not found :
                print("\nStudent not found !")
                         
        case 4 :
            print("\nDELETATION OF STUDENT RECORD")

            del_id = int(input("Delete Student Id  : "))
            found = False

            for i in range(len(student_data)) :
                if student_data[i]['Id_dob'][0] == del_id :
                    del student_data[i]
                    found = True

                    print("\nStudent Data Deleted Successfully !")

                    break

            if found == False :
                print("\nStudent Not Found !")

        case 5 :

            all_sub = set()

            for student in student_data :
                for subject in student['Subjects'] :
                    all_sub.add(subject)

            print("\nUnique Subjects : ")
            print()
            for subject in all_sub :
                print(subject)

        case 6 :
            print("\nExiting The Student Data Organizer..... ! ")
            break

        case _ :
            print("\n Kindly Enter Valid Choice...!")

            
            
            

