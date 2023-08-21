#! Perbandingan
print(10>1)
print(1 == "1") #? bisa
#print(1 < "1") #? tidak bisa

def hint_username(username):
    if len(username) < 3 : 
        print("Username to short")
    elif len(username) > 10:
        print("Tooo loong")
    else:
        print("valid username")

hint_username("ta")
hint_username("tai")
hint_username("Yooohoooooo Aw aw aw")

def checkedNumber(number):
    if number > 11: 
        print(0)
    elif number != 10:
        print(1)
    elif number >= 20 or number < 12:
        print(2)
    else:
        print(3)

print("Number is : ")
checkedNumber(10)
