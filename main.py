from tkinter import *
import random
import math
import time


size = 500
radius = 10
n = 32
arr = []


def LeftRight():
	arr.sort()
	return arr[0],arr[-1]


def pointGenerator():
	for i in range(n):
		x = random.randrange(size-radius)
		y = random.randrange(size-radius)
		screen.create_oval(x,y,x+radius,y+radius, width = 0, fill = "white")
		arr.append([x,y])


root = Tk()
root.title("C O N V E X    H U L L")
root.resizable(False, False)

screen = Canvas(root, width = size, height = size, bg = "black", highlightthickness=0)
screen.pack()

pointGenerator()

left,right = LeftRight()

XX = arr[:]
edge = []
start = left
MAX = []
ok = 0
screen.update()
time.sleep(0.5)
while True:
	maxd = 0
	next_point = []
	for i in range(0,len(arr)):
		if arr[i] == start:
			continue
		
		X = arr[i][0]-start[0]
		Y = arr[i][1]-start[1]
		degree = math.degrees(math.atan2(X,Y))

		if arr[i] != left:
			screen.create_line((start[0]+radius//2,start[1]+radius//2,arr[i][0]+radius//2,arr[i][1]+radius//2), fill = "white")
			time.sleep(0.01)

			for l in XX:
				screen.create_oval(l[0],l[1],l[0]+radius,l[1]+radius, width = 0, fill = "white")
			screen.update()
		
			screen.create_line((start[0]+radius//2,start[1]+radius//2,arr[i][0]+radius//2,arr[i][1]+radius//2), fill = "black")
			time.sleep(0.01)
			
			for l in XX:
				screen.create_oval(l[0],l[1],l[0]+radius,l[1]+radius, width = 0, fill = "white")
			
			for e in edge:
				screen.create_line(e, width = 2, fill = "white")

			screen.update()


		MAX.append([degree,arr[i]])


	MAX.sort()
	if MAX[0][0] < 0 and MAX[-1][0] > 0 and ok == 1:
		q = -1
		while MAX[q][0] > 0:
			q -= 1
		next_point = MAX[q][1]

	else:
		next_point = MAX[-1][1]


	MAX = []
	screen.create_line((start[0]+radius//2,start[1]+radius//2,next_point[0]+radius//2,next_point[1]+radius//2), width = 2, fill = "white")
	edge.append((start[0]+radius//2,start[1]+radius//2,next_point[0]+radius//2,next_point[1]+radius//2))
	screen.update()
	
	start = next_point
	
	if start == right:
		ok = 1
	if start == left:
		break

root.mainloop()