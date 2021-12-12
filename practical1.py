import pickle
file=open("STUDENT.DAT","wb")
more="y"
while more=="y":
    d={}
    rollno=int(input("ENTER THE ROLL NUMBER OF THE STUDENT:"))
    name= input("ENTER THE NAME OF THE STUDENT:")
    marks=float(input("ENTER THE MARKS OF THE STUDENT:"))
    d["rollno"]=rollno
    d["name"]=name
    d["marks"]=marks
    pickle.dump(d,file)
    more=input("Enter more values/(y/n):")
file.close()
file=open("STUDENT.DAT","rb")
try:
    print("This file stores following information:")
    while True:
        data=pickle.load(file)
        print(data)
except EOFError:
    file.close()
