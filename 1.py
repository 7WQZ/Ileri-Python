#Variables
x=5
y="Ayşe"
print(x)
print(y)

#casting
x=12
print(type(x))

x=str(12)
print(type(x))

y=int(3)
z=float(3)
print(y)
print(z)

x="Ali"
x='ali'

#case sensitive 
a=4
A="John"

print(a)
print(A)

#many values to multiple variables
x,y,z="elma","armut","vişne"

#one value to multiple variables
x=y=z="Ayva"
print(x)
print(y)
print(z)

#unpack a collection
fruits=["elma","armut","vişne"]
x,y,z=fruits
print(x)
print(y)
print(z)

#global variables
x="fantastic"

def myfunc():
    print("Python is " + x)

myfunc()

###
x="fantastic"
def myfunc():
    x="awesome"
    print("python is " + x)

    myfunc()
    print("python is " + x)
    
#global keyword
def myfunc():
    global x
    x="fantastic"

myfunc()
print("python is " + x)    

#devam global
x="awesome"

def myfunc():
    global x
    x="fantastic"

myfunc()
print("python is " + x)

#data types
x="hello world"
print(type(x))

x=20
print(type(x))

x=1j
print(type(x))

x=20.5
print(type(x))

x=["elma","armut","kayısı"]
print(type(x))

x=("elma","armut","kayısı")
print(type(x))

x=range(6)
print(type(x))  

x={"elma","armut","kayısı"}
print(type(x))

x={"name":"Watson","age":34}
print(type(x))

#list, set, tuples
mylist=[1,2,2,3]
print(f"{100*'-'}")
print(f"benim listem bu: {mylist}") #bu kullanımı her değişkene entegre edebilirsin
print(mylist)
mylist[0]=100
print("benim listem bu: " + mylist) #bu kullanım sadece string değerler için geçerli burada oyüzden hata alıyoruz

#tuple(hata normal değiştirilemez silinemez eklenemez...)
mytuple=(1,2,2,3)
print(mytuple)
mytuple[0]=100
print(mytuple)

#set(hata normal index numarasına göre ekleme yok normal add, remove ile ekleme silme mevcut)
myset={1,2,3}
print(myset)
myset={1,2,2,3}
print(myset)

myset.add(9)
print(myset)

#String Array
a="hello world"
print(a[0])

print(len(a))

for x in "Mehmet Akif Ersoy":
    #print(x) -> direkt alt alta yazar
    print(x,end=" ")

#check string
txt="Bilişim Sistemleri Mühendisliği okuyorum"
print("Makü" in txt)

print("Makü" not in txt)

#slicing
txt="hello world python programming"
print(txt[1:4])
print(txt[:5])
print(txt[3:])
print(txt[-5:-1])

#python string metots kısmında daha fazla var istersen bakabilirsin ileride kullanılacak

#modify string
a="   hello world   "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("h","j"))
print(a.split(","))

#string concatanetion
a="hello"
b="world"
c=a+b
print(c)

#string format
age=36
txt="my name is John, I am " + str(age)
print(txt)

#f-strings (formatlı yazı demek oradaki f)
age=45
txt=f"My name is John, I am {age} years old"
print(txt)

#string methods devam... 
txt="hello, and welcome to my world"
x=txt.capitalize() #baş harfi büyüttü
print(x)

x=txt.endswith(".")
print(x)

txt="CompanyX123"
x=txt.isalpha()
print(x)

txt="welcome to my world"
x=txt.title()
print(x)

txt="50"
x=txt.zfill(10) #başa 10 tane 0 koydu
print(x)

print(10>9)
print(10==9)
print(10<9)

#Basit hesap makinesi

a = int(input("Birinci sayı: "))
b = int(input("İkinci sayı: "))

#aritmetik operatörler
print("Toplama: ", a + b)
print("Çıkarma: ", a - b)
print("Çarpma: ", a * b)
print("Bölme: ", a / b)

