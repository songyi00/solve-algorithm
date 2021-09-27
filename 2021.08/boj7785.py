import sys 
input = sys.stdin.readline

n = int(input())
people = {}
for _ in range(n):
    name, status = input().split()
    people[name] = status

result = []
for k,v in people.items():
    if v == 'enter':
        result.append(k)

result.sort(reverse=True)
for r in result:
    print(r)


