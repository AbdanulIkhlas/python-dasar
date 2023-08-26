

#! FILE with iteration
""" 
open in terminal, dont run in vscode
"""

# with open("spider.txt") as file:
#     for line in file:
#         # print(line.upper())
#         print(line.strip().upper()) #?  untuk menghapus spasi

#! Membaca file dan assignt ke var
# fileSpider = open("spider.txt", "r")
# lines = fileSpider.readlines()
# fileSpider.close()

# lines.sort()
# print(lines)

""" 
output: dalam sebaris
['Hello, my name is klaz\n', 
"i'm currently learn ML\n", 
'nice to meet you everybody']
 """


#! WRITE FILE
with open("spider","w") as file:
    file.write("I am a spiderman")

with open("spider") as file:
    for line in file:
        print(line.strip())








