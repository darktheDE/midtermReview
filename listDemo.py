lst = [0,1,2,3,4,5,67,3,2,1,2,4,5,6,8,8,9,98,6,5,3,2,3,3,4,4,5,6,67,7,88,9]
lst.insert(3, 22) # insert(index, value)
lst.append(24) # add last, value
new_lst = [ x  for x in lst if x%2 == 0] # list comprehension
lst.extend(new_lst) # add new_lst into lst
lst.remove(0) #remove(value) first met element
lst.pop(4) #remove, show value of index. 
lst.pop() #remove, show value of last ele
del lst[0] # remove element with index
lst.clear() # remove everything and return a empty list
lst.sort() # sort right onto list
lst1 = sorted(lst) # sort the sent list, return new list.
lst2 = lst1.copy()
lst2 = list(lst1) # this all "copy" mean create new memory field, the "=" op is only reference.
lst2 = lst1# this mean lst2 point to lst1 address, every change on lst2 will change lst1 as well
# 2-dim list is a list 1-dim list with each ele is a 1-dim list
print(lst)
del lst  #delete whole obj

# --- Hướng dẫn cơ bản về các kiểu dữ liệu Collection trong Python ---

# Python có các kiểu dữ liệu chính thường dùng để lưu trữ nhiều phần tử: List, Tuple, Set, Dictionary và String.
# Các kiểu dữ liệu này có đặc điểm riêng và phù hợp với các mục đích khác nhau.

# ===================== 1. List (Danh sách) =====================

# List là một cấu trúc dữ liệu có thứ tự, có thể thay đổi (mutable) và có thể chứa các phần tử trùng lặp.

# a) Tạo một list
my_list = [1, 2, 3, 4, 5]  # List chứa các số nguyên
print("List:", my_list)

# b) Thao tác với list
my_list.append(6)           # Thêm một phần tử vào cuối list
my_list.insert(2, 'a')      # Thêm phần tử 'a' vào vị trí thứ 2
print("List sau khi thêm:", my_list)

# c) Truy cập và thay đổi phần tử
print("Phần tử đầu tiên:", my_list[0])  # Truy cập phần tử đầu tiên
my_list[1] = 20                         # Thay đổi phần tử ở vị trí thứ 1
print("List sau khi thay đổi:", my_list)

# d) Xóa phần tử
my_list.remove('a')        # Xóa phần tử 'a' đầu tiên tìm thấy
popped = my_list.pop()     # Xóa và trả về phần tử cuối cùng
print("List sau khi xóa:", my_list)
print("Phần tử đã xóa:", popped)

# ===================== 2. Tuple (Bộ dữ liệu) =====================

# Tuple là một cấu trúc dữ liệu có thứ tự và không thể thay đổi (immutable).

# a) Tạo một tuple
my_tuple = (1, 2, 3, 4)
print("Tuple:", my_tuple)

# b) Truy cập phần tử
print("Phần tử đầu tiên của tuple:", my_tuple[0])

# c) Sử dụng tuple trong unpacking (giải nén)
a, b, c, d = my_tuple
print("Các giá trị sau unpacking:", a, b, c, d)

# ===================== 3. Set (Tập hợp) =====================

# Set là một cấu trúc dữ liệu không có thứ tự, không chứa các phần tử trùng lặp và có thể thay đổi.

# a) Tạo một set
my_set = {1, 2, 3, 4}
print("Set:", my_set)

# b) Thao tác với set
my_set.add(5)             # Thêm phần tử vào set
my_set.update([6, 7])     # Thêm nhiều phần tử vào set
print("Set sau khi thêm:", my_set)

# c) Xóa phần tử
my_set.remove(1)          # Xóa phần tử 1 khỏi set
my_set.discard(10)        # Xóa phần tử 10 nếu có, nếu không có thì bỏ qua
print("Set sau khi xóa:", my_set)

# d) Phép toán trên set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Hợp của set1 và set2:", set1 | set2)     # Phép hợp
print("Giao của set1 và set2:", set1 & set2)    # Phép giao
print("Hiệu của set1 và set2:", set1 - set2)    # Phép hiệu

# ===================== 4. Dictionary (Từ điển) =====================

# Dictionary là một cấu trúc dữ liệu không có thứ tự và có thể thay đổi, lưu trữ các cặp khóa-giá trị (key-value).

# a) Tạo một dictionary
my_dict = {"name": "Alice", "age": 25}
print("Dictionary:", my_dict)

# b) Truy cập giá trị
print("Tên:", my_dict["name"])  # Truy cập giá trị với khóa 'name'

# c) Thêm và thay đổi giá trị
my_dict["location"] = "New York"  # Thêm cặp khóa-giá trị mới
my_dict["age"] = 26               # Thay đổi giá trị của khóa 'age'
print("Dictionary sau khi thêm/thay đổi:", my_dict)

# d) Xóa phần tử
del my_dict["location"]           # Xóa phần tử với khóa 'location'
print("Dictionary sau khi xóa:", my_dict)

# e) Lặp qua các phần tử
for key, value in my_dict.items():
    print(f"Khóa: {key}, Giá trị: {value}")

# ===================== 5. String (Chuỗi) =====================

# String là một chuỗi ký tự trong Python, không thể thay đổi (immutable) nhưng có thể xử lý rất linh hoạt.

# a) Tạo một string
my_string = "Hello, Python!"
print("Chuỗi:", my_string)

# b) Truy cập ký tự
print("Ký tự đầu tiên:", my_string[0])

# c) Cắt chuỗi (slicing)
print("Phần tử từ 0 đến 5:", my_string[0:5])

# d) Các hàm thường dùng với chuỗi
print("In hoa:", my_string.upper())           # In hoa
print("In thường:", my_string.lower())        # In thường
print("Tách từ:", my_string.split())          # Tách chuỗi thành list các từ

# e) Ghép chuỗi
greeting = "Xin chào"
name = "Python"
full_greeting = greeting + ", " + name + "!"
print("Chuỗi ghép:", full_greeting)

# ===================== 6. Các thao tác chung trên Collection =====================

# Các thao tác như lặp (loop), tìm độ dài, kiểm tra phần tử tồn tại có thể dùng với mọi loại collection.

# a) Tìm độ dài của các collection
print("Độ dài của list:", len(my_list))
print("Độ dài của tuple:", len(my_tuple))
print("Độ dài của set:", len(my_set))
print("Độ dài của dict:", len(my_dict))
print("Độ dài của string:", len(my_string))

# b) Kiểm tra phần tử tồn tại
print("3 có trong list?", 3 in my_list)
print("5 có trong set?", 5 in my_set)
print("'name' có trong dict?", 'name' in my_dict)
print("'Python' có trong string?", "Python" in my_string)

# --- Kết thúc hướng dẫn cơ bản về các kiểu dữ liệu Collection ---
# Nội dung trên bao gồm các thao tác cơ bản với list, tuple, set, dictionary và string, giúp bạn làm quen với việc lưu trữ và xử lý dữ liệu trong Python.
