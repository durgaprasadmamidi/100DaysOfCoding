n = int(input())
ls = []
while n > 0:
    ls.append(n%2)
    n = n//2
print(*ls[::-1],sep='')
