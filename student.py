class Student:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major

    def __str__(self):
        return f"ID: {self.student_id} | Tên: {self.name} | Ngành: {self.major}"
