Left_number=[3,4,2,1,3,3]
Right_number=[4,3,5,3,9,3]

Left_number.sort()
Right_number.sort()

print('the left numbers are:', Left_number)
print('the right numbers are:', Right_number)

new_list = ([y - x for x, y in zip(Left_number,Right_number)])

D = 0
print(new_list)
for i in new_list:
    D += i

print(D)


numbers = [3,4,5]
print('new list:',[number * 5 for number in numbers])