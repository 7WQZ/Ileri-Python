#UYGULAMA1
#__iter__ ve __next__ metodlarını yazarak 0’dan N’e kadar çift sayılar üreten bir iterator


class EvenNumbers:
    """0, 2, 4, ... < n üretir."""
    def __init__(self, n: int):
        self.n = n
        self.cur = 0

    def __iter__(self):
        return self  # iterator aynı zamanda iterable

    def __next__(self):
        if self.cur >= self.n:
            raise StopIteration
        val = self.cur
        self.cur += 2
        return val

# kullanım
for x in EvenNumbers(10):
    print(x, end=" ")   # 0 2 4 6 8
print()



#UYGULAMA2
nums = [12, 8, 5, 10, 15]

it = iter(nums)     # nums'un iterator'ı
toplam = 0
adet = 0

while True:
    try:
        v = next(it)           # sıradaki eleman
        print("Aldım:", v)
        toplam += v
        adet += 1
    except StopIteration:      # bittiğinde burada break ile çık
        break

ortalama = toplam / adet if adet else 0
print("Ortalama:", ortalama)


#UYGULAMA3
import io

metin = """Ali, Veli
Ayşe

Mehmet
Zeynep"""

f = io.StringIO(metin)                   # diskte gerçek bir dosya açmadan, bellekte dosya gibi davranan bir metin akışı oluşturur.
satir_it = iter(f.readline, '')          # '' (boş string) gelene dek satır üretir

bos_olmayan = 0
satir_no = 0
for line in satir_it:                    # satır iterator'u
    satir_no += 1
    s = line.strip()
    print(f"{satir_no:02d}: {s!r}")
    if s:
        bos_olmayan += 1

print("Boş olmayan satır sayısı:", bos_olmayan)


#UYGULAMA4
ogrenciler = ["Ali", "Ayşe", "Mehmet", "Zeynep", "Can", "Deniz", "Ece"]

it = iter(ogrenciler)   # tek bir iterator
grup_no = 1

while True:
    a = next(it, None)          # ilk kişi (biterse None)
    if a is None:
        break                   # hiç eleman kalmadıysa çık

    b = next(it, "(boş)")       # ikinci kişi; yoksa "(boş)"
    c = next(it, "(boş)")       # üçüncü kişi; yoksa "(boş)"

    print(f"Grup {grup_no}: ({a}, {b}, {c})")
    grup_no += 1
