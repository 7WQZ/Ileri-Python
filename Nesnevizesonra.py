
#pythonda constructor

class Ogrenci:
    
    def __init__(self,ad=None,soyad=None,no=0,Dogumyeri=None):
        
        self.ad=ad
        self.soyad=soyad
        self.no=no
        self.Dogumyeri=Dogumyeri


ogr1=Ogrenci("Kaan","Taşan",12345,"Adana")
ogr2=Ogrenci("Yeşim","Uyanık")
print(ogr1.ad)
print(ogr2.Dogumyeri)


class Kitap:
    def __init__(self,adi,yazari,sayfasayisi):
        self.adi=adi
        self.yazari=yazari
        self.sayfasayisi=sayfasayisi
    
    def uzunmu(self):
        return self.sayfasayisi>300

kitap1=Kitap("Sözcüklerin Kamera ARkası","Ferhat Taştekin",350)
print(kitap1.uzunmu())

kitap2=Kitap("Dokuzuncu Hariciye Koğuşu","Peyami Safa",244)
print(kitap2.uzunmu())

class Hesap:
    
    def __init__(self,hesap_sahibi,bakiye=0):
        self.hesap_sahibi=hesap_sahibi
        self.bakiye=bakiye
    
    def para_yatir(self,miktar):
        self.bakiye+=miktar
        print(f"yatırılan {miktar} TL. yeni bakiye: {self.bakiye} TL dir.")
    
    
    def para_cek(self,miktar):
        if miktar>self.bakiye:
            print(f"Yetersiz bakiye var mevcut bakiyeniz: {self.bakiye}")
        
        else:
            self.bakiye-=miktar
            print(f"çekilen tutar {miktar} TL. yeni bakiye: {self.bakiye} TL dir.")

my_account=Hesap("Berna Akçalı",100000)
my_account.para_yatir(50000)
my_account.para_cek(200000)
my_account.para_cek(20000)



class Rectangle:
    
    def __init__(self,width,height):
        
        self.width=width
        self.height=height
    
    def area(self):
        
        return self.width*self.height
    
    def perimeter(self):
        
        return 2* (self.width+self.height)

my_rect=Rectangle(7,14)
print(f"Alan: {my_rect.area()}")
print(f"Çevre: {my_rect.perimeter()}")

class Student:
    total_students=0 #bu değişklen class değişkeni
    
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades
        Student.total_students+=1 
    
    def calculate_average(self):
        return sum(self.grades)/len(self.grades)
    
    def display_info(self):
        avg_grade=self.calculate_average()
        return "Öğrenci: "+self.name, "ortalama: "+str(round(avg_grade,2))
    
    #class method
    @classmethod
    def get_total_students(cls):
        return f"toplam öğrenci sayısı: {cls.total_students}"

std1=Student("Ayşe",[85,90,97])
std2=Student("Bekir",[55,66,77])

#instance metot yani nesne üzerinde ulaşıldı
print(std1.display_info())
print(std2.display_info())

#class metot yani sınıf üzerinden ulaşıldı
print(Student.get_total_students())


class Kutuphane:
    
    maksimum_kitap_sayisi=1000
    
    def __init__(self,isim):
        self.isim=isim
        self.kitaplar=[]
    
    def kitap_ekle(self,kitap_adi):
        
        if Kutuphane.kitap_gecerli_mi(kitap_adi):
            if len(self.kitaplar)<Kutuphane.maksimum_kitap_sayisi:
                self.kitaplar.append(kitap_adi)
                print(f"Kitap {kitap_adi} eklendi.")
            else:
                print("maksimum kitap sayısına ulaşıldı.")
        
        else:
            print(f"Kitap adi {kitap_adi} geçersizdir")
    
    def kitaplari_goster(self):
        return f"{self.isim} kütüphanesinde şu kitaplar var: {', '.join(self.kitaplar)}"
    
    @classmethod
    def maksimum_kitap_sayisini_degistir(cls,yeni_limit):
        cls.maksimum_kitap_sayisi=yeni_limit
        print(f" yeni maksimum kitap sayısı: {cls.maksimum_kitap_sayisi}")
    
    
    @staticmethod
    def kitap_gecerli_mi(kitap_adi):
        return isinstance(kitap_adi,str) and len(kitap_adi)>5
    

merkez_kutuphane=Kutuphane("Merkez")
mahalle_kutuphane=Kutuphane("Mahalle")

merkez_kutuphane.kitap_ekle("Sefiller")
merkez_kutuphane.kitap_ekle("")

