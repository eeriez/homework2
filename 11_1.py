import requests
from PIL import Image
import numpy

# requests

res = requests.head('https://www.wikipedia.org/')
res = requests.options('https://www.wikipedia.org/')
res = requests.get('https://www.wikipedia.org/')

# pillow

with Image.open("5efc2686-09fb-40c9-a12a-39860047a88e.png") as im:
    im.rotate(135).show()
    im.resize((600, 500))

# numpy

Z = numpy.zeros(10)
print(Z)
Z = numpy.full(10, 2.5)
print(Z)

Z = numpy.zeros((8,8), dtype=int)
Z[1::2, ::2] = 1
Z[::2, 1::2] = 1
print(Z)

