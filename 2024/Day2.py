data ="""1 3 6 7 9
1 3 6 7 9
1 3 6 7 9
 1 2 3 4 5 6
"""




grouped = data.strip().split('\n')

cleaned = [list(map(int, group.split()))for group in grouped]

count = 0 

for group in cleaned:
    check = False    
    firstNum = group[0]
    for num in group:
        if abs(firstNum - num) <= 3:
            firstNum = num 
            check = True
    if check: 
        count += 1
    
    
print(count)
        
        
        
