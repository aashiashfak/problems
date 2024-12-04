students = [
    {
        'name': "Ameer", 'age':14, 'marks':45
    },
    {
        'name': "Jaiswal", 'age':34, 'marks':55
    },
    {
        'name': "Kanguva", 'age':35, 'marks':95
    },
    {
        'name': "sinan", 'age':18, 'marks':99
    },
]


# def find_adults(students):

#     adults = [student for student in students if student["age"] >= 18]
#     return adults

# adults = find_adults(students)

# print([adult['name'] for adult in adults])



def set_grade(students):

    for student in students:
        if student['marks'] >= 90:
            student['grade'] = 'A'
        elif student['marks'] >= 80:
            student['grade'] = 'B'
        elif student['marks'] >= 70:
            student['grade'] = 'C'
        elif student['marks'] >= 60:
            student['grade'] = 'D'
        else:
            student['grade'] = 'F'
    return students

print(set_grade(students))