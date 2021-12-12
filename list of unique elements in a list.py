def fun(lst):
    uniq=[]
    for a in lst:
        if a not in uniq:
            uniq.append(a)
    return uniq
print(fun(eval(input())))
