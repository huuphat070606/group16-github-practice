import utils

def main_menu():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ SINH VIÊN =====")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách")
        print("3. Tìm kiếm sinh viên")
        print("4. Thoát")
        
        choice = input("Chọn chức năng (1-4): ")
        
        if choice == '1':
            utils.add_student()
        elif choice == '2':
            utils.display_students()
        elif choice == '3':
            utils.search_student()
        elif choice == '4':
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")
