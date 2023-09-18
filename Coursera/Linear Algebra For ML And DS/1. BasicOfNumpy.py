import numpy as np 

#! Membuat elemen array 1 dimensi
one_dimensional_arr = np.array([10, 12])
print(one_dimensional_arr)

a = np.array([1, 2, 3])
print(a)

#! membuat array dengan 3 int, start dari 0
b = np.arange(3)
print(b)

b_float = np.arange(3, dtype=float)
print(b_float)

#! membuat array start 1 - 20, kelipatan 3
c = np.arange(1, 20, 3)
print(c)

# dengan tipe data int
c_int = np.arange(1, 20, 3, dtype=int)
print(c_int)

#! membuat array dari 0 - 100 dengan jarak yang sama dengan jumlah elemen sebanyak 5
lin_spaced_arr = np.linspace(0, 100, 5)
print(lin_spaced_arr)

# dengan tipe data int
lin_spaced_arr_int = np.linspace(0, 100, 5, dtype=int)
print(lin_spaced_arr_int)

#! membuat array char dan dan melihat tipe data
char_arr = np.array(['Welcome to Math for ML!'])
print(char_arr)
print(char_arr.dtype) # Prints the data type of the array => <23


#! More on Numpy Arrays
""" 
np.ones() - Mengembalikan nilai pengaturan Array baru menjadi satu.
np.zeros() - Mengembalikan nilai pengaturan Array baru ke nol.
np.empty() - Mengembalikan Array baru yang belum diinisialisasi.
np.random.rand() - Mengembalikan Array baru dengan nilai yang dipilih secara acak.
"""

#! mengembalikan nilai 3 int  menjadi 1
ones_arr = np.ones(3)
print(ones_arr)

#! mengembalikan nilai 3 int  menjadi 0
zeros_arr = np.zeros(3)
print(zeros_arr)

#! mengembalikan nilai 3 int  menjadi 0
empt_arr = np.empty(3)
print(empt_arr)

#! mengembalikan nilai 3 int dengan angka random 0 - 1
rand_arr = np.random.rand(3)
print(rand_arr)




