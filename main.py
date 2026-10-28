with open('data.txt', 'r') as f:
    data = f.read()

def parse_student(student_string):
    student_list = student_string.split("\n")
    name = student_list[0]
    noten = student_list[1:]
    student_dict = {
        'name': name,
        'grades': noten
    }
    return student_dict

student_strings = data.split('\n\n')

student_dicts = []
for student_string in student_strings:
    student_dict = parse_student(student_string)
    student_dicts.append(student_dict)

print(student_dicts)