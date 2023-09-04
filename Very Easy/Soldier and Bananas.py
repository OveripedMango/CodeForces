# Code Forces 546A 

cost, bank, num = map(int, input().split())

exp = 0

for i in range(1, num+1): 
    exp += (i * cost)

# --- Think more about the actual scenarios 
borrow = exp - bank
if borrow < 0:
    print(0)
else:
    print(borrow)
