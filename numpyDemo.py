# --- Hướng dẫn cơ bản về NumPy trong Python ---

# NumPy là một thư viện mạnh mẽ cho tính toán khoa học trong Python, đặc biệt hữu ích khi làm việc với mảng và ma trận.
# Để sử dụng NumPy, bạn cần import thư viện:
import numpy as np

# ===================== 1. Tạo mảng NumPy =====================

# a) Tạo mảng từ danh sách
arr_1d = np.array([1, 2, 3, 4, 5])  # Mảng 1 chiều
print("Mảng 1 chiều:", arr_1d)

# b) Tạo mảng 2 chiều
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])  # Mảng 2x3
print("Mảng 2 chiều:\n", arr_2d)

# c) Tạo mảng với các giá trị từ 0 đến 9
arr_range = np.arange(10)
print("Mảng từ 0 đến 9:", arr_range)

# d) Tạo mảng với các giá trị từ 0 đến 9, bước nhảy là 2
arr_step = np.arange(0, 10, 2)
print("Mảng với bước nhảy 2:", arr_step)

# ===================== 2. Các hàm tạo mảng phổ biến =====================

# a) Tạo mảng gồm các số 0
arr_zeros = np.zeros((3, 3))
print("Mảng gồm các số 0:\n", arr_zeros)

# b) Tạo mảng gồm các số 1
arr_ones = np.ones((2, 4))
print("Mảng gồm các số 1:\n", arr_ones)

# c) Tạo mảng đơn vị (ma trận vuông với đường chéo là 1)
arr_eye = np.eye(3)
print("Mảng đơn vị:\n", arr_eye)

# d) Tạo mảng số ngẫu nhiên
arr_random = np.random.rand(2, 3)
print("Mảng số ngẫu nhiên:\n", arr_random)

# ===================== 3. Thao tác cơ bản với mảng =====================

# a) Truy cập phần tử của mảng
print("Phần tử đầu tiên của arr_1d:", arr_1d[0])  # Truy cập phần tử đầu tiên của mảng 1 chiều
print("Phần tử ở hàng 1, cột 2 của arr_2d:", arr_2d[0, 1])  # Truy cập phần tử hàng 1, cột 2 trong mảng 2 chiều

# b) Cắt mảng (slicing)
print("Các phần tử từ 1 đến 3 trong arr_1d:", arr_1d[1:4])  # Lấy phần tử từ vị trí 1 đến 3
print("Dòng đầu tiên của arr_2d:", arr_2d[0, :])  # Lấy dòng đầu tiên của mảng 2 chiều

# c) Thay đổi kích thước của mảng
arr_reshape = np.arange(12).reshape(3, 4)
print("Mảng 3x4 được tạo từ mảng 1 chiều:\n", arr_reshape)

# ===================== 4. Tính toán trên mảng =====================

# a) Các phép toán cơ bản
arr_add = arr_1d + 2  # Cộng 2 vào mỗi phần tử của mảng
print("Cộng 2 vào mỗi phần tử:", arr_add)

arr_mul = arr_1d * 3  # Nhân mỗi phần tử với 3
print("Nhân mỗi phần tử với 3:", arr_mul)

# b) Phép toán giữa các mảng
arr_sum = arr_1d + np.array([5, 4, 3, 2, 1])
print("Phép cộng giữa hai mảng:", arr_sum)

# c) Các hàm tính toán phổ biến
print("Tổng các phần tử của arr_1d:", np.sum(arr_1d))  # Tính tổng các phần tử
print("Giá trị lớn nhất trong arr_1d:", np.max(arr_1d))  # Tìm giá trị lớn nhất
print("Giá trị nhỏ nhất trong arr_1d:", np.min(arr_1d))  # Tìm giá trị nhỏ nhất
print("Trung bình của arr_1d:", np.mean(arr_1d))  # Tính giá trị trung bình

# ===================== 5. Các hàm thao tác mảng khác =====================

# a) Ghép mảng theo trục dọc và ngang
arr_a = np.array([[1, 2], [3, 4]])
arr_b = np.array([[5, 6], [7, 8]])
arr_vstack = np.vstack((arr_a, arr_b))  # Ghép theo trục dọc
arr_hstack = np.hstack((arr_a, arr_b))  # Ghép theo trục ngang
print("Ghép theo trục dọc:\n", arr_vstack)
print("Ghép theo trục ngang:\n", arr_hstack)

# b) Transpose (chuyển vị) mảng
arr_transpose = arr_2d.T
print("Chuyển vị của arr_2d:\n", arr_transpose)

# c) Tìm chỉ số của các phần tử dựa trên điều kiện
indices = np.where(arr_1d > 3)  # Tìm các phần tử lớn hơn 3
print("Chỉ số các phần tử lớn hơn 3:", indices)
print("Các phần tử lớn hơn 3:", arr_1d[indices])

# d) Lọc các giá trị duy nhất trong mảng
arr_unique = np.unique(arr_1d)
print("Các giá trị duy nhất trong arr_1d:", arr_unique)

# ===================== 6. Sao chép mảng =====================

# Sao chép mảng
arr_copy = arr_1d.copy()
arr_copy[0] = 10
print("Mảng gốc:", arr_1d)
print("Mảng sao chép sau khi thay đổi:", arr_copy)

# ===================== 7. Xử lý mảng thiếu =====================

# NumPy hỗ trợ giá trị NaN (Not a Number) cho các phần tử bị thiếu
arr_nan = np.array([1, 2, np.nan, 4])
print("Mảng với giá trị NaN:", arr_nan)

