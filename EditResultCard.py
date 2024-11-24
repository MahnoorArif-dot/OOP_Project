from ResultCard import*

file_path = 'Quran.txt'
with open(file_path, 'r') as file:
    read = file.readlines()

rollno_to_find = input('Enter RollNo: ')
index_to_update = None

for i, line in enumerate(read):
    roll_no = line[0:13].strip()
    if roll_no == rollno_to_find:
        index_to_update = i
        break

if index_to_update is not None:
    fields = [
        line[0:13].strip(),  
        line[14:29].strip(),  
        (line[30:32].strip()),  
        (line[33:35].strip()),  
        (line[36:38].strip()),  
        (line[39:41].strip()),  
        line[42:].strip()  
    ]

    fields[0] = input('Enter RollNo:').ljust(15)
    fields[1] = input('Enter Course Title: ').ljust(15)
    fields[2] = str(int(input('Enter Mid Mark: '))).ljust(11)
    fields[3] = str(int(input('Enter Sessional Marks: '))).ljust(18)
    fields[4] = str(int(input('Enter Final Marks: '))).ljust(12)
    fields[5] = str(int(input('Enter Credit Hour: '))).ljust(13)
    fields[6] = input('Enter Name: ').ljust(15)
    updated_line = f"{fields[0]} {fields[1]} {fields[2]:>2} {fields[3]:>2} {fields[4]:>2} {fields[5]:>2} {fields[6]}\n"
    read[index_to_update] = updated_line

    with open(file_path, 'w') as file:
        file.writelines(read)
else:
    print(f'RollNo {rollno_to_find} not found.')


