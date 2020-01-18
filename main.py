from PIL import Image, ImageDraw
import random
import numpy
import math

size = 10
arr = []

img = Image.new("RGB", (800,800), "black")
draw = ImageDraw.Draw(img)

for i in range(100):
	x = random.randrange(800-size)
	y = random.randrange(800-size)
	arr.append([x,y])

for x,y in arr:
	draw.ellipse((x, y, x+size, y+size), fill = 'white')

arr.sort()
x,y = arr[-1]
# draw.ellipse((x, y, x+size, y+size), fill = 'green')

S = arr[0]
E = arr[-1]
start = arr[0]
MAX = []
ok = 0
while True:
	maxd = 0
	j = []
	for i in range(0,len(arr)):
		if arr[i] == start:
			continue
		X = arr[i][0]-start[0]
		Y = arr[i][1]-start[1]
		degree = math.degrees(math.atan2(X,Y))
		# print(start,arr[i],degree)
		MAX.append([degree,arr[i]])
		if degree > maxd:
			maxd = degree
			j = arr[i]
	MAX.sort()
	if MAX[0][0] < 0 and MAX[-1][0] > 0 and ok == 1:
		q = -1
		while MAX[q][0] > 0:
			q -= 1
		j = MAX[q][1]

	else:
		j = MAX[-1][1]
	MAX = []
	draw.line((start[0]+size//2,start[1]+size//2,j[0]+size//2,j[1]+size//2))
	if start != S:
		arr.pop(arr.index(start))
	start = j
	if start == E:
		ok = 1
	if start == S:
		break

img.show()

root = Tk()
root.resizable(False, False)
root.mainloop()