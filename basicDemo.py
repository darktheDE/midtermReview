# ===================== Khái niệm cơ bản về Python =====================

# Python là ngôn ngữ lập trình bậc cao, dễ học và có cú pháp đơn giản.
# Python hỗ trợ các kiểu dữ liệu cơ bản như:
# - int (số nguyên), float (số thực), bool (giá trị logic True/False), str (chuỗi ký tự)
# - list (danh sách), tuple (bộ dữ liệu), set (tập hợp), dict (từ điển)

# Ví dụ các kiểu dữ liệu cơ bản
so_nguyen = 10       # Kiểu int
so_thuc = 3.14       # Kiểu float
chuoi = "Hello"      # Kiểu str
logic = True         # Kiểu bool

# ===================== Rẽ nhánh (Cấu trúc điều kiện) =====================

# Cấu trúc điều kiện trong Python được sử dụng với các câu lệnh `if`, `elif` và `else`.
# Cú pháp:
# if <điều kiện>:
#     <khối lệnh thực thi nếu điều kiện đúng>
# elif <điều kiện khác>:
#     <khối lệnh thực thi nếu điều kiện khác đúng>
# else:
#     <khối lệnh thực thi nếu không có điều kiện nào đúng>

# Ví dụ:
x = 5
if x > 0:
    print("x là số dương")
elif x == 0:
    print("x là số không")
else:
    print("x là số âm")

# ===================== Vòng lặp =====================

# Python cung cấp hai loại vòng lặp chính là `for` và `while`.

# 1. Vòng lặp for: Duyệt qua các phần tử trong một chuỗi, danh sách, hoặc bất kỳ đối tượng lặp nào.
# Cú pháp:
# for <biến> in <đối tượng lặp>:
#     <khối lệnh thực thi cho mỗi phần tử>

# Ví dụ:
for i in range(5):  # Duyệt từ 0 đến 4
    print("i =", i)

# 2. Vòng lặp while: Lặp lại một khối lệnh khi điều kiện còn đúng.
# Cú pháp:
# while <điều kiện>:
#     <khối lệnh thực thi nếu điều kiện đúng>

# Ví dụ:
count = 0
while count < 5:
    print("count =", count)
    count += 1  # Tăng giá trị biến đếm

# ===================== Hàm (Function) =====================

# Hàm là khối lệnh có thể tái sử dụng để thực hiện một nhiệm vụ cụ thể.
# Hàm có thể nhận các đối số (parameters) và trả về giá trị (return).
# Cú pháp:
# def <tên hàm>(<các tham số>):
#     <khối lệnh trong hàm>
#     return <giá trị trả về>

# Ví dụ:
def tinh_tong(a, b):
    """Hàm tính tổng hai số"""
    tong = a + b
    return tong

# Gọi hàm
result = tinh_tong(3, 5)
print("Tổng là:", result)

# ===================== Xử lý ngoại lệ (Exception Handling) =====================

# Python có cơ chế xử lý lỗi (ngoại lệ) với các khối lệnh `try`, `except`, `else`, và `finally`.
# `try`: Thực thi một khối lệnh có thể gây ra lỗi.
# `except`: Xử lý lỗi nếu có.
# `else`: Thực thi nếu không có lỗi xảy ra.
# `finally`: Thực thi bất kể có lỗi hay không.

# Cú pháp:
# try:
#     <khối lệnh có thể gây ra lỗi>
# except <loại lỗi>:
#     <khối lệnh xử lý lỗi>
# else:
#     <khối lệnh thực thi nếu không có lỗi>
# finally:
#     <khối lệnh luôn được thực thi>

# Ví dụ:
try:
    a = int(input("Nhập số nguyên: "))
    b = int(input("Nhập số nguyên khác 0: "))
    ket_qua = a / b
except ValueError:
    print("Lỗi: Giá trị nhập không phải là số nguyên!")
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
else:
    print("Kết quả phép chia:", ket_qua)
finally:
    print("Kết thúc chương trình.")

# ===================== Kết thúc hướng dẫn cơ bản về Python =====================

# Các khái niệm trên cung cấp nền tảng cơ bản để làm việc với Python.
# Các ví dụ bao gồm cách sử dụng biến, cấu trúc điều kiện, vòng lặp, hàm và xử lý ngoại lệ.
