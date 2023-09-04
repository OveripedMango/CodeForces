# Code Forces 231_A

n = int(input())
sol = 0
for i in range(n):
    res = input()
    if res.count("1") >= 2: 
        sol += 1

print(sol)