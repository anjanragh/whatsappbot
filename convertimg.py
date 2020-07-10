import imageio
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt


def grayscale(img):
    return np.dot(img[..., :3], [0.299, 0.587, 0.114])


def dodge(front, back):
    result = front*255/(255-back)
    result[result > 255] = 255
    result[back == 255] = 255
    return result.astype('uint8')


img = "http://static.cricinfo.com/db/PICTURES/CMS/263600/263697.20.jpg"
s = imageio.imread(img)
g = grayscale(s)
i = 255-g
b = scipy.ndimage.filters.gaussian_filter(i, sigma=100)
r = dodge(b, g)

plt.imshow(r, cmap="gray")
# plt.show()
plt.imsave('img2.png', r, cmap='gray', vmin=0, vmax=255)
print("Done")
