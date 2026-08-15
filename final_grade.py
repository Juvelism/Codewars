def final_grade(exam, projects):

    if exam > 90 or projects > 10:
        print(100)
    elif exam > 75 and projects >= 5:
        print(90)
    elif exam > 50 and projects >= 2:
        print(75)
    else:
        print(0)

final_grade(55,0)
