def josephus(people, step):
    ls=[]
    ls2=[]
    for i in range(1,int(people)+1):
        ls.append(i)
    step = int(step)-1
    Deiktis=int(step)
    while len(ls)>1:
        ls2.append(ls[Deiktis])
        ls.pop(Deiktis)
        Deiktis=(int(Deiktis)+int(step)) % len(ls)
    ls2.append(ls[0])
    return ls2





'''
atoma=input('ΔΩΣΕ ΑΤΟΜΑ:')
bima=input('ΔΩΣΕ ΒΗΜΑ:')
josephus(atoma,bima)'''
