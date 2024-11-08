# --- Hướng dẫn cơ bản về Lập trình Hướng đối tượng (OOP) trong Python ---

# OOP là một phương pháp lập trình dựa trên các "đối tượng", được định nghĩa thông qua các lớp (class).
# Mục tiêu của OOP là mô phỏng các đối tượng trong thế giới thực và cách chúng tương tác với nhau.

# ===================== 1. Class và Object (Lớp và Đối tượng) =====================

# a) Tạo một Class (Lớp)
# Lớp là một bản thiết kế (blueprint) cho các đối tượng. Nó định nghĩa các thuộc tính (attributes) và phương thức (methods) mà đối tượng sẽ có.

class Person:
    # Hàm khởi tạo (__init__) được gọi khi một đối tượng mới của lớp được tạo.
    def __init__(self, name, age):
        self.name = name   # self.name là thuộc tính của đối tượng
        self.age = age     # self.age là thuộc tính của đối tượng

    # Phương thức của lớp
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# b) Tạo một Object (Đối tượng)
# Đối tượng là một thể hiện cụ thể của lớp. Mỗi đối tượng có dữ liệu và hành vi riêng dựa trên lớp mà nó được tạo ra.
person1 = Person("Alice", 25)
print(person1.greet())    # Gọi phương thức greet của đối tượng person1

# ===================== 2. Encapsulation (Đóng gói) =====================

# Đóng gói là việc giới hạn quyền truy cập vào các thuộc tính và phương thức của một đối tượng.
# Trong Python, các thuộc tính hoặc phương thức bắt đầu bằng dấu gạch dưới (_) hoặc (__)
# thường được coi là "private" và không nên truy cập trực tiếp từ bên ngoài.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # __balance là thuộc tính private

    # Phương thức nạp tiền vào tài khoản
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    # Phương thức rút tiền
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Số dư không đủ")

    # Phương thức xem số dư
    def get_balance(self):
        return self.__balance

# Tạo đối tượng BankAccount
account = BankAccount("Bob", 1000)
account.deposit(500)
account.withdraw(300)
print("Số dư tài khoản:", account.get_balance())

# ===================== 3. Inheritance (Kế thừa) =====================

# Kế thừa cho phép một lớp con kế thừa thuộc tính và phương thức của lớp cha.
# Kế thừa giúp tái sử dụng mã và mở rộng chức năng của lớp cha.

class Employee(Person):    # Employee kế thừa từ Person
    def __init__(self, name, age, salary):
        super().__init__(name, age)  # Gọi hàm khởi tạo của lớp cha (Person)
        self.salary = salary         # Thêm thuộc tính mới cho lớp con

    # Phương thức riêng của Employee
    def get_salary(self):
        return f"{self.name} earns {self.salary} per year."

# Tạo đối tượng Employee
employee1 = Employee("David", 30, 50000)
print(employee1.greet())           # Sử dụng phương thức từ lớp cha (Person)
print(employee1.get_salary())       # Sử dụng phương thức của lớp con (Employee)

# ===================== 4. Polymorphism (Đa hình) =====================

# Đa hình là khả năng sử dụng một giao diện duy nhất để làm việc với các lớp khác nhau.
# Ví dụ: cùng một phương thức với tên gọi giống nhau có thể có các cách hoạt động khác nhau khi sử dụng với các lớp khác nhau.

class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

# Hàm sử dụng đa hình
def make_sound(animal):
    print(animal.sound())

# Sử dụng hàm make_sound với các đối tượng khác nhau
dog = Dog()
cat = Cat()
make_sound(dog)   # Kết quả: Woof!
make_sound(cat)   # Kết quả: Meow!

# ===================== 5. Abstraction (Trừu tượng) =====================

# Trừu tượng là việc ẩn đi các chi tiết không cần thiết và chỉ hiển thị các tính năng chính.
# Trong Python, có thể tạo các lớp trừu tượng bằng module abc (abstract base class).

from abc import ABC, abstractmethod

class Shape(ABC):  # Shape là một lớp trừu tượng
    @abstractmethod
    def area(self):
        pass  # Hàm trừu tượng, lớp con phải triển khai

    @abstractmethod
    def perimeter(self):
        pass  # Hàm trừu tượng, lớp con phải triển khai

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Tạo đối tượng Rectangle và tính diện tích, chu vi
rect = Rectangle(4, 5)
print("Diện tích hình chữ nhật:", rect.area())
print("Chu vi hình chữ nhật:", rect.perimeter())

# ===================== 6. Các thuộc tính và phương thức đặc biệt =====================

# Python cung cấp một số thuộc tính và phương thức đặc biệt bắt đầu và kết thúc bằng dấu gạch dưới kép __
# Những thuộc tính/phương thức này được gọi là "magic methods" hoặc "dunder methods".

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # __str__ để mô tả đối tượng dưới dạng chuỗi khi sử dụng hàm print()
    def __str__(self):
        return f"{self.title} by {self.author}"

    # __len__ để trả về độ dài của đối tượng
    def __len__(self):
        return len(self.title)

book = Book("Python Programming", "John Doe")
print(book)               # Kết quả: Python Programming by John Doe
print("Độ dài của tiêu đề sách:", len(book))  # Kết quả: 18 (số ký tự trong tiêu đề)

# --- Kết thúc hướng dẫn cơ bản về Lập trình Hướng đối tượng trong Python ---
# Các nội dung trên giới thiệu cách tạo và sử dụng các thành phần chính của OOP: class, object, encapsulation, inheritance,
# polymorphism, abstraction và magic methods. Lập trình hướng đối tượng là một công cụ mạnh mẽ để xây dựng và tổ chức mã trong Python.