print("Mod alma (kalan bulma): ", a % b)
print("Üs alma: ", a ** b)

#karşılaştırma operatörleri
print("a>b: ", a>b)
print("a<b: ", a<b)
print("a==b: ", a==b)
print("a!=b: ", a!=b)

#mantıksal operatörler
print("a>0 and b>0: ", a>0 and b>0)
print("a>0 or b>0: ", a>0 or b>0)
print("not(a>b): ", not(a>b)) 

#python lists
thisList = ["apple", "banana", "cherry"]
print(thisList)
print(len(thisList))

list1 = ["abc", 34, True, "male"]
print(list1)

print(thisList[1])
print(thisList[-1])


thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[2:5])

thisList[1] = "strawberry"
print("thisList yeni hali: ", thisList) 

#append items
thisList = ["apple", "banana", "cherry"] 
thisList.append("orange")
print(thisList)

#insert items
thisList = ["apple", "banana", "cherry"]
thisList.insert(1, "orange")
print(thisList)

#extend list
thisList = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thisList.extend(tropical)
print(thisList)

#remove items
thisList = ["apple", "banana", "cherry"]
print("thisList: ", thisList)
thisList.pop(1)
print("thisList: ", thisList)

thisList = ["apple", "banana", "cherry"]
thisList.remove("apple")
print(thisList)

thisList = ["apple", "banana", "cherry"]
thisList.clear()
print(thisList)
#-----------------------------------------
del thisList

thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x)

    thisList = ["apple", "banana", "cherry"]
    for i in range(len(thisList)):
        print(thisList[i])

#while
thisList = ["apple", "banana", "cherry"]
i = 0
while i < len(thisList):
    print(thisList[i])
    i += 1

    thisList = ["apple", "banana", "cherry"]
    [x for x in "thisList"] #list comprehension

"""my_listtt = ['b' for x in thisList]
print(my_listtt) """ 

#sort list
thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort()
print(thisList)
thisList.sort(reverse = True)
print(thisList)

#copy list
thisList = ["apple", "banana", "cherry"]
myList = thisList.copy()
print(myList)

#remove item from list
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

fruits = ["apple", "banana", "cherry"]
x = fruits.count("apple")
print(x)

#Dictionaries
thisList = {
    "brand": "Ford",
    "model": "Focus",
    "year": 2021
}

x = thisList["model"]
print(x)

x = thisList.get("model")
print(x)

x = thisList.keys()
print(x)

x = thisList.values()
print(x)

x = thisList.items()
print(x)

thisList["year"] = 2019
print(thisList)

thisDict = {
    "brand": "Ford",
    "model": "Fiesta",
    "year": 2008
}
thisDict["color"] = "red"
print(thisDict)

thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1986
}

thisDict.pop("model")
print(thisDict)

for x in thisDict:
    print(x)

for x in thisDict.keys():
    print(x)    

for x, y in thisDict.items():
    print(x, y)

#Python if else kullanımı
a = 200
b = 33

if b>a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")

#while 
i = 1
while i < 6:
    print(i)
    i += 1

#with break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1    

#continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#Functions
def my_function():
    print("Hello from a function")

my_function()

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Samet", "Demir")

#my_function("Sam") #bu hatalı neden hatalı lname kısmını yazmadğımızdan

#arbitrary arguments, *args
def my_function(*args):
     print("En genç çocuk: " + args[2])

my_function("Emir", "Efe", "Ali")
# my_functiob("Emir", "Efe") #hata verir çünkü 2. index yok

def demo_func(*args):
    if len(args) >= 3:
        print("2. index: ", args[2])
    elif len(args) >= 2:
        print("1. index: ", args[1])
    else:
        print("Yeterli parametre girilmedi")

demo_func(10,20,30)
demo_func(10,20)

#keyword arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emir", child2 = "Efe", child3 = "Ali")

