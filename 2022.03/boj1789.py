S = int(input())

i = 1

while True:
    if i*(i+1) <= 2*S:
        result = i
        i+=1
    else:
        break

print(result)