# --- Hướng dẫn cơ bản về Module trong Python ---

# Một module trong Python là một file chứa mã Python (bao gồm hàm, lớp, biến, v.v.).
# Mục đích chính của module là tổ chức mã, giúp tái sử dụng mã và làm cho chương trình dễ quản lý hơn.
# Module có thể được import vào file khác để sử dụng các chức năng đã định nghĩa trong module.

# ===================== 1. Tạo một Module =====================

# a) Để tạo một module, bạn chỉ cần tạo một file Python mới.
# Ví dụ: tạo một file `mymodule.py` với nội dung sau:
# ----------------------------------------------------------
# # Đây là file mymodule.py
# def greet(name):
#     """Hàm chào hỏi."""
#     return f"Hello, {name}!"
# 
# PI = 3.14159  # Một hằng số trong module
# ----------------------------------------------------------
# File này là một module với một hàm `greet` và một biến `PI`.

# ===================== 2. Import một Module =====================

# Có nhiều cách để import một module vào chương trình Python.

# a) Import toàn bộ module
# Cách này sẽ import tất cả các hàm và biến trong module.
import mymodule
print(mymodule.greet("Alice"))  # Gọi hàm greet từ module
print("Giá trị của PI:", mymodule.PI)  # Truy cập biến PI từ module

# b) Import một hàm hoặc biến cụ thể từ module
# Cách này chỉ import những phần tử được chỉ định.
from mymodule import greet, PI
print(greet("Bob"))  # Gọi hàm greet từ module (không cần viết mymodule.greet)
print("Giá trị của PI:", PI)

# c) Đặt tên khác cho module khi import (dùng alias)
# Đặt tên khác cho module giúp viết code ngắn gọn hơn.
import mymodule as mod
print(mod.greet("Charlie"))
print("Giá trị của PI:", mod.PI)

# ===================== 3. Tạo và Sử dụng Package =====================

# Một package là một tập hợp các module có tổ chức trong một thư mục. 
# Một thư mục chứa các module có thể trở thành một package nếu có file `__init__.py` (có thể rỗng) bên trong.
# Ví dụ:
# project_folder/
# ├── mypackage/
# │   ├── __init__.py    # Đánh dấu thư mục này là một package
# │   ├── module1.py     # Một module bên trong package
# │   └── module2.py     # Một module khác trong package
# └── main.py            # File chính

# Giả sử nội dung của `module1.py` như sau:
# ----------------------------------------------------------
# # Đây là file module1.py trong package mypackage
# def add(x, y):
#     return x + y
# ----------------------------------------------------------

# Để import và sử dụng các module trong package:
# from mypackage import module1
# print(module1.add(3, 5))  # Gọi hàm add từ module1 trong package mypackage

# ===================== 4. Các Kiểu Import trong Package =====================

# a) Import module cụ thể từ package
# Chỉ import module1 từ mypackage
from mypackage import module1
print(module1.add(5, 7))

# b) Import toàn bộ package (nhưng phải chỉ định cụ thể khi gọi các phần tử bên trong)
# import mypackage
# print(mypackage.module1.add(10, 15))

# ===================== 5. Biến __name__ và Điều kiện __main__ =====================

# Trong một file Python, biến đặc biệt __name__ sẽ có giá trị là "__main__" khi file đó được chạy trực tiếp.
# Nếu file được import như một module, __name__ sẽ là tên của module.

# Ví dụ trong file `mymodule.py`:
# ----------------------------------------------------------
# if __name__ == "__main__":
#     # Phần này sẽ chỉ chạy khi mymodule.py được chạy trực tiếp, không chạy khi được import.
#     print("Module mymodule đang được chạy trực tiếp")
# ----------------------------------------------------------

# Điều này hữu ích để kiểm tra hoặc viết mã kiểm thử chỉ chạy khi file được chạy trực tiếp.

# ===================== 6. Module Tích hợp sẵn và Module Bên ngoài =====================

# Python có rất nhiều module tích hợp sẵn như `math`, `datetime`, `random`.
# a) Sử dụng module tích hợp sẵn
import math
print("Giá trị của π:", math.pi)  # Truy cập hằng số pi trong module math
print("Căn bậc hai của 16:", math.sqrt(16))  # Gọi hàm căn bậc hai

# b) Sử dụng module bên ngoài
# Để sử dụng module bên ngoài, cần cài đặt chúng trước bằng lệnh `pip install <module_name>`.
# Ví dụ: cài đặt và sử dụng thư viện NumPy
# import numpy as np
# arr = np.array([1, 2, 3])
# print("Mảng NumPy:", arr)

# ===================== 7. Các Quy tắc Tổ chức Module =====================

# - Đặt tên module ngắn gọn, dễ hiểu và nên sử dụng chữ thường, ví dụ `utils.py`.
# - Các biến toàn cục, hàm và lớp trong module nên có tên rõ ràng và tuân theo quy tắc đặt tên.
# - Tránh xung đột tên bằng cách sử dụng `import as` để đặt tên biệt danh cho module khi cần.
# - Sử dụng comment và docstring để giải thích các hàm, lớp trong module giúp người khác dễ hiểu hơn.

# --- Kết thúc hướng dẫn cơ bản về Module trong Python ---
# Các hướng dẫn trên giúp bạn hiểu rõ về cách tạo và sử dụng module, package, cũng như các cách import.
# Module là công cụ mạnh mẽ trong Python để quản lý mã và chia sẻ chức năng.

import math, random # import 2 modules
print(math.factorial(5))
print(random.randint(10, 20))
def main():
    'Thực thi các logic của chương trình'
# code cần chạy
if __name__ == '__main__':
    main()
import sys
print(sys.path)
import math
print(dir(math))
__all__ = [
    '<module_name>'
]
__all__ = ["echo", "surround", "reverse"]

# import <package_name>.<module_name> [as <alias_name>]
