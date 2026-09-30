from PIL import Image

size_fraction = 2

img = Image.open("rocket.bmp")
new_size = (img.width // size_fraction, img.height // size_fraction)
img = img.resize(new_size, Image.LANCZOS)
img.save('rocket.bmp')