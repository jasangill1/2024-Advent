Left_number=[3,4,2,1,3,3]
Right_number=[4,3,5,3,9,3]

Left_number.sort()
Right_number.sort()

print('the left numbers are:', Left_number)
print('the right numbers are:', Right_number)

D1 = abs(Left_number[0] - Right_number[0])
D2 = abs(Left_number[1] - Right_number[1])
D3 = abs(Left_number[2] - Right_number[2])
D4 = abs(Left_number[3] - Right_number[3])
D5 = abs(Left_number[4] - Right_number[4])
D6 = abs(Left_number[5] - Right_number[5])

total_D = D1 + D2 + D3 + D4 + D5 + D6

print("Total D:", total_D)
    