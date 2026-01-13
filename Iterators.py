myList = [1,5,9,12,34]

iterator=iter(myList)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

iller=["İzmir","Bursa","Kayseri","Elazığ","Gaziantep"]
iterator_iller=iter(iller)
for element in iller:
    print(element)

#Kendimiz iterator tasarlayalım

class UsAl:
    def _init_(self,max):
        self,max=max
    
    def _iter_(self):
        self.n=0
        return self
    
    def _next_(self):
        if self.n<self.max:
            result=2**self.n
            self.n+=1
            return result
        else:
            raise StopIteration

sayi=UsAl(7) 
iterator_sayi=iter(sayi)
print(next(iterator_sayi))
print(next(iterator_sayi))
print(next(iterator_sayi))
print(next(iterator_sayi))
print(next(iterator_sayi))
print(next(iterator_sayi))
print(next(iterator_sayi))

class Fibonacci:
    def _init_(self,max):
        self,max=max
        self.a=0
        self.b=1

    def _iter_(self):
        return self

    def _next_(self):
        if self.a>self.max:
            raise StopIteration

        current=self.a
        self.a, self.b=self.b,self.a+self.b
        return current

fibo=Fibonacci(56) 
iter_fibo=iter(fibo)
for i in iter_fibo:
    print(i, end="-")

#even numbers classında parametre 10ken mesela ona kadar olan çift sayıları döndürsün
class EvenNumbers:
    def __init__(self, sayi):
        self.sayi = sayi
        self.current = 0
    
    def __iter__(self):
        self.current = 0
        return self
    
    def __next__(self):
        self.current += 2  # Her seferinde 2 ekleyerek çift sayıları üret
        if self.current <= self.sayi:
            return self.current
        else:
            raise StopIteration    

# Test edelim
ciftsayi = EvenNumbers(10)
for sayi in ciftsayi:
    print(sayi, end=" ")  # 2 4 6 8 10

#uygulama2
nums=[12,8,5,10,15] #iterator ederek sayıların toplamlarını bul ve ortalamalarını hesapla    
iterator_nums = iter(nums)
toplam = 0
eleman_sayisi = 0

try:
    while True:
        sayi = next(iterator_nums)
        toplam += sayi
        eleman_sayisi += 1
except StopIteration:
    ortalama = toplam / eleman_sayisi
    print(f"Sayıların toplamı: {toplam}")
    print(f"Sayıların ortalaması: {ortalama}")

#uyg3
import io

metin="""Ali, Veli
Ayşe

Mehmet

Zeynep

"""

f=io.StringIO(metin)

satir_it=iter(f.readline,'')

bos_olmayan=0
satir_no=0

for line in satir_it:
    satir_no+=1
    s=line.strip()
    print(f"{satir_no:02d}:{s!r}")
    
    if s:
        bos_olmayan+=1

print("boş olmayan satır sayısı: ",bos_olmayan)