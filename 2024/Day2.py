data ="""19 20 21 23 24 25 28 26
56 58 60 63 66 69 69
3 6 7 8 11 15
50 53 55 58 63
39 41 42 45 42 44 46
22 25 27 26 25
54 57 54 55 55
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
        