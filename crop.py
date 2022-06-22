from PIL import Image

x1, y1=35,175
x2, y2=230,385
w1, h1=200,260

chars=[33, 34, 39, 44, 46, 58, 59, 63, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]

def cropimg(img, src):
	im=Image.open(img)
	w, h=im.size

	x1, y1=35,175
	x2, y2=230,385
	w1, h1=200,260

	for char in chars:
		im1=im.crop((x1, y1, x2, y2))
		im2=im1.convert("1")
		px=im2.load()
		t1=-10
		t2=-10
		for i in range(x2-x1):
			for j in range(y2-y1):
				if px[i,j]!=px[1,1]:
					t1=i-5
					break
			if t1==i-5:
				break

		for i in reversed(range(x2-x1)):
			for j in range(y2-y1):
				if px[i,j]!=px[1,1]:
					t2=i+5
					break
			if t2==i+5:
				break
		im1=im1.crop((t1, 0, t2, y2-y1))
		im1.save("{}/{}.png".format(src, char))

		x1+=w1
		x2+=w1
		if x2>w or char==58 or char==68:
			x1=35
			x2=230
			y1+=h1
			y2+=h1

if __name__ == '__main__':
	crop('./aditya.png', './images')