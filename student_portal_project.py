def m_academic():
    print("-------------")
    print(" ACADEMIC")
    print("-------------")
    print("1.Subjects")
    print("2.Credits")
    print("3.Time table")
    print("4.Attendance")
    print("5.Exit")
    inpu2 = int(input("\nEnter your choice(1-4): "))
    if inpu2 == 1:
        a_subjects()
    elif inpu2 == 2:
        a_credits()
    elif inpu2 == 3:
        a_timetable()
    elif inpu2 == 4:
        m_attendance()
    elif inpu2 == 5:
        main()
    else:
        print("Something went wrong...")
        main()

def a_subjects():
    subjects = open("subjects", "r")
    print(subjects.read())
    repeat = input("\nWould you like to return to Academic:")
    if repeat == 'y' or repeat == 'Y' or repeat == 'yes' or repeat == 'YES':
        m_academic()
    else:
        print("exit processing........")
        main()

def a_credits():
    credits = open("credits", "r")
    print(credits.read())
    repeat = input("\nWould you like to return to Academic:")
    if repeat == 'y' or repeat == 'Y' or repeat == 'yes' or repeat == 'YES':
        m_academic()
    else:
        print("exit processing........")
        main()

def m_finance():
    finance = open("finance", "r")
    print(finance.read())
    repeat = input("\nWould you like to return to Main Menu: ")
    if repeat == 'y' or repeat == 'Y' or repeat == 'yes' or repeat == 'YES':
        main()
    else:
        print("exit processing........")
        exit()

def m_examination():
    print("------------------")
    print("   EXAMINATION")
    print("------------------")
    print("1.Marks")
    print("2.Results")
    print("3.Internal Marks")
    print("4.Exit")
    exam = int(input("Enter your choice(1-3): "))
    if exam == 1:
        e_marks()
    elif exam == 2:
        e_result()
    elif exam == 3:
        e_internal_marks()
    elif exam == 4:
        exam_exit()
    else:
        print("something went wrong...")
        main()

def e_marks():
    print("----------------------")
    print("       MARKS")
    print("----------------------")
    marks = open("marks", "r")
    print(marks.read())
    print("----------------------")
    repeat = input("\nWould you like to return to Examination:")
    if repeat == 'y' or repeat == 'Y' or repeat == 'yes' or repeat == 'YES':
        m_examination()
    else:
        print("exit processing........")
        main()

def e_result():
    print("------------------------------")
    print("        RESULT")
    print("------------------------------")
    result = open("result", "r")
    print(result.read())
    print("-----------------------------")
    repeat = input("\nWould you like to return to Examination:")
    if repeat == 'y' or repeat == 'Y' or repeat == 'yes' or repeat == 'YES':
        m_examination()
    else:
        print("exit processing........")
        main()

def e_internal_marks():
    print("\nYou choiced 'internal marks'")
    print("_____________________________")
    print("      INTERNAL MARKS")
    print("_____________________________")
    intmarks = open("internal marks", "r")
    print(intmarks.read())
    print("_____________________________")
    repeat = input("\nWould you like to return to Examination:")
    if repeat == 'y' or repeat == 'Y' or repeat == 'yes' or repeat == 'YES':
        m_examination()
    else:
        print("exit processing........")
        main()

def exam_exit():
    print("Returning to main menu")
    main()

def m_feedback():
    feedback = open("faculty names", "r")
    print(feedback.read())
    fedsel = int(input("Enter your choice(1-4):"))
    if fedsel == 1 or fedsel == 2 or fedsel == 3 or fedsel == 4 or fedsel == 5 or fedsel == 6 or fedsel == 7:
        input("\nRegularity in taking Classes: ")
        input("Helps students in realizing career goal: ")
        input("Completes syllabus of the course in time: ")
        input("Schedule of assignments, class test, quizzes: ")
        input("Helping approach towards varied academic interests of students: ")
        input("Shows the evaluated answer books of class tests to the students: ")
        input("\nFeel Free to give your Feedback: ")
        print("\nThanks you for your Feedback......")
        m_feedback()
    elif fedsel == 8:
        repeat = input("\nWould you like to return to main menu:")
        if repeat == 'y' or repeat == 'Y' or repeat == 'yes' or repeat == 'YES':
            main()
        else:
            print("exit processing........")
            main()
    else:
        print("Some thing went wrong.....")
        main()

def  m_attendance():
    print("Attendance Not Entered.")
    repeat = input("\nWould you like to return to main menu:")
    if repeat == 'y' or repeat == 'Y' or repeat == 'yes' or repeat == 'YES':
        main()
    else:
        print("exit processing........")
        exit()

