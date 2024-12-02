Left_number=[3,4,2,1,3,3]
Right_number=[4,3,5,3,9,3]

Left_number.sort()
Right_number.sort()

print('Total Distance:',sum([abs(y - x) for x, y in zip(Left_number,Right_number)]))



