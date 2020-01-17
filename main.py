from PIL import Image, ImageDraw
import random


size = 10
arr = []

img = Image.new("RGB", (500,500), "black")
draw = ImageDraw.Draw(img)

for i in range(10):
	x = random.randrange(500-size)
	y = random.randrange(500-size)
	arr.append([x,y])

for x,y in arr:
	draw.ellipse((x, y, x+size, y+size), fill = 'white')

arr.sort()
x,y = arr[0]
draw.ellipse((x, y, x+size, y+size), fill = 'green')



img.show()