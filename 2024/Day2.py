data =[7,6,4,2,1]

firstNum = data[0]


count = 0 

for x in data:
    if abs(firstNum - x) >= 3:
        firstNum = x 
        count =+ 1
    else:
        exit
    
print(count)
        