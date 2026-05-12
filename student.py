class Student:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id} | Tên: {self.name} | Ngành: {self.major}"
def search_student():
    """Chức năng tìm kiếm dữ liệu [cite: 33]"""
    search_id = input("Nhập mã sinh viên cần tìm: ")
    found = False
    for sv in students_list:
        if sv.student_id == search_id:
            print("Kết quả tìm kiếm:", sv)
            found = True
            break
    if not found:
        print("Không tìm thấy sinh viên có mã này.")
fafa
