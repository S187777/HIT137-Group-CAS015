"""
The code written into python.
"""

total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i- j
counter = 0
while counter < 5:
    if total < 13:
        total += 1
    
    elif total > 13:
        total -= 1
    
    else:
        counter += 2

    #the missing piece for this code is just a return or the value, i.e.:
print(total)