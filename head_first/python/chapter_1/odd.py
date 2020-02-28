from datetime import datetime
import time
import random
print(dir(random))

odds = []
for i in range(1, 60):
	if i % 2 != 0:
		odds.append(i)

for i in range(1, 5):
	right_this_minute = datetime.today().minute
	if right_this_minute in odds:
		print("This minute is an odd minute!.")
	else:
		print("This is an even minute :) ")
	time.sleep(random.randint(1, 60))