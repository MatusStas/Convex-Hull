from tkinter import *
import random
import math
import time


width = 500
height = 500
size = 10
n = 20
arr = []

root = Tk()
root.title("C O N V E X    H U L L")
root.resizable(False, False)

screen = Canvas(root, width = width, height = height, bg = "black", highlightthickness=0)
screen.pack()

for i in range(n):
	x = random.randrange(width-size)
	y = random.randrange(height-size)
	screen.create_oval(x,y,x+size,y+size, width = 0, fill = "white")
	arr.append([x,y])

arr.sort()

XX = arr[:]

edge = []

S = arr[0]
E = arr[-1]
start = arr[0]
MAX = []
ok = 0
screen.update()
time.sleep(0.5)
while True:
	maxd = 0
	j = []
	for i in range(0,len(arr)):
		if arr[i] == start:
			continue
		X = arr[i][0]-start[0]
		Y = arr[i][1]-start[1]
		degree = math.degrees(math.atan2(X,Y))

		if arr[i] != S:
			screen.create_line((start[0]+size//2,start[1]+size//2,arr[i][0]+size//2,arr[i][1]+size//2), fill = "white")
			time.sleep(0.01)

			for l in XX:
				screen.create_oval(l[0],l[1],l[0]+size,l[1]+size, width = 0, fill = "white")
			screen.update()
			

			screen.create_line((start[0]+size//2,start[1]+size//2,arr[i][0]+size//2,arr[i][1]+size//2), fill = "black")
			time.sleep(0.01)
			for l in XX:
				screen.create_oval(l[0],l[1],l[0]+size,l[1]+size, width = 0, fill = "white")
			
			for e in edge:
				screen.create_line(e, width = 2, fill = "white")

			screen.update()


		MAX.append([degree,arr[i]])
		if degree > maxd:
			maxd = degree
			j = arr[i]

	screen.create_oval(start[0],start[1],start[0]+size,start[1]+size, width = 0, fill = "white")


	MAX.sort()
	if MAX[0][0] < 0 and MAX[-1][0] > 0 and ok == 1:
		q = -1
		while MAX[q][0] > 0:
			q -= 1
		j = MAX[q][1]

	else:
		j = MAX[-1][1]
	MAX = []
	screen.create_line((start[0]+size//2,start[1]+size//2,j[0]+size//2,j[1]+size//2), width = 2, fill = "white")
	edge.append((start[0]+size//2,start[1]+size//2,j[0]+size//2,j[1]+size//2))
	screen.update()
	if start != S:
		arr.pop(arr.index(start))
	start = j
	if start == E:
		ok = 1
	if start == S:
		break

root.mainloop()