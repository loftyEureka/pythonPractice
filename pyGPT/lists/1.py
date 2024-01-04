'''
1.Write a Python program to find the sum of all the even numbers in a  given of from 1 to 100 list.

'''

number = list(range(1,100))


sum =0

for i  in number:
    if i % 2 ==0:
        sum +=i
    else:
        continue


print(f'The total sum of the list is {sum}')
