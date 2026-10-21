import csv

#with open("students.csv","r") as file:
    
    #reader = csv.reader(file)

    #next(reader) #to skip first row

    # for row in reader:
    #     print(row)

# with open("students.csv","w",newline = "") as file:

#     writer = csv.writer(file)

#     writer.writerow(["Name","Age","Cource"])

#     writer.writerow(["Mahesh","21","Magento"])

#     writer.writerow(["Suresh","22","AI"])

#     writer.writerow(["Dinesh","23","Data Sceince"])


# with open("employee.csv","w") as file:

#     writer = csv.writer(file)

#     writer.writerows([
#         ["Name","Department","Salary"],
#         ["John","IT",5000],
#         ["Alice","HR",4500],
#         ["Bob","Finance",6000],
#     ])
       

with open("employee.csv","r") as file:

    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row[0])