def intro():
    regnum = input("\nEnter Your Register Number: ")
    if regnum == 'AP21110010617':
        pass1 = int(input("Enter The Password: "))
        if pass1 == 617:
            with open("lets try", 'r') as fp:#functioning programming
                line_numbers = [0, 1, 2, 3, 4, 5, 6, 7]
                lines = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        lines.append(line.strip())
                    elif i > 100:
                        break
            list1 = lines
            num = [str(i) for i in list1]
            x1 = "\n".join(num)
            chaptcha()
        else:
            print("Wrong Password / ID......")
            areyou = input("\nDid you given details before: ")
            if areyou == 'y' or areyou == 'Y' or areyou == 'yes' or areyou == 'YES':
                intro()
            else:
                create_details()

    elif regnum == 'AP21110010618':
        pass1 = int(input("Enter The Password: "))
        if pass1 == 618:
            with open("lets try", 'r') as fp:#functioning programming
                line_numbers = [8, 9, 10, 11, 12, 13, 14, 15]
                lines = []
                for i, line in enumerate(fp):
                    if i in line_numbers:
                        lines.append(line.strip())
                    elif i > 100:
                        break
            list1 = lines
            num = [str(i) for i in list1]
            x1 = "\n".join(num)
            chaptcha()
        else:
            print("Wrong Password / ID......")
            areyou = input("\nDid you given details before: ")
            if areyou == 'y' or areyou == 'Y' or areyou == 'yes' or areyou == 'YES':
                intro()
            else:
                create_details()

    elif regnum == 'AP21110010619':
            pass1 = int(input("Enter The Password: "))
            if pass1 == 619:
                with open("lets try", 'r') as fp:#functioning programming
                    line_numbers = [16, 17, 18, 19, 20, 21, 22, 23]
                    lines = []
                    for i, line in enumerate(fp):
                        if i in line_numbers:
                            lines.append(line.strip())
                        elif i > 100:
                            break
                list1 = lines
                num = [str(i) for i in list1]
                x1 = "\n".join(num)
                chaptcha()
            else:
                print("Wrong Password / ID......")
                areyou = input("\nDid you given details before: ")
                if areyou == 'y' or areyou == 'Y' or areyou == 'yes' or areyou == 'YES':
                    intro()
                else:
                    create_details()

    elif regnum == 'AP21110010620':
            pass1 = int(input("Enter The Password: "))
            if pass1 == 620:
                with open("lets try", 'r') as fp:#functioning programming
                    line_numbers = [24, 25, 26, 27, 28, 29, 30, 31]
                    lines = []
                    for i, line in enumerate(fp):
                        if i in line_numbers:
                            lines.append(line.strip())
                        elif i > 100:
                            break
                list1 = lines
                num = [str(i) for i in list1]
                x1 = "\n".join(num)
                chaptcha()
            else:
                print("Wrong Password / ID......")
                areyou = input("\nDid you given details before: ")
                if areyou == 'y' or areyou == 'Y' or areyou == 'yes' or areyou == 'YES':
                    intro()
                else:
                    create_details()

    elif regnum == 'AP21110010621':
            pass1 = int(input("Enter The Password: "))
            if pass1 == 621:
                with open("lets try", 'r') as fp:#functioning programming
                    line_numbers = [32, 33, 34, 35, 36, 37, 38, 39]
                    lines = []
                    for i, line in enumerate(fp):
                        if i in line_numbers:
                            lines.append(line.strip())
                        elif i > 100:
                            break
                list1 = lines
                num = [str(i) for i in list1]
                x1 = "\n".join(num)
                chaptcha()
            else:
                print("Wrong Password / ID......")
                areyou = input("\nDid you given details before: ")
                if areyou == 'y' or areyou == 'Y' or areyou == 'yes' or areyou == 'YES':
                    intro()
                else:
                    create_details()

    else:
            areyou = input("Did you register before: ")
            if areyou == 'y' or areyou == 'Y' or areyou == 'yes' or areyou == 'YES':
                intro()
            else:
                create_details()

    print(x1)
    print("PORTAL")



def chaptcha():
    import random
    import string
    letters = string.ascii_letters
    print(''.join(random.choice(letters)
    for i in range(5)))
    input("Enter the chaptcha: ")
    print("\n----------------------------------------------------------")
    print("                         PROFILE")
    print("-----------------------------------------------------------")

