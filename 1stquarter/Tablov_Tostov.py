g = int(input())
a = input()
a = a.split(" ")
a = list(map(int, a))


a.sort()
sum = 0
for i in range(g):
    if i != g-1:
        sum += (i + 2) * a[i]
    else:
        sum += g * a[i]
print(sum)
