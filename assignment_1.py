x = []

for i in range(0, 10000):
	if (i%2==0) and (i%3==0) and (i%5==0):
		x.append(i)

y = sum(x)

print(y)