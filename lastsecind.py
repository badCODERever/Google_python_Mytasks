if __name__ == '__main__':
    tlist=[]
    slast=[]
    nlist=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        tlist.append([name,score])
        slast.append(score)
    slist=sorted(set(slast))[1:2]
    for j in range(len(tlist)):
        if tlist[j][1]==slist[0]:
            nlist.append(tlist[j][0])
        else:
            continue
    nlist.sort()
    for i in nlist:
        print(i)
    
