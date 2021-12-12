file=open("story.txt")
content=file.readlines()
file.close()
count=0
for line in content:
    if line[0]=="A":
        count+=1
print("Number of files starting with 'A' are",count)
