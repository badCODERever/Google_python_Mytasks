print('Enter the number of values need to add: ')
N=int(input())
sum_array=0
numArray=list(map(int, input('Enter the values').strip().split()))[:N]
for numbers in numArray:
    sum_array+=numbers
print(sum_array)
