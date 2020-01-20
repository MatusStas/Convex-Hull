from tkinter import *
import random
import math
import time


size = 500
radius = 10
center = radius//2
n = 32
arr = []
edges = []
ok = 0
MAX = []


def extractCoorinates(actual_point, next_point, center):
	actual_point_coordinates = [x+center for x in actual_point]
	next_point_coordinates = [x+center for x in next_point]
	return actual_point_coordinates, next_point_coordinates

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

left_point,right_point = LeftRight()

XX = arr[:]
actual_point = left_point

screen.update()
time.sleep(0.5)

while True:
	next_point = []
	for index,next_point in enumerate(arr):
		if next_point == actual_point:
			continue
		
		X = next_point[0]-actual_point[0]
		Y = next_point[1]-actual_point[1]
		degree = math.degrees(math.atan2(X,Y))

		screen.create_line(extractCoorinates(actual_point,next_point,center), fill = "white")
		time.sleep(0.01)

		for l in XX:
			screen.create_oval(l[0],l[1],l[0]+radius,l[1]+radius, width = 0, fill = "white")
		screen.update()
	
		screen.create_line(extractCoorinates(actual_point,next_point,center), fill = "black")
		time.sleep(0.01)
		
		for l in XX:
			screen.create_oval(l[0],l[1],l[0]+radius,l[1]+radius, width = 0, fill = "white")
		
		for edge in edges:
			screen.create_line(edge, width = 2, fill = "white")

		screen.update()


		MAX.append([degree,next_point])


	MAX.sort()
	if MAX[0][0] < 0 and MAX[-1][0] > 0 and ok == 1:
		q = -1
		while MAX[q][0] > 0:
			q -= 1
		next_point = MAX[q][1]

	else:
		next_point = MAX[-1][1]

	MAX = []

	screen.create_line(extractCoorinates(actual_point,next_point,center), width = 2, fill = "white")
	edges.append(extractCoorinates(actual_point,next_point,center))
	screen.update()
	
	actual_point = next_point
	
	if actual_point == right_point:
		ok = 1
	if actual_point == left_point:
		break

root.mainloop()