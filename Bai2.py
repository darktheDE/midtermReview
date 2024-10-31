import datetime


class DiaChi:
    def __init__(self, soNha, tenDuong, tenQuan, thanhPho):
        self._soNha = soNha
        self._tenDuong = tenDuong
        self._tenQuan = tenQuan
        self._thanhPho = thanhPho

    def InDiaChi(self):
        print(
            str(self._soNha)
            + " "
            + str(self._tenDuong)
            + " "
            + str(self._tenQuan)
            + " "
            + self._thanhPho
        )


class NhanVien:
    def __init__(self, hoTen, ngaySinh, diaChi):
        self._hoTen = hoTen
        self._ngaySinh = ngaySinh
        self._diaChi = diaChi

    def InThongTin(self):
        print("Họ và tên: ", self._hoTen)
        print(
            "Ngày sinh: "
            + datetime.datetime.strptime(self._ngaySinh, "%Y-%m-%d").strftime(
                "%d-%m-%Y"
            )
        )
        self._diaChi.InDiaChi()
        print("\n")


class NhanVienVanPhong(NhanVien):
    def __init__(self, hoTen, ngaySinh, diaChi, soNgayLamViec):
        super().__init__(hoTen, ngaySinh, diaChi)
        self._soNgayLamViec = soNgayLamViec

    def InThongTin(self):
        super().InThongTin()
        print("Số ngày làm việc: ", self._soNgayLamViec)
        print("Tổng lương: ", self.TinhLuong())
        print("\n")

    def TinhLuong(self):
        return float(self._soNgayLamViec * 100000)


class NhanVienSanXuat(NhanVien):
    def __init__(self, hoTen, ngaySinh, diaChi, luongCB, soSP):
        super().__init__(hoTen, ngaySinh, diaChi)
        self._luongCB = luongCB
        self._soSP = soSP

    def InThongTin(self):
        super().InThongTin()
        print("Lương cơ bản: ", self._luongCB)
        print("Số SP: ", self._soSP)
        print("Tổng lương: ", self.TinhLuong())
        print("\n")

    def TinhLuong(self):
        return float(self._luongCB + self._soSP * 5000)


def main():
    nhanViens = []
    diaChiNV1 = DiaChi(123, "8", "LinhXuan", "ThuDuc")
    nv1 = NhanVienSanXuat("Hung", "2005-05-11", diaChiNV1, 12313, 213)
    nv2 = NhanVienVanPhong("Hung", "2005-05-11", diaChiNV1, 20)
    nhanViens.append(nv1)
    nhanViens.append(nv2)

    for nhanVien in nhanViens:
        nhanVien.InThongTin()


main()
