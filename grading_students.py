def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] < 38:pass
        elif abs(((grades[i]%5)-5)) < 3:
            grades[i] = (grades[i]-(grades[i]%5))+5
    return grades
    
print(gradingStudents([73,67,38,33]))
