import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('Lena.png')

plt.imshow(img)
plt.show()