mahalle_kutuphane.kitap_ekle("savaş ve Barış")
mahalle_kutuphane.kitap_ekle("123")

print(merkez_kutuphane.kitaplari_goster())   

Kutuphane.maksimum_kitap_sayisini_degistir(3000)

print(Kutuphane.kitap_gecerli_mi(1985))
            

class Student:
    
    student_list=[] #class variable
    
    def __init__(self,student_id,name,grade):
        
        if not self.validate_student_id(student_id):
            raise ValueError("geçersiz öğrenci numarası numara std ile başlamalı ve 7 karakter olmalı")
        
        self.student_id=student_id
        self.name=name
        self.grade=grade
    
    
    def add_student(self):
        Student.student_list.append(self)
        print(f" Öğrenci: {self.name} eklendi!")
    
    
    def remove_student(self):
        
        for student in Student.student_list:
            if student.student_id==self.student_id:
                Student.student_list.remove(self)
                print(f"Öğrenci {self.name} silindi!")
                return
        
        print(f"{self.student_id} Öğrencisi bulunamadı.")
    
    
    def display_student_details(self):
        print(f"ID: {self.student_id}\n İsim: {self.name}\n Not: {self.grade}")
    
    
    @classmethod
    def list_students(cls):
        if not cls.student_list:
            print("Liste boş öğrenci yok")
        
        else:
            print("öğrencilerin tam listesi:")
            for student in cls.student_list:
                print(f"ID: {student.student_id}\n İsim: {student.name}\n Not: {student.grade}")
    
    
    @staticmethod
    def validate_student_id(student_id):
        return student_id.startswith('std') and len(student_id)==7

stud1=Student("std1234","Bahar","A")
stud2=Student("std3333","Veysel","A")

stud1.add_student()
stud2.add_student()

Student.list_students()

stud1.display_student_details()
stud2.remove_student()

Student.list_students()

try:
    invalid_stud=Student("1234567","Hasan","C")
    invalid_stud.add_student()
except ValueError as e:
    print("gerçersiz öğrenci numarası")
    

######INHERITANCE  IN PYTHON
class Shape:
    
    def __init__(self,name,color):
        self.name=name
        self.color=color
    
    def display(self):
        print(f" {self.name} şeklinin rengi {self.color} dır")
    

class Rectangle(Shape):
    
    def __init__(self, name, color,width,height):
        super().__init__(name,color)
        
        self.width=width
        self.height=height
    
    def area(self):
        return self.width* self.height
    
    def perimeter(self):
        return  2*(self.width+self.height)

class Circle(Shape):
    
    def __init__(self, name, color,radius):
        super().__init__(name,color)
        self.radius=radius
    
    def area(self):
        return 3.14* (self.radius**2)
    
    def perimeter(self):
        return  2*3.14*self.radius

r1=Rectangle("Dikdörtgen","kırmızı",7,11)
r1.display()
print(f"dikdörtgenin alanı: {r1.area()} , çevresi: {r1.perimeter()}")

c1=Circle("Daire","yeşil",4.5)
c1.display()
print(f"daire alanı: {c1.area()} , çevresi: {c1.perimeter()}")


class Employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self.salary=salary
    
    def display_details(self):
        print(f"name: {self.name} id: {self.emp_id} salary: {self.salary}")
    
    def calculate_bonus(self):
        return self.salary*0.35

class FullTime:
    def __init__(self,benefits):
        self.benefits=benefits
    
    def display_benefits(self):
        print(f"full time benefirs: {self.benefits}")
    

class PartTime:
    def __init__(self,hours_per_week):
        self.hours_per_week=hours_per_week
    
    def display_hours(self):
        print(f"part time hours: {self.hours_per_week}")
    

class Manager(Employee,FullTime):
    
    def __init__(self,name,emp_id,salary,benefits,team_size):
        Employee.__init__(self,name,emp_id,salary)
        FullTime.__init__(self,benefits)
        self.team_size=team_size
    
    #override
    def calculate_bonus(self):
        return self.salary* 0.50
    
    
    #override
    def display_details(self):
        super().display_details()
        print(f"tema size: {self.team_size}")
        self.display_benefits()


        
#02.12.2025 devammmmmmm
class Developer(Employee, FullTime):
    def __init__(self, name, emp_id, salary, programming_language):
        Employee.__init__(self, name, emp_id, salary)
        FullTime.__init__(self, benefits=None)  # Fulltime sınıfının init metodu çağrılıyor
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programlama Dili: {self.programming_language}")    

