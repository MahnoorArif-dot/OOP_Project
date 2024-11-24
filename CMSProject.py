import tkinter as tk
from tkinter import ttk, simpledialog,messagebox
from PIL import Image, ImageTk

class StudentOptionsWindow:
    def __init__(self, master, rollno):
        self.master = master
        self.rollno = rollno
        self.window = tk.Toplevel(self.master)
        self.window.title("Student Options")
        self.window.geometry('400x300')

        ttk.Button(self.window, text="View Result", command=self.view_result).pack(pady=10)
        ttk.Button(self.window, text="Add/Drop Subject", command=self.add_drop_subject).pack(pady=10)
        ttk.Button(self.window, text="View Attendance Sheet", command=self.view_attendance).pack(pady=10)

    def view_result(self):
        result_window = tk.Toplevel(self.window)
        result_window.title("View Result")
        result_window.geometry('400x300')
        file_path = f'{self.rollno}.txt'

        try:
            with open(file_path, 'r') as file:
                result_text = file.read()
                result_label = tk.Label(result_window, text=result_text)
                result_label.pack(pady=10)
        except FileNotFoundError:
            result_label = tk.Label(result_window, text=f"No result found for {self.rollno}")
            result_label.pack(pady=10)

    def view_attendance(self):
        attendance_window = tk.Toplevel(self.window)
        attendance_window.title("View Attendance Sheet")
        attendance_window.geometry('400x300')

        subject_selection_label = ttk.Label(attendance_window, text="Select Subject:")
        subject_selection_label.grid(row=2, column=0, padx=10, pady=5)

        self.subject_selection_combobox = ttk.Combobox(attendance_window, values=["Python", "DLD", "CPS", "Quran", "Islamiyat", "Probability"])
        self.subject_selection_combobox.grid(row=2, column=1, padx=10, pady=5)
        self.subject_selection_combobox.set("Python")

        view_button = ttk.Button(attendance_window, text="Enter", command=self.view_attendance_file)
        view_button.grid(row=3, column=0, columnspan=2, pady=10)

    def view_attendance_file(self):
        selected_subject = self.subject_selection_combobox.get()
        file_path = f'{selected_subject}_attendance.txt'

        try:
            with open(file_path, 'r') as file:
                att_text = file.read()
                att_text_window = tk.Toplevel(self.window)
                att_text_window.title(f"Attendance for {selected_subject}")
                att_text_window.geometry('400x300')
                att_text_widget = tk.Text(att_text_window, wrap='word', height=100, width=150)
                att_text_widget.insert(tk.END, att_text)
                att_text_widget.pack(pady=10)
        except FileNotFoundError:
            att_label = tk.Label(self.window, text=f"No attendance found for {selected_subject}")
            att_label.pack(pady=10)

    def add_drop_subject(self):
        add_drop_window = tk.Toplevel(self.window)
        add_drop_window.title("Add/Drop Subject")
        add_drop_window.geometry('400x300')

        email_label = ttk.Label(add_drop_window, text="Email:")
        email_label.grid(row=0, column=0, padx=10, pady=5)
        self.email_entry = ttk.Entry(add_drop_window)
        self.email_entry.grid(row=0, column=1, padx=10, pady=5)

        password_label = ttk.Label(add_drop_window, text="Password:")
        password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = ttk.Entry(add_drop_window, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        subject_selection_label = ttk.Label(add_drop_window, text="Select Subject:")
        subject_selection_label.grid(row=2, column=0, padx=10, pady=5)
        self.subject_selection_combobox = ttk.Combobox(add_drop_window, values=["Python", "DLD", "CPS", "Quran", "Islamiyat", "Probability"])
        self.subject_selection_combobox.grid(row=2, column=1, padx=10, pady=5)
        self.subject_selection_combobox.set("Python")

        operation_selection_label = ttk.Label(add_drop_window, text="Select operation:")
        operation_selection_label.grid(row=3, column=0, padx=10, pady=5)
        operation_selection_combobox = ttk.Combobox(add_drop_window, values=["Add", "Drop"])
        operation_selection_combobox.grid(row=3, column=1, padx=10, pady=5)
        operation_selection_combobox.set("Add")

        add_drop_button = ttk.Button(add_drop_window, text="Add/Drop Subject", command=lambda: self.email_check(operation_selection_combobox.get()))
        add_drop_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.message_var = tk.StringVar()
        message_label = ttk.Label(add_drop_window, textvariable=self.message_var, foreground="red")
        message_label.grid(row=5, column=0, columnspan=2, pady=5)

    def email_check(self, operation):
        email = self.email_entry.get()
        password = self.password_entry.get()
        subject = self.subject_selection_combobox.get()

        if email == 'pucitadd\drop@gmail.com' and password == 'fcit123':
            if operation == "Add":
                self.message_var.set(f"{self.rollno} Your application is transferred successfully for {subject}.")
            elif operation == "Drop":
                self.message_var.set(f"{self.rollno} Your application is dropped successfully for {subject}.")
        else:
            self.message_var.set("Incorrect email or password")

class TeacherOptionsWindow:
    def __init__(self, master, teacher_name):
        self.master = master
        self.teacher_name = teacher_name
        self.window = tk.Toplevel(self.master)
        self.window.title("Teacher Options")
        self.window.geometry('400x300')

        ttk.Button(self.window, text="View Result", command=self.prompt_roll_number).pack(pady=10)
        ttk.Button(self.window, text="View Attendance Sheet", command=self.view_attendance).pack(pady=10)
        ttk.Button(self.window, text="View Marks Sheet", command=self.view_marks).pack(pady=10)
        ttk.Button(self.window, text="Edit Marks Sheet", command=self.edit_marksheet).pack(pady=10)



    def prompt_roll_number(self):
        roll_number = simpledialog.askstring("Enter Roll Number", "Please enter the student's roll number:")
        if roll_number:
            self.view_result(roll_number)

    def view_result(self, roll_number):
        result_window = tk.Toplevel(self.window)
        result_window.title("View Result")
        result_window.geometry('400x300')
        file_path = f'{roll_number}.txt'

        try:
            with open(file_path, 'r') as file:
                result_text = file.read()
                result_label = tk.Label(result_window, text=result_text)
                result_label.pack(pady=10)
        except FileNotFoundError:
            result_label = tk.Label(result_window, text=f"No result found for {roll_number}")
            result_label.pack(pady=10)

    def view_attendance(self):
        teacher_users = {
            "Idrees": "Python_attendance.txt",
            "Tahir": "Quran_attendance.txt",
            "Khadijah": "CPS_attendance.txt",
            "Mehmood": "Islamiyat_attendance.txt",
            "ArifButt": "DLD_attendance.txt",
            "FaisalBukhari": "Probability_attendance.txt",
        }
        if self.teacher_name in teacher_users:
            file_path = teacher_users[self.teacher_name]
            try:
                att_window = tk.Toplevel(self.window)  
                att_window.title("View Attendance Sheet")
                att_window.geometry('400x300')

                with open(file_path, 'r') as file:
                    att_text = file.read()
                    att_text_widget = tk.Text(att_window, wrap='word', height=100, width=150)
                    att_text_widget.insert(tk.END, att_text)
                    att_text_widget.pack(pady=10)
            except FileNotFoundError:
                att_label = tk.Label(att_window, text=f"No attendance found for {self.teacher_name}")
                att_label.pack(pady=10)
        else:
            att_window = tk.Toplevel(self.window)  
            att_label = tk.Label(att_window, text="You do not have access to view attendance.")
            att_label.pack(pady=10)

        
    def view_marks(self):
        marks_window = tk.Toplevel(self.window)
        marks_window.title("View Marks Sheet")
        marks_window.geometry('400x300')

        file_mapping = {
            "FaisalBukhari": "Probability.txt",
            "Tahir": "Quran.txt",
            "Idrees": "Python.txt",
            "Khadijah": "CPS.txt",  
            "Mehmood": "Islamiyat.txt",
            "ArifButt": "DLD.txt",
        }

        if self.teacher_name in file_mapping:
            file_path = file_mapping[self.teacher_name]
            try:
                with open(file_path, 'r') as file:
                    marks_text = file.read()
                    marks_text_widget = tk.Text(marks_window, wrap='word', height=100, width=150)
                    marks_text_widget.insert(tk.END, marks_text)
                    marks_text_widget.pack(pady=10)
            except FileNotFoundError:
                marks_label = tk.Label(marks_window, text=f"No marks found for {self.teacher_name}")
                marks_label.pack(pady=10)
        else:
            marks_label = tk.Label(marks_window, text="You do not have access to view marks.")
            marks_label.pack(pady=10)
            
    def edit_marksheet(self):
        result_window = tk.Toplevel(self.window)
        result_window.title("Edit MarkSheet")
        result_window.geometry('400x300')
        file_mapping = {
            "FaisalBukhari": "Probability.txt",
            "Tahir": "Quran.txt",
            "Idrees": "Python.txt",
            "Khadijah": "CPS.txt",
            "Mehmood": "Islamiyat.txt",
            "ArifButt": "DLD.txt",
            }
        if self.teacher_name in file_mapping:
            file_path = file_mapping[self.teacher_name]

            with open(file_path, 'r') as file:
                read = file.readlines()
                rollno_to_find = simpledialog.askstring("Enter RollNo", "Please enter the RollNo:")
            index_to_update = None
            for i, line in enumerate(read):
                roll_no = line[0:13].strip()
                if roll_no == rollno_to_find:
                    index_to_update = i
                    break

            if index_to_update is not None:
                course_titles = ["Python", "DLD", "CPS", "Quran", "Islamiyat", "Probability"]
                course_title_combobox = ttk.Combobox(result_window, values=course_titles)
                course_title_combobox.set(course_titles[0])
                course_title_combobox_label = ttk.Label(result_window, text="Select Course Title:")
                course_title_combobox_label.pack(pady=5)
                course_title_combobox.pack(pady=5)

            
                mid_marks_combobox = ttk.Combobox(result_window, values=[str(i) for i in range(36)])
                mid_marks_combobox.set("0")
                mid_marks_combobox_label = ttk.Label(result_window, text="Select Mid Marks:")
                mid_marks_combobox_label.pack(pady=5)
                mid_marks_combobox.pack(pady=5)

            
                sessional_marks_combobox = ttk.Combobox(result_window, values=[str(i) for i in range(26)])
                sessional_marks_combobox.set("0")
                sessional_marks_combobox_label = ttk.Label(result_window, text="Select Sessional Marks:")
                sessional_marks_combobox_label.pack(pady=5)
                sessional_marks_combobox.pack(pady=5)

            
                final_marks_combobox = ttk.Combobox(result_window, values=[str(i) for i in range(40)])
                final_marks_combobox.set("0")
                final_marks_combobox_label = ttk.Label(result_window, text="Select Final Marks:")
                final_marks_combobox_label.pack(pady=5)
                final_marks_combobox.pack(pady=5)

            
                credit_hr_combobox = ttk.Combobox(result_window, values=[str(i) for i in range(1, 5)])
                credit_hr_combobox.set("1")
                credit_hr_combobox_label = ttk.Label(result_window, text="Select Credit Hour:")
                credit_hr_combobox_label.pack(pady=5)
                credit_hr_combobox.pack(pady=5)

                name_entry = ttk.Entry(result_window)
                name_label = ttk.Label(result_window, text="Enter Student Name:")
                name_label.pack(pady=5)
                name_entry.pack(pady=5)
               
                def update_marksheet():
                    fields = read[index_to_update].split()
                    fields[0] = rollno_to_find.ljust(15)
                    fields[1] = course_title_combobox.get().ljust(15)
                    fields[2] = mid_marks_combobox.get().ljust(11)
                    fields[3] = sessional_marks_combobox.get().ljust(18)
                    fields[4] = final_marks_combobox.get().ljust(12)
                    fields[5] = credit_hr_combobox.get().ljust(13)
                    fields[6] = name_entry.get().ljust(15)
                    updated_line = f"{fields[0]} {fields[1]} {fields[2]:>2} {fields[3]:>2} {fields[4]:>2} {fields[5]:>2} {fields[6]}\n"
                    read[index_to_update] = updated_line
                    with open(file_path, 'w') as file:
                        file.writelines(read)
                        
                    messagebox.showinfo("Success", f'Marksheet for RollNo {rollno_to_find} in {file_path} updated successfully.')
                update_button = ttk.Button(result_window, text="Update MarkSheet", command=update_marksheet)
                update_button.pack(pady=10)
           
            else:
                messagebox.showerror("Error", f'RollNo {rollno_to_find} not found in {file_path}.')
        else:
            messagebox.showerror("Error", f'Teacher {self.teacher_name} not found in the mapping.')



def authenticate_user(username, password, user_type):
    if user_type == "Student":
        users = student_users
    elif user_type == "Teacher":
        users = teacher_users
    else:
        return False

    if username in users and users[username] == password:
        return True
    else:
        return False
    
def open_teacher_options():
    teacher_options_window = TeacherOptionsWindow(root, username_entry.get())
def open_student_options():
    student_options_window = StudentOptionsWindow(root, username_entry.get())

def login(username_entry, password_entry, user_type):
    username = username_entry.get()
    password = password_entry.get()

    if authenticate_user(username, password, user_type):
        message_var.set(f"Login successful as {user_type}: {username}")
        if user_type == "Student":
            open_student_options()
        elif user_type == "Teacher":
            open_teacher_options()
    else:
        message_var.set("Login failed. Please check your credentials.")

student_users = {
    "BSDSF22A001": "pucit123",
    "BSDSF22A002": "pucit123",
    "BSDSF22A003": "pucit123",
    "BSDSF22A004": "pucit123",
    "BSDSF22A005": "pucit123",
    "BSDSF22A006": "pucit123",
    "BSDSF22A007": "pucit123",
    "BSDSF22A008": "pucit123",
    "BSDSF22A009": "pucit123",
    "BSDSF22A010": "pucit123",
    "BSDSF22A011": "pucit123",
    "BSDSF22A012": "pucit123",
    "BSDSF22A013": "pucit123",
    "BSDSF22A014": "pucit123",
    "BSDSF22A015": "pucit123",
    "BSDSF22A016": "pucit123",
    "BSDSF22A017": "pucit123",
    "BSDSF22A018": "pucit123",
    "BSDSF22A019": "pucit123",
    "BSDSF22A020": "pucit123",
    "BSDSF22A021": "pucit123",
    "BSDSF22A022": "pucit123",
    "BSDSF22A023": "pucit123",
    "BSDSF22A024": "pucit123",
    "BSDSF22A025": "pucit123",
    "BSDSF22A026": "pucit123",
    "BSDSF22A027": "pucit123",
    "BSDSF22A028": "pucit123",
    "BSDSF22A029": "pucit123",
    "BSDSF22A030": "pucit123",
    "BSDSF22A031": "pucit123",
    "BSDSF22A032": "pucit123",
    "BSDSF22A033": "pucit123",
    "BSDSF22A034": "pucit123",
    "BSDSF22A035": "pucit123",
    "BSDSF22A036": "pucit123",
    "BSDSF22A037": "pucit123",
    "BSDSF22A038": "pucit123",
    "BSDSF22A039": "pucit123",
    "BSDSF22A040": "pucit123",
    "BSDSF22A041": "pucit123",
    "BSDSF22A042": "pucit123",
}

teacher_users = {
    "Idrees": "pucit123",
    "Tahir": "pucit123",
    "Khadijah": "pucit123",
    "Mehmood": "pucit123",
    "ArifButt": "pucit123",
    "FaisalBukhari": "pucit123",
}

root = tk.Tk()
root.title("CMS LOGIN")
root.geometry('800x700')
image = Image.open('PU.jpg') 
photo = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=0.5, relheight=1)
frame = ttk.Frame(root)
frame.place(relx=0.8, rely=0.8, anchor='center', relwidth=0.5, relheight=1)

ttk.Label(frame, text="Username:").grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(frame, justify="center")  
username_entry.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(frame, text="Password:").grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(frame, show="*", justify="center")  
password_entry.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(frame, text="User Type:").grid(row=2, column=0, padx=10, pady=5)
user_type_combobox = ttk.Combobox(frame, values=["Student", "Teacher"], justify="center")
user_type_combobox.grid(row=2, column=1, padx=10, pady=5)
user_type_combobox.set("Student")

login_button = ttk.Button(frame, text="Login", command=lambda: login(username_entry, password_entry, user_type_combobox.get()))
login_button.grid(row=3, column=0, columnspan=2, pady=10)

message_var = tk.StringVar()
message_label = ttk.Label(frame, textvariable=message_var, foreground="red", justify="center")
message_label.grid(row=4, column=0, columnspan=2, pady=5)


root.mainloop()
