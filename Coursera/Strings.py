# STRING
name = "klaz"
#! Strng indexing
""" 
    K l a z
    0 1 2 3
"""
# print(name[2]) #? Output : a

#! Negatif indexing : mengetahui karakter apa muulai dari terkhir
# alamat = "Tambak Bayan 5 No 4A"
# print(alamat[-1]) #? output : A
# print(alamat[-4]) #? output : o

#! Slide indexing
""" mengambil karakter index 1 - 4 """
# print(alamat[1:4]) #? :: amb
# fruit = "PotatoKomaO"
# print(fruit[3:]) #? :: atoKomaO
# print(fruit[:3]) #? :: Pot

# print(fruit[:5] + fruit[5:]) #? :: PotatoKomaO

#! Mengganti Karakter / fix typo
# message = "Only lou forever"
""" 
l index 5 dapat di ganti menjadi y 
Dapat di ganti menjadi dengan cara berikut
"""
# new_message = message[0:5] + "y" + message[6:]
# print(new_message)

#! Untuk mengetahui karakter tersebut index berapa
# animal = "Cat Orange"
# print(animal.index("O")) #? :: 4
# print(animal.index("ge")) #? :: g -> 8

# print("Cat" in animal) #? True
# print("Dogs" in animal) #? False

#!--------------------------
#! More Method of strings
varTemp = "Mountain"
print(varTemp.lower()) #? auto lower case
print(varTemp.upper()) #? auto upper case

varTemp2 = " yes "
print(varTemp2.strip()) #? menghilangkan space
print(varTemp2.lstrip()) #? menghilangkan space di kiri
print(varTemp2.rstrip()) #? menghilangkan space di kanan

varTemp3 = "find me in another dimension mwehehehe" #? terdapat 7 e
print(varTemp3.count("e")) #? menghitung banyak karakter e

varTemp4 = "Forest"
#? mengecek apakah ada rest di akhir/awal
print(varTemp4.endswith("rest")) # true
print(varTemp4.endswith("restourant")) # false
print(varTemp4.startswith("Fo")) # true


varTemp5 = "123"
#? mengecek apakah string adalah angka
print(varTemp5.isnumeric()) # true
print(int(varTemp5) + int("321")) # 444


varTemp6 = ["this","is","the","sentence"]
#? menggabungkan di setiap array string
print("...".join(varTemp6))

varTemp7 = "Last Sentence in this example"
#? split to array strings
print(varTemp7.split())