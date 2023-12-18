from PIL import Image
import pilgram

im = Image.open('sample.jpg')
pilgram.toaster(im).save('sample-aden.jpg')