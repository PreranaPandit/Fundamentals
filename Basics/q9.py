''' NESTED LOOP
 Question -
       XXXXX
       XX
       XXXXX
       XX
       XX


Create F using nested loops.
'''

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    print('X' * x_count)

print('\n')

'''
F printing using while loop
'''
number = [5,2,5,2,2,2]
for xCount in number:
    output = ''
    for count in range(xCount):
        output += 'X'
    print(output + '\n')

'''
L format display
'''

numbers = [2, 2, 2, 2, 5]
for x_count in numbers:
    print('X' * x_count)

