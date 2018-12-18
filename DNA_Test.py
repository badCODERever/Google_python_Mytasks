DNA=str(input())
newList=''
for c in DNA:
    if c=='G':
        newList+='C'
    elif c=='C':
        newList+='G'
    elif c=='T':
        newList+='A'
    elif c=='A':
        newList+='U'
    else:
        print('Invalid Input')
        newList=''
        break   
print(newList)
    
