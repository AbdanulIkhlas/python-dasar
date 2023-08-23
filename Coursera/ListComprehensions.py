#! List Comprehensions
multiple = [x*7 for x in range(1,11)]
print(multiple)
""" 
hasilnya : [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
"""

#! menghitung panjang karakter tiap languages
languages = ["Python", "perl", "Ruby", "PHP", "Go", "Java"]
lengths = [len(language) for language in languages]
print(lengths) # hasil : [6, 4, 4, 3, 2, 4]

#! Contoh membuat list kelipatan 3
powerOfThree = [n for n in range(0,101) if n % 3 == 0]
print(powerOfThree) # hasilnya : kelipatan 3, 0 - 99
