# TUPLE

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters : {}, Average lenght: {}".format(chars, chars/len(animals)))


#! menggunakan function enumerate : looping dengan memanggil indexnya
""" 
Fungsi enumerate() mengambil daftar sebagai 
parameter dan mengembalikan tuple untuk setiap 
elemen dalam daftar. Nilai pertama dari tuple 
adalah indeks dan nilai kedua adalah elemen itu sendiri
"""
winners = ["Ashley", "Dylan", "Rose"]
for index,person in enumerate(winners):
    print("{}. {}".format(index+1, person))

#* contoh enumerate, menampilkan index yang ganjil
def skip_elements(elements):
	result = [];
	for index,element in enumerate(elements):
		if((index+1) % 2 != 0):
			result.append(element)
	return result
print("\nPrint the ganjil index from this tuple")
print('"a", "b", "c", "d", "e", "f", "g"')
print("'Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'")
print("\nthe result")
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']