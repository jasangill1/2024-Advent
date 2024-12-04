data ="""1 3 6 7 9
1 3 6 7 9
1 3 6 7 9
 1 2 3 4 5 6
901241059
 12345
"""




grouped = data.strip().split('\n')

cleaned = [list(map(int, group.split()))for group in grouped]

count = 0 

for group in cleaned:
    check = True    
    firstNum = group[0]
    increase = all(group[i] > group[i - 1] for i in range(1, len(group)))
    decrease = all(group[i] < group[i - 1] for i in range(1, len(group)))
    
    if not(increase or decrease):
        check = False
    for num in range(1,len(group)):
        if abs(group[num] - group[num - 1] - num) > 3:
            check = False
            break
        firstNum = num 
    if check: 
        count += 1
    
    
print(count)
        
        
        
