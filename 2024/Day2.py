data ="""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""




rows = data.split('\n')
print(rows)

list= []
for group in rows:
    
firstNum = data[0]
count = 0 
for x in data:
    if abs(firstNum - x) >= 3:
        firstNum = x 
        count =+ 1
    
    
print(count)
        
        
 