from PIL import Image, ImageDraw
import random


size = 10
img = Image.new("RGB", (500,500), "black")
draw = ImageDraw.Draw(img)
for i in range(10):
	x = random.randrange(500-size)
	y = random.randrange(500-size)
	draw.ellipse((x, y, x+size, y+size), fill = 'white')
img.show()