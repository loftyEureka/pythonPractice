'''

2.Write a Python program to count the number of occurrences of an element in a list.
'''


num = [1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,11,22,33,44,55,66,77,88,99,00]

rep =0

for i in num:
    if i ==1:
        rep +=1
    else:
        continue


print(f'Number {1} is repeated {rep} times in a list')