def my_function(**kwargs):
    print("His last name is " + kwargs["lname"])

my_function(fname = "Ali", lname = "Taş")
my_function(fname = "Ali", lname = "Taş", middle = "None")

#default parameter value
def my_function(country = "Norway"):
    print("I am from " + country)

my_function()
my_function("Sweden")
my_function("USA")

#file handling
#open a file
f = open("ileripy.txt", "C:/Users/smtdm/Desktop/İleri Python/ileripy.txt")
print(f.read())
f.close()

f = open("ileripy.txt", "r")
print(f.read(10))
f.close()

f = open("ileripy.txt", "r")
print(f.readline())
f.close()

f = open("ileripy.txt", "r")
for x in f:
    print(x)
f.close()

f = open("ileripy.txt", "a")
f.write("This is a new line")
f.close()
f = open("ileripy.txt", "r")
print(f.read())
f.close()

import os 
os.remove("ileripy.txt")

if os.path.exists("ileripy.txt"):
    print("The file exists")
else:
    print("The file does not exist")

#delete folder
import os
os.rmdir("deneme.txt")     

sayilar=[22,24,26,32,36]
yeni_sayilar=[  i*2    for i in sayilar]
print(yeni_sayilar)

#uzun hali
dene=[]
for i in sayilar:
    dene.append(i*2)

print(dene)

plaka_kodlari=[45,35,6,34,48,32]
yeni_plaka_kodlari=[i**2    for i in plaka_kodlari]
print(yeni_plaka_kodlari)

listem=[charecter   for charecter in [1,2,3]]
print(listem)


aa=[ i       for i in range(12) if i%2==0]
print(aa)


numbers=[-2,-7,-9,-4,8,21,54]
positive_numbers=[ i     for i in numbers if i>0]
print(positive_numbers)


numbers=[1,6,3,8,5,9]
modified_numbers= [i*3     for i in numbers if i>5]
print(modified_numbers)


yy=[  "çift sayı"  if i%2==0  else "tek sayı"  for i in range(8)]
print(yy)

sicaklik=[32,100,-40,212,0]
donusturulmus_sicaklik=[ ((i-32)*5/9) if i>0 else i  for i in sicaklik]
print(donusturulmus_sicaklik)


words=["apple","cat","banana","dog"]
modified_words=[ word   if len(word)>3  else "kısa kelime"  for word in words]
print(modified_words)

notlar=[85,92,58,77,99]
harf_karsiliklari=[ 'A'  if  nott>=90  else  'B' if nott>=80  else 'C' if nott>=70 else 'D'    for nott in notlar]
print(harf_karsiliklari)

names=['M.John','F.ALice','M.Bob','F.Diana']
greetings=[ 'Mr'+name[1:]  if name[0]=='M' else 'Ms'+name[1:]  for name in names]
print(greetings)

#list comprehension with functions
def digitSum(n):
    dsum = 0
    for ele in str(n):
        dsum += int(ele)
    return dsum

list1 = [367, 111, 562, 945, 6726,873]
new_list1 = [digitSum(i) for i in list1 if i%2!=0]
print(new_list1)

matris = [ [j for j in range(3)] for i in range(5)]
print(matris)

isim = "MAKÜ BSM"
listem = [chr for chr in isim]
print(listem)

#lambda functions

x = lambda a : a + 10
print(x(5))

y = lambda a, b : a * b
print(y(3, 4))

z = lambda a, b, c : a + b + c
print(z(5, 6, 2))

def math(n):
    return lambda a : a ** n

kare = math(2)
print = (kare(8))

kup = math(3)
print(kup(7))

even_numbers = [2, 4, 6, 8, 10,12]
squared_numbers = [ (lambda x:x**2) (i) for i in even_numbers]
print(squared_numbers)

words = ["apple","cat","banana","dog"]
word_length = [ (lambda x:x+" kelimesi uzundur" if len(x)>3 else x+" kelimesi kısadır") (word)  for word in words]
print(word_length)

