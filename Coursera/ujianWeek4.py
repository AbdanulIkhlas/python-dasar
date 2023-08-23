# PENERAPAN STRING,LIST,DICTIONARY
#! NO 1
colors = ["red","white","blue"]
colors.insert(2,"yellow")
print(colors)

#! NO 2
def confirm_length(word):

    # Complete the condition statement using a string operation. 
    if len(word) > 0:
        # Complete the return statement using a string operation.
        return len(word)
    else:
        return 0


print(confirm_length("a")) # Should print 1
print(confirm_length("This is a long string")) # Should print 21
print(confirm_length("Monday")) # Should print 6
print(confirm_length("")) # Should print 0

#! NO 3
def highlight_word(sentence, word):
    # Complete the return statement using a string method.
    return sentence.replace(word,word.upper())


print(highlight_word("Have a nice day", "nice"))
# Should print: "Have a NICE day"
print(highlight_word("Shhh, don't be so loud!", "loud"))
# Should print: "Shhh, don't be so LOUD!"
print(highlight_word("Automating with Python is fun", "fun"))
# Should print: "Automating with Python is FUN"

#! NO 4
def sort_distance(distances):
    distances.sort() # Sort the list
    distances.reverse() # Reverse the order of the list
    return distances


print(sort_distance([2,4,0,15,8,9]))
# Should print [15, 9, 8, 4, 2, 0]

#! NO 5
def count_numbers(text):
  # Initialize a new dictionary.
  dictionary = {}  # Inisialisasi kamus kosong

  # Complete the for loop to iterate through each "text" character.
  for char in text:
    # Complete the if-statement using a string method to check if the
    # character is a number.
    if char.isdigit():
      # Complete the if-statement using a logical operator to check if 
      # the number is not already in the dictionary.
      if char not in dictionary:
           # Use a dictionary operation to add the number as a key
           # and set the initial count value to zero.
           dictionary[char] = 0
      # Use a dictionary operation to increment the number count value 
      # for the existing key.
      dictionary[char] += 1
  return dictionary

print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}


#! NO 6
car = "Lamborghini"
print(car[3:-5])
print(car[-4:])
print(car[:7])

#! NO 7
def increments(start, end):
    return [ x for x in range(start+2,end+3) ] # Create the required list comprehension.


print(increments(2, 3)) # Should print [4, 5]
print(increments(1, 5)) # Should print [3, 4, 5, 6, 7]
print(increments(0, 10)) # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#! NO 8
def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.    
    for key in animal_dict.items(): 
        # Use a string method to format the required string.
        result += key[0] + "\n"
    return result


print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))

# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger

#! NO 9
def combine_guests(guests1, guests2):
  guests2.update(guests1) # Use a dictionary method to combine the dictionaries.
  return guests2

Ricks_guests = { "Adam":2, "Camila":3, "David":1, "Jamal":3, "Charley":2, "Titus":1, "Raj":4}
Tessas_guests = { "David":4, "Noemi":1, "Raj":2, "Adam":1, "Sakira":3, "Chidi":5}

print(combine_guests(Ricks_guests, Tessas_guests))
# Should print:
# {'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}