class Intern(Employee, PartTime):
    def __init__(self, name, emp_id, salary, hours_per_week):
        Employee.__init__(self, name, emp_id, salary)
        PartTime.__init__(self, hours_per_week)
        self.duration_months = duration_months

    def display_details(self):
        super().display_details()
        print(f"Intership duration {self.duration_months} Months")
        self.display_hours()

#Kullanımı
manager = Manager("Alice", 101, 120000, "Health , 401k, Paid Leave", 10)
manager.display_details()
print(f"Bonus: {manager.calculate_bonus()}")

developer = Developer("Bob", 102, 95000, "Health, 401k, Python")
print(f"Bonus: {developer.calculate_bonus()}")

intern = Intern("Charlie", 103, 40000, 20, 6)
intern.display_details()
print(f"Bonus: {intern.calculate_bonus()}")

class Shape:
    def area(self) ->float:
        raise NotImplementedError
    
class Circle(Shape):
    def __init__(self,radius: float) ->None:
        self.radius=radius
    
    def area(self) ->float:
        return 3.14 * (self.radius**2)
    
    def scale(slef, factor: float) ->Circle:
        new_radius=self.radius-factor 
        return Circle(new_radius)
    
class Rectangle(Shape):
    def __init__(self,width: float,height: float) ->None:
        self.width=width
        self.height=height
    
    def area(self) ->float:
        return self.width* self.height
    
    def is_square(self) ->bool:
        return self.height==self.width 

def total_area(shapes: list[Shape]) ->float:
    total: float=0.0
    for s in shapes:
        total+=s.area()
    return total

if __name__=="__main__":
    c1 = Circle(3.0)
    c2 = Circle(3.6)

    r1 = Rectangle(4.0,5.0)
    r2 = Rectangle(6.2,9.5)

    print("c1 alan:", c1.area())
    print("c2 alan:", c2.area())

    print("r1 alan:", r1.area())
    print("r2 alan:", r2.area())   
    print("r1 kare mi?", r1.is_square())
    
    shapes: list[Shape]= [c1,c2,r1,r2]
    toplam: float= total_area(shapes)
    print("toplam alan:", toplam)

#Polymorphisim
class AreaCalculator:
    def area(self,*args):
        if len(args)==1:
            radius=args[0]
            return 3.14 * (radius*2)
        
        elif len(args)==2:
            length, width=args[0], args[1]
            return width * length
        
        elif len(args)==3:
            base, height=args[0], args[1]
            return base * height * 0.5
        else:
            return "geçersiz parametre sayısı"
        
calc=AreaCalculator()
print(f"Daire alanı: {calc.area(7): 2f}")

print(f"Dikdörtgen alanı: {calc.area(10,5): 2f}")

print(f"Üçgen alanı: {calc.area(10,6,8): 2f}")

print(calc.area(10,5,2,4,8))

#encapsulation
class Urun:

    def __init__(self,ad,fiyat,stok):
        self.ad=ad
        self.fiyat=fiyat
        self.__stok=stok #private demek

        def stok_ekle(self,miktar):
            if miktar>0:
                self.__stok+=miktar
                print(f"{miktar}adet stok güncellendi yeni stok: {self.__stok}")
            else:
                print("geçersiz miktar")

        def stok_azalt(self, miktar):
            if miktar>0 and miktar<=self.__stok:
                self.__stok-=miktar
                print(f"{miktar} adet stok azaltıldı kalan stok: {self.__stok}")
            else:
                print("geçersiz miktar")

        def stok_goster(self):
            return self.__stok #javadaki getter gibi

        def __indirimuygula(self, yuzde):
            if 0<yuzde<100:
                indirim_miktari=self.fiyat * (yuzde/100)
                self.fiyat-=indirim_miktari
                print(f"{yuzde}% indirim uygulandı yeni fiyat: {self.fiyat}")
            else:
                print("geçersiz indirim yüzdesi")

        def indirim_yap(self,yuzde):
            self.__indirimuygula(yuzde)

urun1=Urun("Laptop",100000,50)               

urun1.stok_ekle(30)  
urun1.stok_azalt(10)

try:
    print(urun1.__stok)  #hata verir çünkü private
except AttributeError as e:
    print("stok değişkenine doğrudan erişim sağlanamaz.")

print(f"mevcut stok: {urun1.stok_goster()}")
urun1.indirim_yap(10)

try:
    urun1.__indirimuygula(10)  #hata verir çünkü private
except AttributeError as e:
    print("indirim uygulama metotuna doğrudan erişim sağlanamaz.")