#Pythonda Map Kullanımı
numbers = [1, 3, 5, 9, 10, 4]

def square(sum):
    return sum**2
result = list (map(square, numbers))
print(result)

#diğer örnek
words = ["python", "map", "function"]
buyuk_harf = list(map(str.upper, words))
print(buyuk_harf)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

toplam_liste = list(map(lambda x, y: x + y, list1, list2))
print(toplam_liste)

sayilar = list(map((lambda x:x%2), [i for i in range(2, 44)]))
print(sayilar)

isimler = ["Elif", "Berk", "Can", "Ece", "Emirhan"]
bas_harf = [isim[0] for isim in list(map(lambda x:x,isimler)) if len(isim)<4]
print(bas_harf)

list1 = [10, 20, 5, 15]
list2 = [7, 25, 10, 5]

cikar = [sonuc for sonuc in list(map(lambda x, y: x - y, list1, list2)) if sonuc<0]
print(cikar)

#Pythonda Filter Kullanımı
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #kendi örneğim number olan
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']
def filter_words(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if letter in vowels:
        return True
    else:
        return False
    
filter_words = list(filter(filter_words, letters))
print(filter_words)

#diğer örnek
seq = [0, 1, 2, 3, 5, 8, 13]
result = list(filter(lambda x: x % 2 !=0, seq))
print(result)

#diğer örnek
def is_multiple_of_3(num):
    return num%3==0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: is_multiple_of_3(x), numbers))
print(result)

#asal sayıları filtreleme
numbers = range(1, 50)
def is_prime(n):
    if n <2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
asal = list(filter(is_prime, numbers))
print(asal)
#--------------------------------------------------------------

numbers=[12,15,20,24,30,35,40,45,48,50,60,75]
#Soru: Bir liste halinde verilen sayıların
#sadece çift ve 3'e bölünebilen olanlarını
#filtreleyip,  bu sayıların karelerini hesaplayın.
#Hem filter hem de list comprehension kullanın

filtered_numbers= list(filter(lambda x: x%2 ==0 and x%3==0,numbers))

kare_al= [i**2 for i in filtered_numbers ]
print(kare_al)


kisiler=["Ali","Derya","Halime","Selim"]
tarihler=[1998,2002,2007,1967]
kisiler_tarihler= list(zip(kisiler,tarihler))
print(kisiler_tarihler)
             
filtrelenmis_kisiler= list(filter(lambda x:1998<= x[1] <=2007,
                                  kisiler_tarihler))
print(filtrelenmis_kisiler)


dosyalar=["data.csv","report.txt","image.png","notes.txt"
          ,"sunum.pptx","script.py"]

filtelenmis_dosyalar= list(filter(lambda x: x.endswith("txt"),
                                  dosyalar))
print(filtelenmis_dosyalar)


employees=[
    {'name':'AHMET','salary':90000,'department':'IT'},
    {'name':'Veli','salary':70000,'department':'Management'},
    {'name':'Ayşe','salary':60000,'department':'Finans'},
    {'name':'Yeşim','salary':50000,'department':'Marketing'},
    {'name':'AHMET','salary':50000,'department':'IT'}    
]

maas_filtrelenmis= list(filter(lambda x: x['salary']>60000
                               ,employees))
print(maas_filtrelenmis)


#Any Kullanımı

myList=[False,True,True]
x=any(myList)
print(x)

#All Kullanımı
mylist=[True,True,True]
mylist2=[False,True,True]
x=all(mylist)
y=all(mylist2)
print(x)
print(y)


#örnek1
#bir listede en az bir pozitif sayı
#olup olmadığını kontrol ediniz

numbers=[-1,-2,0,-5,3,-10]

positive_numbers=any( x>0 for x in numbers)
print(positive_numbers)


#listede tüm sayıların pozitif
#olup olmmadığını kontrol ediniz

