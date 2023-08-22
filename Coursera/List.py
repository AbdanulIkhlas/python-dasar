# LIST
# x = ["now","we","are","Programming!"]
# print(type(x)) # <class 'list'>
print("Fruits Before Modif")
fruits = ["pineapple", "banana", "mango"]
print(fruits)

#! Menambahkan data
print("\nADD Melon")
fruits.append("Melon")
print(fruits) # menambahkan buah di akhir list

#! INSERT DATA
print("\nInsert Potato in index 1")
fruits.insert(1,"Potato")
print(fruits)

#! REMOVE DATA by remove method
print("\Remove Mango")
fruits.remove("mango")
print(fruits)

#! REMOVE DATA by pop method for the index
print("\nRemove index 0 : pineapple")
fruits.pop(0)
print(fruits)

#! edit list
print("\nModify banana to appleGreen")
fruits[1] = "appleGreen"
print(fruits)