
#! Read csv
import csv
filename = open("csv_file.txt")
csv_file = csv.reader(filename)

for row in csv_file:
    name,phone,role = row
    print("Name : {}, Phone : {}, Role : {}".format(name,phone,role))


#! Write csv
with open("hosts.csv","w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    # writer.writerows(hosts)


#! Write and read csv using DictWritter
#* write
users = [{"name" : "Abdanul Ikhlas", "username": "klaz", "departmen": "IT Consultant"},
{"name" : "Tegar Wibisana", "username": "gara", "departmen": "BAckend"}]
keys = ["name","username", "departmen"]
with open("by_department.csv","w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader() #? di ambil dari -> fieldnames=keys
    writer.writerows(users) #? di ambil dari -> list users

#* Read
with open("by_department.csv") as by_department:
    reader = csv.DictReader(by_department)
    for row in reader:
        print("Nama : {}, Username : {}, Department : {}".format(row["name"],row["username"], row["departmen"]))