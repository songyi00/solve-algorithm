apple , banana = map(int,input().split())

i = 1 # 사람 수 
max_num = max(apple,banana)
while i<=max_num:
    if apple%i==0 and banana%i==0:
        print(i,apple//i,banana//i)
    i+=1