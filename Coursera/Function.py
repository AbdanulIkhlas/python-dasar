#! Membuat function
def greeting(name):
    print("Hello, " + name + ". How are u today")
    print("are you ready " + name + " to code with python")

#! Cara memanggilnya
greeting("Klaz")
greeting("Yohooo")

#! Return Function
def luasSegitiga(alas, tinggi):
    return alas*tinggi/2

segitiga1 = luasSegitiga(5,10)
print("Luas Segitiga 1 : " + str(segitiga1)) #? masih dalam bentuk float
segitiga2 = luasSegitiga(8,10)
print("Luas Segitiga 2 : " + str(int(segitiga2))) #? Agar menjadi int, bukan float

