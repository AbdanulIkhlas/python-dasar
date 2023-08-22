# # BAGAIMANA MAKSUDNYA
# def calculate_storage(filesize):
#     block_size = 4096
#     # Use floor division to calculate how many blocks are fully occupied
#     full_blocks = filesize // block_size
#     print("fullblok : " + str(full_blocks))
#     # Use the modulo operator to check whether there's any remainder
#     partial_block_remainder = filesize % block_size
#     print("partial : " + str(partial_block_remainder))
#     # Depending on whether there's a remainder or not, return
#     # the total number of bytes required to allocate enough blocks
#     # to store your data.
#     if partial_block_remainder > 0:
#         return (full_blocks + 1) * block_size
#     return full_blocks * block_size

# print(calculate_storage(1))    # Should be 4096
# print(calculate_storage(4096)) # Should be 4096
# print(calculate_storage(4097)) # Should be 8192
# print(calculate_storage(6000)) # Should be 8192

num1 = 0
num2 = 0

for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)

def counting():
    x = 1
    while x <= 10:
        print(x)
        x+=1

counting()