data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
print(len(data))

average = 0
for count1 in data:
	average += len(count1)

print(average / len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print(len(new))
print(new[0])