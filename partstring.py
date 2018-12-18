def count_substring(string, sub_string):
    value=0
    for i in range(0,len(string)-len(sub_string)+1):
        if string[i:int(len(sub_string))+i]==sub_string:
            value+=1
    return value
        
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
