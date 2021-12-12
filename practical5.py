import csv
file=open("student.csv","w",newline="")
fwriter=csv.writer(file)
fwriter.writerow(["rollno","name","marks"])
for i in range(5):
    print("Student Record",i+1)
    rollno=int(input("Enter rollno:"))
    name=input("Enter Name:")
    marks=float(input("Enter Marks:"))
    record=[rollno,name,marks]
    fwriter.writerow(record)
file.close()
file=open("student.csv","r",newline="")
freader=csv.reader(file)
print("The file contains the following records:")
for rec in freader:
    print(rec)
file.close()
