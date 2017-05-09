def orangecap(d):
    topscore=0
    for i in d.keys():
        if topscore < d[i][len(d)]:
            topscore=d.values().values()
            playername=d.values().keys()
    return (playername,topscore)


def addpoly(p1,p2):
    list1=[]
    p3=p1
    p4=p2
    for l in range(len(p1)):
        for m in range(len(p2)):
            if p1[l][1]== p2[m][1]:
                n=((p3[l][0]+p4[m][0]),p3[l][1])
                list1=list1.append(n)
    return (list1)

def multpoly(p1,p2):
    list1=[]
    p3=p1
    p4=p2
    for l in range(len(p1)):
        for m in range(len(p2)):
            if p1[l][1]== p2[m][1]:
                n=((p3[l][0]*p4[m][0]),p3[l][1])
                list1=list1.append(n)
    return (list1)
