def process_file(file_path, rollno_to_find):
    with open(file_path, 'r') as file:
        header = file.readline()

        for line in file:
            roll_no = line[0:13].strip()
            if roll_no == rollno_to_find:
                fields = line.split()
                course_title, mid_mark, sessional_marks, final_marks, credit_hours, name = fields[1], int(fields[2]), int(fields[3]), int(fields[4]), int(fields[5]), ' '.join(fields[6:])

                total_marks = mid_mark + sessional_marks + final_marks
                grade = calculate_grade(total_marks)
                gpa = calculate_gpa(grade)

                result_message = (
                    f"{name}\t "
                    f"{roll_no}\t"
                    f"{course_title}\t\t"
                    f"{mid_mark}\t"
                    f"{sessional_marks}\t"
                    f"{final_marks}\t"
                    f"{total_marks}\t"
                    f"{grade}\t"
                    f"{gpa}\t"
                    f"{credit_hours}"
                )
                with open('output.txt', 'a') as output_file:
                    print(result_message, file=output_file)
                return gpa, credit_hours

    print(f"No information found for RollNo: {rollno_to_find} in {file_path}")
    return 0.0, 0

def calculate_grade(total_marks):
    if total_marks >= 85:
        return 'A+'
    elif 80 <= total_marks <= 84:
        return 'A'
    elif 75 <= total_marks <= 79:
        return 'B+'
    elif 71 <= total_marks <= 74:
        return 'B'
    elif 70 <= total_marks <= 70:
        return 'B-'
    elif 65 <= total_marks <= 69:
        return 'C+'
    elif 60 <= total_marks <= 64:
        return 'C'
    elif 55 <= total_marks <= 59:
        return 'D'
    elif 50 <= total_marks <= 54:
        return 'D'
    else:
        return 'F'

def calculate_gpa(grade):
    grade_points = {'A+': 4.0, 'A': 3.8, 'B+': 3.6, 'B': 3.3, 'B-': 3.0, 'C+': 2.7, 'C': 2.0, 'D': 1.7, 'F': 0.0}
    return grade_points.get(grade, 0.0)

def calculate_cgpa(subjects_gpa_credit):
    total_gpa = 0.0
    total_credit_hours = 0
    for gpa, credit_hours in subjects_gpa_credit:
        total_gpa += gpa * credit_hours
        total_credit_hours += credit_hours

    if total_credit_hours == 0: 
        return 0.0

    return total_gpa / total_credit_hours

subjects_gpa_credit = []

rollno_to_find =input('Enter Roll No:')

gpa, credit = process_file('Python.txt', rollno_to_find)
subjects_gpa_credit.append((gpa, credit))

gpa, credit = process_file('Quran.txt', rollno_to_find)
subjects_gpa_credit.append((gpa, credit))

gpa, credit = process_file('Islamiyat.txt', rollno_to_find)
subjects_gpa_credit.append((gpa, credit))

gpa, credit = process_file('DLD.txt', rollno_to_find)
subjects_gpa_credit.append((gpa, credit))

gpa, credit = process_file('Probability.txt', rollno_to_find)
subjects_gpa_credit.append((gpa, credit))

gpa, credit = process_file('CPS.txt', rollno_to_find)
subjects_gpa_credit.append((gpa, credit))

cgpa = calculate_cgpa(subjects_gpa_credit)
cgpa = calculate_cgpa(subjects_gpa_credit)
with open('output.txt', 'a') as output_file:
    print(f"CGPA: {cgpa:.2f}", file=output_file)

file = open('output.txt', 'r')
print('COURSE_TITLE\tMID_MARKS\tSE.MARKS\tFINAL_MARKS\tTOTAL_MARKS\tGRADES\tGPA')
for line in file:
    fields = line.strip().split('\t')
    if len(fields) >= 10:
        name = fields[0]
        roll_no = fields[1]
        course_title = fields[2]
        mid_mark = (fields[3])
        sessional_marks = int(fields[4])
        final_marks = int(fields[5])
        total_marks = int(fields[6])
        grade = fields[7]
        gpa = (fields[8])
        credit_hours = (fields[9])

        print(f'{course_title}\t{mid_mark}\t{sessional_marks}\t\t{final_marks}\t\t{total_marks}\t\t{grade}\t\t{gpa}\t{credit_hours}')
print(line)
file.close()

with open('output.txt', 'r') as input_file, open('BSDSF22A042.txt', 'w') as output_file:
    print(f'NAME:\t{name}',file=output_file)
    print('COURSE_TITLE\tMID_MARKS\tSE.MARKS\tFINAL_MARKS\tTOTAL_MARKS\tGRADES\tGPA', file=output_file)
    for line in input_file:
        fields = line.strip().split('\t')
        if len(fields) >= 10:
            name = fields[0]
            roll_no = fields[1]
            course_title = fields[2]
            mid_mark = fields[3]
            sessional_marks = int(fields[4])
            final_marks = int(fields[5])
            total_marks = int(fields[6])
            grade = fields[7]
            gpa = fields[8]
            credit_hours = fields[9]

            print(f'{course_title}\t{mid_mark}\t{sessional_marks}\t\t{final_marks}\t\t{total_marks}\t\t{grade}\t\t{gpa}\t{credit_hours}', file=output_file)
    print(f'CGPA:\t{cgpa:.2f}', file=output_file) 








