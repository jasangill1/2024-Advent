Left_number=[3,4,2,1,3,3]
Right_number=[4,3,5,3,9,3]

Left_number.sort()
Right_number.sort()

print('the left numbers are:', Left_number)
print('the right numbers are:', Right_number)

new_list = ([x - y for x, y in zip(Left_number,Right_number)])

D = 0

for i in new_list:
    i += D

print(i)

    