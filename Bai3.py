from abc import ABC, abstractmethod
class BatDongSan(ABC):
    def __init__(self, maSo, chieuDai, chieuRong):
        self.maSo = maSo
        self.chieuDai = chieuDai
        self.chieuRong = chieuRong

    @property
    def maSo(self):
        return self._maSo

    @maSo.setter
    def maSo(self, value):
        if value.isdigit() and int(value) > 0:
            self._maSo = int(value)
        else:
            raise ValueError("Ma so khong hop le, phai la so nguyen duong")

    @property
    def chieuDai(self):
        return self._chieuDai

    @chieuDai.setter
    def chieuDai(self, value):
        if value.isdigit() and float(value) > 0:
            self._chieuDai = float(value)
        else:
            raise ValueError("Chieu dai khong hop le, phai la so duong")

    @property
    def chieuRong(self):
        return self._chieuRong

    @chieuRong.setter
    def chieuRong(self, value):
        if value.isdigit() and float(value) > 0 and float(value) < self.chieuDai:
            self._chieuRong = float(value)
        else:
            raise ValueError("Chieu rong khong hop le, phai la so duong")
        
    @abstractmethod
    def tinhGiaTri(self):
        pass
    
    def tinhDienTich(self):
        return self.chieuDai*self.chieuRong
    
    def inThongTin(self):
        print("Ma so: ", self.maSo)
        print("Chieu dai: ", self.chieuDai)
        print("Chieu rong: ", self.chieuRong)
        print("Gia tri: ", self.tinhGiaTri())
        print("Dien tich: ", self.tinhDienTich())



class TinhPhiKinhDoanh(ABC):
    @abstractmethod
    def tinhPhiKinhDoanh(self):
        pass

class DatTrong(BatDongSan):
    def __init__(self, maSo, chieuDai, chieuRong):
        super().__init__(maSo, chieuDai, chieuRong)
    
    def tinhDienTich(self):
        return super().tinhDienTich()

    def tinhGiaTri(self):
        return self.tinhDienTich() * 30_000_000
    
    def inThongTin(self):
        super().inThongTin()
    
class NhaO(BatDongSan):
    def __init__(self, maSo, chieuDai, chieuRong, soLau):
        super().__init__(maSo, chieuDai, chieuRong)
        self.soLau = soLau
        
    @property
    def soLau(self):
        return self._soLau

    @soLau.setter
    def soLau(self, value):
        if value.isdigit() and int(value) >= 0:
            self._soLau = int(value)
        else:
            raise ValueError("So lau khong hop le, phai la so nguyen khong am")
        
    def tinhDienTich(self):
        return super().tinhDienTich()
    
    def tinhGiaTri(self):
        return self.tinhDienTich() * 60_000_000 + self.soLau * 100_000_000
    
    def inThongTin(self):
        super().inThongTin()    
        print("So lau: ", self.soLau)

    
class KhachSan(BatDongSan, TinhPhiKinhDoanh):
    def __init__(self, maSo, chieuDai, chieuRong, soSao):
        super().__init__(maSo, chieuDai, chieuRong)
        self.soSao = soSao
        
    @property
    def soSao(self):
        return self._soSao

    @soSao.setter
    def soSao(self, value):
        if value.isdigit() and int(value) >= 0:
            self._soSao = int(value)
        else:
            raise ValueError("So sao khong hop le, phai la so nguyen khong am")
    
    def tinhDienTich(self):
        return super().tinhDienTich()
    
    def tinhPhiKinhDoanh(self):
        return self.chieuRong * 10000
    
    def tinhGiaTri(self):
        return self.tinhDienTich() * 70_000_000 + self.soSao * 50_000_000
    
    def inThongTin(self):
        super().inThongTin()
        print("So sao: ", self.soSao)
        print("Phi kinh doanh: ", self.tinhPhiKinhDoanh())

    
class BietThu(BatDongSan, TinhPhiKinhDoanh):
    def __init__(self, maSo, chieuDai, chieuRong):
        super().__init__(maSo, chieuDai, chieuRong)
        
    
    def tinhDienTich(self):
        return super().tinhDienTich()
    
    def tinhPhiKinhDoanh(self):
        return self.chieuRong * 5000
    
    def tinhGiaTri(self):
        return self.tinhDienTich() * 100_000_000
    def inThongTin(self):
        super().inThongTin()
        print("Phi kinh doanh: ", self.tinhPhiKinhDoanh())

    
def main():
    listBDS = []
    kSan01 = KhachSan("232","3213","32","2")
    bThu01 = BietThu("231","1214","32")
    nhaO1 = NhaO("3213","321","32","2")
    dTrong01 = DatTrong("3243","42","23")
    listBDS.append(kSan01)
    listBDS.append(bThu01)
    listBDS.append(nhaO1)
    listBDS.append(dTrong01)
    
    tongPhiKinhDoanh = 0
    for bds in listBDS:
        bds.inThongTin()
        if bds.tinhDienTich() > 1000:
            print("BDS co dien tich > 1000")
        print("-------------------------")
        if isinstance(bds, TinhPhiKinhDoanh):
            tongPhiKinhDoanh += bds.tinhPhiKinhDoanh()
    print("Tong phi kinh doanh: ", tongPhiKinhDoanh)
    
if __name__ == "__main__":
    main()