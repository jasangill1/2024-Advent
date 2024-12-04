data ="""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""




col = data.strip().split('\n')
print(col)

cleaned = [list(map(int, array.split()))for array in col]

count = 0 

for group in cleaned:
    check = False    
    firstNum = group[0]
    for num in group:
        if abs(firstNum - num) >= 3:
            firstNum = num 
            check = True
    if check: 
        count =+ 1
    
    
print(count)
        
        
        
