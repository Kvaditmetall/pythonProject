a = int(input())
b = int(input())
counter = 0
for i in range(a, b):
    if i**3 == 4 or i**3 == 9 or i**3%10 == 4 or i**3%10==9:
        counter +=1
print(counter)