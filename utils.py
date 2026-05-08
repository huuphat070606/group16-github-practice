from student import Student
def add_student():
    """Chức năng thêm dữ liệu [cite: 31]"""
    id_sv = input("Nhập mã sinh viên: ")
    name = input("Nhập tên sinh viên: ")
    major = input("Nhập ngành học: ")
    new_student = Student(id_sv, name, major)
    students_list.append(new_student)
    print("Thêm sinh viên thành công!")

def display_students():
    """Chức năng hiển thị dữ liệu [cite: 32]"""
    if not students_list:
        print("Danh sách trống.")
    else:
        print("\n*-- DANH SÁCH SINH VIÊN --*")
        for sv in students_list:
            print(sv)
students_list = []
