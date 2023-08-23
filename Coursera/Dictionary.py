# DICTIONARY {} : seperti stuct in c++
file_count = {
    "jpg":10,
    "txt":14,
    "csv":2,
    "py":23
}

print(type(file_count))
print(file_count)

#! how to print the value
print("Jumlah Txt : ",file_count["txt"])

#! Menambah elemen di dictionary
file_count["cfg"] = 8
print(file_count)

#! Menambah elemen di dictionary yang sudah ada = update
file_count["txt"] = 17
print(file_count)

#! menghapus element pada dictionary
del file_count["cfg"]
print(file_count)

#! mengecek apkah ada elemen x di dictionary
xTrue = "jpg" in file_count
xFalse = "html" in file_count
print("apakah ada jpg : ",xTrue)
print("apakah ada html : ",xFalse)

#! mengetahui tuple key and value
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
theTupleKeys = cool_beasts.keys()
theTupleValues = cool_beasts.values()
print("Tuple Keys : ",theTupleKeys)
print("Tuple Value : ",theTupleValues)
for animal,body in cool_beasts.items():
    # animal = key, body = value
    print("{} have {}".format(animal,body))