# Tính toán bỏ qua các giá trị NaN
print("Trung bình (bỏ qua NaN):", np.nanmean(arr_nan))  # Tính trung bình bỏ qua NaN
print("Tổng (bỏ qua NaN):", np.nansum(arr_nan))  # Tính tổng bỏ qua NaN

# --- Kết thúc hướng dẫn cơ bản NumPy ---
# Những nội dung trên bao gồm các kiến thức cơ bản để làm việc với NumPy, giúp bạn thao tác và xử lý dữ liệu dạng mảng hiệu quả.
# Bạn có thể sử dụng các ví dụ trên như một tham khảo khi làm việc với mảng và ma trận.

# --- Hướng dẫn sử dụng NumPy để giải các bài tập về mảng và ma trận ---
# Chúng ta sẽ sử dụng thư viện NumPy, một thư viện mạnh mẽ trong Python cho tính toán số học và xử lý ma trận.
# Để bắt đầu, hãy import thư viện NumPy:
import numpy as np

# ===================== BÀI TẬP 1 =====================

# Cho trước mảng B như sau:
B = np.array(np.arange(12))  # Mảng từ 0 đến 11

# a. Phát sinh mảng A gồm 2352 phần tử ngẫu nhiên số nguyên không âm trong đoạn [1, 20]
# Dùng np.random.randint() để tạo mảng số nguyên ngẫu nhiên từ 1 đến 20
A = np.random.randint(1, 21, 2352)

# b. Phát sinh mảng B gồm 2352 phần tử ngẫu nhiên số nguyên không dương trong đoạn [-20, -1]
# Dùng np.random.randint() để tạo mảng số nguyên ngẫu nhiên từ -20 đến -1
B = np.random.randint(-20, 0, 2352)

# c. Xem thông tin các chiều của mảng
# Sử dụng A.shape và B.shape để xem thông tin số chiều và số phần tử trong mỗi chiều của mảng
print("Shape của A:", A.shape)
print("Shape của B:", B.shape)

# d. Tạo ma trận C, D lần lượt từ mảng A, B về ma trận 3 chiều với (28, 28, 3)
# Sử dụng phương thức reshape để biến đổi A, B thành ma trận 3 chiều 28x28x3
C = A.reshape(28, 28, 3)
D = B.reshape(28, 28, 3)

# e. Nối ma trận C, D theo dòng
# Dùng np.concatenate(axis=0) để nối theo dòng (trên-dưới)
CD_vertical = np.concatenate((C, D), axis=0)
print("Shape của ma trận CD_vertical:", CD_vertical.shape)

# f. Đặt 2 ma trận C, D lên nhau
# Có thể hiểu như chồng lên nhau (ghép theo trục 1)
CD_stack = np.stack((C, D), axis=0)
print("Shape của ma trận CD_stack:", CD_stack.shape)

# g. Ghép 2 ma trận C, D theo chiều ngang, dọc
# Dùng np.concatenate(axis=1) để ghép theo chiều ngang (trái-phải)
CD_horizontal = np.concatenate((C, D), axis=1)
print("Shape của ma trận CD_horizontal:", CD_horizontal.shape)

# ===================== BÀI TẬP 2 =====================

# Cho 2 ma trận A và B như sau:
A = np.array([[1, 3, 6], [2, 7, 9]])
B = np.array([[0, 4, 5], [1, 6, 10]])

# a. Tìm phần tử nhỏ nhất trong A
min_A = np.min(A)
print("Phần tử nhỏ nhất trong A:", min_A)

# b. Tìm phần tử nhỏ nhất của A theo từng dòng
min_A_rows = np.min(A, axis=1)
print("Phần tử nhỏ nhất của A theo từng dòng:", min_A_rows)

# c. Tìm phần tử nhỏ nhất của A theo từng cột
min_A_cols = np.min(A, axis=0)
print("Phần tử nhỏ nhất của A theo từng cột:", min_A_cols)

# d. Tìm các phần tử maximum/minimum của A và B ở cùng vị trí indice
max_AB = np.maximum(A, B)  # Phần tử lớn nhất ở từng vị trí của A và B
min_AB = np.minimum(A, B)  # Phần tử nhỏ nhất ở từng vị trí của A và B
print("Phần tử maximum của A và B:", max_AB)
print("Phần tử minimum của A và B:", min_AB)

# e. Tìm ra indice có giá trị lớn nhất của các dòng trong ma trận A
max_indices_rows = np.argmax(A, axis=1)
print("Indice có giá trị lớn nhất của các dòng trong A:", max_indices_rows)

# f. Tìm ra indice của các cột theo thứ tự tăng/giảm dần của ma trận A
sorted_col_indices = np.argsort(A, axis=0)
print("Indice của các cột theo thứ tự tăng dần của A:", sorted_col_indices)

# ===================== BÀI TẬP 3 =====================

# Cho ma trận xác suất với số hàng là số quan sát và số cột là số lớp (classes):
B = np.array([[0.1, 0.2, 0.7],
              [0.6, 0.4, 0.0],
              [0.1, 0.5, 0.4],
              [0.3, 0.3, 0.4],
              [0.1, 0.8, 0.1]])

# Yêu cầu: Thống kê kết quả nhãn thuộc về mỗi loại.
# Sử dụng np.argmax() để tìm chỉ số của lớp có xác suất cao nhất cho mỗi quan sát
labels = np.argmax(B, axis=1)
print("Kết quả nhãn thuộc về mỗi loại cho từng quan sát:", labels)

# Đếm tần số xuất hiện của từng nhãn
unique, counts = np.unique(labels, return_counts=True)
label_counts = dict(zip(unique, counts))
print("Số lượng quan sát thuộc về mỗi loại:", label_counts)
