from PIL import Image
import PIL.ImageOps
import glob
files = glob.glob('cameraman.tif')
for f in files:
image = Image.open(f)
inverted_image = PIL.ImageOps.invert(image)
width, height = image.size
shifted_image = Image.new("RGB", (width+35, height))
shifted_image.paste(image, (35, 45))
shifted_image.save('Imagem alterada.jpg' )
