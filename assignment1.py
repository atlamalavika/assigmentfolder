
value=int(input())
for i in range(value):
    if i==2:
        continue
    print(i)

for i in range(value):
    if i==8:
        break
    print(i)


for i in range(value):
    if i==2:
        pass
    print(i)

