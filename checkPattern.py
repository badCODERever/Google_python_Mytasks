import re
strp=input()
match=re.search('(\d\d)+\w+(\d\d\d)+-+(\d\d)',strp)
if match:
    for gcount in range(1,4):
        for literals in match.group(gcount):
            if int(literals) <= 0:
                print('invalid')
                break
            else:
                continue
            break
    if (int(strp[0])+int(strp[1]))%2!=1 and (int(strp[3])+int(strp[5]))%2!=1 and (int(strp[4])+int(strp[5])+int(strp[7])+int(strp[8]))%2!=1 and strp[2] not in ['A','E','I','O','U','Y']:
        print('valid')
    else:
        print('invalid')
else:
    print('invalid')
