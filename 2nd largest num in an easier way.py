numlst=eval(input())
freq=numlst.count(max(numlst))
for i in range(freq):
    numlst.pop(numlst.index(max(numlst)))
mxm=max(numlst)
print(mxm)
