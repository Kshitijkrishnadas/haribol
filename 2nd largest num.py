numlst = eval(input())
lst = list(numlst)
for i in range(2):
    for a in range(len(lst)):
        if a == 0:
            mxm = lst[a]
        else:
            if mxm < lst[a]:
                mxm = lst[a]
    if i == 0:
        for k in range(lst.count(mxm)):
            lst.pop(lst.index(mxm))  
print(mxm)
