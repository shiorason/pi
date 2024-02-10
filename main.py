import random

print('非負整数で入力してください。')
count = int(input('試行回数(多いほど正確ですが、時間がかかります。おすすめは10〜30):'))
pi_amount = 0

for j in range(count):
  point = 10000000
  circle = 0
  square = 0

  for i in range(point):

	  x = random.uniform(-1, 1)
	  y = random.uniform(-1, 1)
	  square += 1

	  if x*x+y*y <= 1:

		  circle += 1

  pi = 4*circle/square
  pi_amount += pi
print(pi_amount/count)
