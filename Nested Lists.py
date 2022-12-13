if __name__ == '__main__':
    d1={}
    for _ in range(int(input())):
        name = input()
        d1[name] = float(input())
    d1=dict(sorted(d1.items(),key=lambda x:x[1]))
    s=list(d1.items())[0][1]
    l1=list(d1.items())
    while s in d1.values():
        del l1[0]
        d1=dict(l1)
    l1=list(d1.items())
    s=list(d1.items())[0][1]
    l2=[]
    while s in d1.values():
        l2.append(l1[0])
        del l1[0]
        d1=dict(l1)
    l1=list(sorted(l2,key=lambda x:x[0]))
    for i in l1:
        print(i[0])