def a_timetable():
    det4 = input("Enter your Semister: ")
    if det4 == '1' or det4 == 'one' or det4 == 'ONE' or det4 == '1st' or det4 == '1ST':
        with open("time table", 'r') as fp:#functioning programming
            line_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
            lines = []
            for i, line in enumerate(fp):
                if i in line_numbers:
                    lines.append(line.strip())
                elif i > 100:
                    break
        list1 = lines
        num = [str(i) for i in list1]
        x1 = "\n".join(num)

    elif det4 == '2' or det4 == 'TWO' or det4 == 'two' or det4 == '2nd' or det4 == '2ND':
        with open("time table", 'r') as fp: #functioning programming
            line_numbers = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
            lines = []
            for i, line in enumerate(fp):
                if i in line_numbers:
                    lines.append(line.strip())
                elif i > 100:
                    break
        list1 = lines
        num = [str(i) for i in list1]
        x1 = "\n".join(num)

    elif det4 == '3' or det4 == 'three' or det4 == 'THREE' or det4 == '3rd' or det4 == '3RD':
        with open("time table", 'r') as fp: #functioning programming
            line_numbers = [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
            lines = []
            for i, line in enumerate(fp):
                if i in line_numbers:
                    lines.append(line.strip())
                elif i > 100:
                    break
        list1 = lines
        num = [str(i) for i in list1]
        x1 = "\n".join(num)
    elif det4 == '4' or det4 == 'four' or det4 == 'FOUR' or det4 == '4th' or det4 == '4TH':
        with open("time table", 'r') as fp: #functioning programming
            line_numbers = [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
            lines = []
            for i, line in enumerate(fp):
                if i in line_numbers:
                    lines.append(line.strip())
                elif i > 100:
                    break
        list1 = lines
        num = [str(i) for i in list1]
        x1 = "\n".join(num)
    else:
        print("Something went wrong.......")
        main()
    print(x1)
    repeat = input("\nWould you like to return to Academic:")
    if repeat == 'y' or repeat == 'Y' or repeat == 'yes' or repeat == 'YES':
        m_academic()
    else:
        print("exit processing........")
        main()

def create_details():
    print("\nGive your details properly.....")
    f = open("lets try", "a")
    print("__________________________________________________________")
    det1 = input("Enter your Full Name              : ")
    det2 = input("Enter your Semester               : ")
    det6 = input("Enter your program(Btech,mtech...): ")
    det7 = input("Enter your Speciligation          : ")
    det8 = input("Enter your Gender                 : ")
    det9 = input("Enter your D.O.B                  : ")
    det10 = input("Enter your Father Name            : ")
    det11 = input("Enter your Mother Name            : ")
    f.write("\nStudent name           :    ")
    f.write(det1)
    f.write("\nRegister num           :    ")
    #f.write(det4)
    f.write("\nSemester               :    ")
    f.write(det2)
    f.write("\nSection/program        :    ")
    #f.write(det5, )
    f.write(det6)
    f.write("\nSpeciligation          :    ")
    f.write(det7)
    f.write("\nGender/D.O.B           :    ")
    f.write(det8)
    f.write(det9)
    f.write("\nFather/mother name     :    ")
    f.write(det10)
    f.write(det11)
    f.write("\n-----------------------------------------------------------")
    f.close()
    input("\nNOTE: THIS IS ONLY TEMPORARY LOGIN.FOR MORE INFORMATION PLEASE CONTACT OUR FACULTY MEMBERS")
    save = input("\nDo you like to see the details: ")
    if save == 'y' or save == 'Yes' or save == 'Y' or save == 'YES':
        print("______________________________________________")
        print("                 PROFILE")
        print("______________________________________________")
        print("Student name           : ", det1)
        print("Semester               : ", det2)
        print("Program                : ", det6 )#,det5,)
        print("Speciligation          : ", det7)
        print("Gender/D.O.B           : ", det8, "/", det9)
        print("Father/mother name     : ", det10, "/", det11)
        print("______________________________________________")
        print("PORTAL")
        main()
    else:
        main()

def main():
    input("")
    print("-------------")
    print("MAIN MENU")
    print("-------------")
    print("1.Academic")
    print("2.Finance")
    print("3.Examination")
    print("4.Feedback")
    print("5.Exit")
    inpu1 = int(input("\nEnter your choice(1-4): "))
    if inpu1 == 1:
        m_academic()
    elif inpu1 == 2:
        m_finance()
    elif inpu1 == 3:
        m_examination()
    elif inpu1 == 4:
        m_feedback()
    elif inpu1 ==5:
        exit()
    else:
        print("Something went wrong..")
        exit()

print("\nSRMAP, Student Login")
didyou = input("Did you given details before: ")
if didyou == 'y' or didyou == 'Y' or didyou == 'yes' or didyou == 'YES':
    intro()
else:
    create_details()

main()