kontrol= all( x>0 for x in numbers)
print(kontrol)


#bir listedeki stringlerin en az birinin boş
#olup olmadığını kontrol

strings=["merhaba","dünya", "python",""]

bos_var_mi= any(s==""  for s in strings)
print(bos_var_mi)


words=["elma","muz","vişne","hurma"]
alfabetik= all( w.isalpha() for w in words )
print(alfabetik)


sayilar=[33,44,66,77,88]
cift_mi=all(i%2==0 for i in sayilar)
print(cift_mi)


datam={
    'ad':'Volkan',
    'yas':24,
    'meslek':'Mühendis',
    'sehir':None
}
bos_mu= any(d==None for d in datam.values())
print(bos_mu)

#sorted fonksiyonu

#bir sayı listesini küçükten büyüğe sıralama

numbers=[23,1,45,78,3,12,56]

sorted_numbers=sorted(numbers)
print(sorted_numbers)


employees=[
    {'name':'AHMET','salary':90000,'department':'IT'},
    {'name':'Veli','salary':70000,'department':'Management'},
    {'name':'Ayşe','salary':60000,'department':'Finans'},
    {'name':'Yeşim','salary':50000,'department':'Marketing'},
    {'name':'AHMET','salary':45000,'department':'IT'}    
]

#çalışnalrı maaşlarına göre küçükten büyüğe sıralayalım
#sorted ile
sirali_maas= sorted(employees,key=lambda x: x['salary'])
print(sirali_maas)


numbers=[34,12,56,78,90,23,45]
min_num=min(numbers)
max_num=max(numbers)
print("min:",min_num)
print("max:",max_num)


list1=[10,50,30]
list2=[20,40,60]

min_values=list( map(min,list1,list2))

max_values= list(map(max,list1,list2))

print("min values: ",min_values)
print("max values: ",max_values)

#sum ve round

number=12.34567
rounded_num=round(number,3)
print(rounded_num)

numbers=[111,335,678,986]
print(sum(numbers))

ortalama =sum(numbers)/len(numbers)
print(ortalama)



#Uyg1: 
"""
Size aynı uzunlukta liste1 ve liste2 olmak üzere iki tamsayı listesi verildi. 
Aşağıdaki görevleri gerçekleştiren bir Python programı yazın:

Görev 1: liste1 ve liste2'nin karşılık gelen öğelerini toplamak için map fonksiyonunu 
kullanın.
Görev 2: List comprehension özelliğini kullanarak, toplam değeri 10 eşik 
değerinden küçük olan sonuçları filtreleyin.Yani onları almayın

Görev 3: Yalnızca 10'dan büyük olan toplamları içeren son listeyi döndürün.

list1 = [5, 3, 10, 15]
list2 = [4, 7, 1, 8]

"""
list1=[5,3,10,15]
list2=[4,7,1,8]

son_liste=[ i for i in  list(map(lambda x1,x2: x1+x2,list1,list2)) if i>10 ]
print(son_liste)



""" 
insanların isimlerini temsil eden dizelerden oluşan bir liste verildi. 
Aşağıdaki görevleri yerine getiren bir Python programı yazın:

Görev 1: Her ismin ilk harfini büyük yapmak için map fonksiyonunu kullanın 
(örneğin, 'john', 'John' olur).

Görev 2: Liste kavrama özelliğini kullanarak 3 karakterden az olan isimleri filtreleyin.
yani 3 ten az olanları almayın

Görev 3: 3 karakterden daha uzun olan büyük harfli isimlerin son listesini döndürün.

names = ['ahmet', 'mehmet', 'ali', 'ayşe', 'gül', 'serap']
"""

names = ['ahmet', 'mehmet', 'ali', 'ayşe', 'gül', 'serap']

son_ad=[ad for ad in      list(map(lambda x: x.capitalize(),names)) if len(ad)>3]
print(son_ad)

