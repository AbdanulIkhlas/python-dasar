import numpy as np

#! membuat array 2 dimensi
two_dim_arr = np.array([[1,2,3], [4,5,6]])
print(two_dim_arr)

#! membuat array 1 dimensi menjadi 2 dimensi
# 1-D array 
print("Sebelum di buat jadi 2")
one_dim_arr = np.array([1, 2, 3, 4, 5, 6])
print(one_dim_arr)
#? Multidimensional array using reshape()
multi_dim_arr = np.reshape(
                one_dim_arr, # the array to be reshaped
               (2,3) # dimensions of the new array
              )
print("Setelah di buat jadi 2 ")
print(multi_dim_arr)

#! mengetahui dimensi array
print("Dimenasi array :", multi_dim_arr.ndim)

#! mengetahui shape baris dan kolom array/matriks
print("Baris,Kolom",multi_dim_arr.shape)

#! mengetahui size baris dan kolom array/matriks
print("size :",multi_dim_arr.size)

#! operasi array
arr_1 = np.array([2, 4, 6])
arr_2 = np.array([1, 3, 5])

# Adding two 1-D arrays
addition = arr_1 + arr_2
print(addition)

# Subtracting two 1-D arrays
subtraction = arr_1 - arr_2
print(subtraction)

# Multiplying two 1-D arrays elementwise
multiplication = arr_1 * arr_2
print(multiplication)

#! perkalian vektor
vector = np.array([1, 2])
print(vector * 1.6)

print("-------------------------")
#! Slicing
""" 
Mengiris memberi Anda sublist elemen 
yang Anda tentukan dari larik. 
Notasi irisan menentukan nilai awal dan akhir, 
dan menyalin daftar dari awal hingga tetapi
 tidak termasuk akhir (eksklusif akhir).

format : 
 array[start:end:step]
"""
a = ([1, 2, 3, 4, 5])
# print(a[2])

# mulai dari index yang di pilih
sliced_arr = a[1:4] #? [2, 3, 4]
sliced_arr = a[:3] #? [1, 2, 3]
sliced_arr = a[2:] #? [3, 4, 5]
sliced_arr = a[::2] #? [1, 3, 5]
# print(sliced_arr)

#! membagi menjadi 2D
two_dim = np.array(([1, 2, 3],
          [4, 5, 6], 
          [7, 8, 9]))

sliced_arr_1 = two_dim[0:2]
print(sliced_arr_1)
""" 
[1, 2, 3],
[4, 5, 6]
"""

sliced_two_dim_rows = two_dim[1:3]
print(sliced_two_dim_rows)
""" 
[[4 5 6]
 [7 8 9]]
"""

sliced_two_dim_cols = two_dim[:,1]
print(sliced_two_dim_cols)
""" 
[2 5 8]
 """

print("\n-------------------------------------\n")
#! Stacking
""" 
np.vstack() - menumpuk secara vertikal
np.hstack() - menumpuk secara horizontal
np.hsplit() - membagi larik menjadi beberapa larik yang lebih kecil
"""

a1 = np.array([[1,1], 
               [2,2]])
a2 = np.array([[3,3],
              [4,4]])
print(f'a1:\n{a1}')
print(f'a2:\n{a2}')

vert_stack = np.vstack((a1, a2))
print(vert_stack)
""" 
[[1 1]
 [2 2]
 [3 3]
 [4 4]]
"""

horz_stack = np.hstack((a1, a2))
print(horz_stack)
""" 
[[1 1 3 3]
 [2 2 4 4]]
"""











