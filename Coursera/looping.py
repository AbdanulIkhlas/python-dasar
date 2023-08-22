
# #! WHILE ------------------
# x = 0
# while x < 5 :
#     print("x = " + str(x))
#     x += 1
# print("last x : " + str(x))

# #* contoh lain
# # def getUsername(username):
# #     return username == "klaz"
# # username = getUsername()
# # while not validUsername(username):
# #     print("invalid username")

# #! Foor Loop -----------------------
# print("")
# for x in range(5):
#     print("hello world " + str(x))

# friends = ['Taylor', 'Klaz', 'Alex']
# for friend in friends:
#     print("Hi " + friend)

# print("===============")
# #* For dengan range 3 parameter (awal,akhir,step)
""" 
bisa juga 2 parameter dalam range(awal,akhir)
"""
# def to_celcius(x):
#     return (x-32)*5/9

# for x in range(0,101,10): #? 0 : awal, 101 : akhir, dalam 10 langkah
#     print(x,"F = ",to_celcius(x), "C" )

# for n in range(6,18+1,3):
#     print(n*2)



# #* Iterasi Mundur
# for x in range(2, -2, -1):
#     print(x) #? The loop should print 2, 1, 0, -1


#* Mencetak seperti domino
# for left in range(7):
#     for right in range(left,7):
#         print("[",left,"|",right,"]",end=" ")
#     print()

#! Rekursif function
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

print("3! = ",factorial(3))