#uygulama3
"""
Bir liste içinde çeşitli sayıların bulunduğu bir Python listesi veriliyor. 
Sizden istenen, listenin yalnızca çift sayılarını alıp, bu sayıları
2 ile çarparak yeni bir liste oluşturmanızdır. 
Ayrıca, yeni listenin her elemanı için şunu kontrol etmelisiniz: 
Eğer sayı 10'dan büyükse, 
o sayının "Büyük" olarak değiştirilmesini, 
değilse sayının olduğu gibi kalmasını sağlayın.
Bu işlemi list comprehension ile yapın.
"""
numbers = [4, 7, 9, 12, 5, 2, 15, 8]

new_list = ["büyük" if i * 2 > 10 else i*2 for i in numbers if i % 2 == 0]
print(new_list)

#recursive
def faktoryel(n):
    if n==0:
        return 1
    else:
        return n* faktoryel(n-1)
print(faktoryel(5))
print(faktoryel(0))

#0, 1, 1, 2, 3, 5, 8, 13,.
def fibonacci(n):
    
    if n==0:
        return 0
      
    
    elif n==1:
        return 1

    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5)) #yani kendinden önce gelen son 2 sayıyı topladı 
print(fibonacci(6))

##### fibonacci kodu doğru çalışıyor
#-------------------------------------------------------------
#Polindrom öreği
def is_pal_recursive(s,i=0,j=None):
    if j is None:
        j=len(s)-1
    if i>=j:
        return True
    if s[i]!=s[j]:
        return False
    return is_pal_recursive(s,i+1,j-1)

print(is_pal_recursive("recacar"))
print(is_pal_recursive("hello"))
print(is_pal_recursive("level"))

#diğer örnek
def sum_digits(n:int) -> int:
    n = abs(n)
    if n < 10:
        return n
    else:
        return n % 10 + sum_digits(n // 10)
    
print(sum_digits(1234))  # Output: 10    
print(sum_digits(-56789)) # Output: 35
#------------------------son haftadan 1 önce EKSİK-------------------------------------
#Sanırım tamamladım burayı
#-----------------------------------------------------------------------------
def simpleGenerator():
    yield 1
    yield 2
    yield 3

for value in simpleGenerator():
    print(value)

#2.yol
x=simpleGenerator()
print(next(x))
print(next(x))
print(next(x))


#fibonacci
def fib(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a+b
        
fibo=fib(100)
for f in fibo:
    print(f,end="-")


list1=[  i   for i in range(0,50,2)]
print(list1)

list2= (  i  for i in range(0,50,2))
print("list2:",list2)
print(next(list2))
print(next(list2))


def read_file(file_path):
    with open(file_path,'r') as file:
        for line in file:
            yield line

path="/Users/arisoy/Documents/İleri Python Dersi 2025-2026 Yılı/Nutuk.txt"
gen=read_file(path)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num/2)+1):
        if num%i==0:
            return False
    return True
        
    
def generate_prime_numbers():
    num=2
    while True:
        if is_prime(num):
            yield num
        num+=1
        
x=generate_prime_numbers()
print(next(x))
print(next(x))       
print(next(x))


def log_filter_read(file_path,ip):
    with open(file_path,'r') as file:
        for line in file:
            if ip in line:
                yield line

    
x=log_filter_read("/Users/arisoy/Documents/İleri Python Dersi 2025-2026 Yılı/log.txt"
                  ,"192.168.1.1")
for i in x:
    print(i)


def kare_al():
    sayi=0
    while True:
        kare=sayi**2
        yield kare
        sayi+=1

y=kare_al()
print(next(y))
print(next(y))
print(next(y))


def dosya_adi_uret(on_ad,baslangic,bitis,uzanti):
    for i in range(baslangic,bitis):
        yield f"{on_ad}_{i}.{uzanti}"

dosya_adi=dosya_adi_uret("text",1,5,"docx")
for i in dosya_adi:
    print(i)