#Abstaction in python
from abc import ABC, abstractmethod
class Calisan(ABC):
    
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim

    @abstractmethod
    def maas_hesapla(self):
        pass

    def tam_ad(self):
        return f"{self.isim} {self.soyisim}"
    
class TamZamanliCalisan(Calisan):
    
    def __init__(self, isim, soyisim, aylik_maas):
        super().__init__(isim, soyisim)
        self.aylik_maas = aylik_maas

    def maas_hesapla(self):
        return f"{self.tam_ad()} nın aylık maaşı: {self.aylik_maas} TL" 

class SerbestZamanliCalisan(Calisan):
    
    def __init__(self, isim, soyisim, saatlik_ucret, calisan_saat):
        super().__init__(isim, soyisim)
        self.saatlik_ucret = saatlik_ucret
        self.calisan_saat = calisan_saat

    def maas_hesapla(self):
        toplam_ucret = self.saatlik_ucret * self.calisan_saat
        return f"{self.tam_ad()} nın toplam maaşı: {toplam_ucret} TL" 
    
calisan1 = TamZamanliCalisan("Ali", "Yılmaz", 50000)
calisan2 = SerbestZamanliCalisan("Ahmet", "Karaboğa", 3000, 18)

print(calisan1.maas_hesapla())
print(calisan2.maas_hesapla())

#Diğer Örnek

from abc import ABC, abstractmethod

class Kullanici(ABC):

    kisiler=[]
    def __init(self, ad_soyad):
        self.ad_soyad = ad_soyad
        self.mesajlar=[]
        Kullanici.kisiler.append(self.ad_soyad)

    @abstractmethod
    def mesaj_gonder(self, mesaj):
        pass    

    @abstractmethod
    def bilgi_goster(self):
        print(f"")
        print(f"Kullanıcı Adı: {self.ad_soyad}")

class NormalKullanici(Kullanici):
    def __init__(self, ad_soyad):
        super().__init__(ad_soyad)

    def mesaj_gonder(self, mesaj):
        self.mesajlar.append(mesaj)
        print(f"{self.ad_soyad} mesaj gönderdi: {mesaj}")

    def bilgi_goster(self):
        print(f"Normal Kullanıcı: {self.ad_soyad}")
        print(f"mesajlar: {self.mesajlar}")

class Yonetici(Kullanici):
    def __init__(self, ad_soyad):
        super().__init__(ad_soyad)

    def mesaj_gonder(self, mesaj):
        self.mesajlar.append(mesaj)
        print(f"{self.ad_soyad} mesaj gönderdi: {mesaj}")

    def bilgi_goster(self):
        print(f"Yönetici Kullanıcı: {self.ad_soyad}")
        print(f"mesajlar: {self.mesajlar}")

    def kullanici_sil(self, kullanici):
        print(f"silinmeden önce kişi kistesi: {len(Kullanici.kisiler)}")
        kullanici.kisiler.remove(kullanici.ad_soyad)

        print(f"{self.ad_soyad} yöneticisi şu kişiyi {kullanici.ad_soyad} sildi.")
        print(f"silindikten sonra kişi kistesi: {len(Kullanici.kisiler)}")

normal_kullanici = NormalKullanici("Ali Demir")
yonetici=Yonetici("Hasan Yiğit")

normal_kullanici.bilgii_goster()

for i in range(3):
    normal_kullanici.mesaj_gonder("mesaj " + str(i+1))

yonetici.bilgi_goster()

for i in range(3):
    yonetici.mesaj_gonder("Yönetici mesaj " + str(i+1))

yonetici.kullanici_sil(normal_kullanici)

#Diğer Örnek

from abc import ABC, abstractmethod
from typing import Iterable,List

class UserRepository(ABC):
    @abstractmethod
    def get_all_users(self) -> Iterable[str]:
        pass
class InMemoryUserRepository(UserRepository):
    def __init__(self, users: List[str]):
        self.users=users
    
    def get_all_user(self) -> Iterable[str]:
        for u in self.users:
            yield u


class StaticUserRepository(UserRepository):
    def get_all_users(self) -> Iterable[str]:
        yield "Ayşe"
        yield "Hasan"
        
class CompositeUserRepository(UserRepository):
    def __init__(self, repositories: List[UserRepository]):
        self.repositories=repositories
    
    def get_all_users(self) -> Iterable[str]:
        for repo in self.repositories:
            yield from repo.get_all_users()        

if __name__ == "__main__":
    repo1=InMemoryUserRepository(["Veli","Fidan"])
    repo2=StaticUserRepository()
    all_repos=CompositeUserRepository([repo1,repo2])

    for user in all_repos.get_all_users():
        print("-", user)