import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pylab as plt
from scipy.fftpack import dct, idct
from tkinter import Tk
import sys

# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')

def callback():

    # path to images
    path = fd.askopenfilename(initialdir='/Data', title='Select Photo',
                                      filetypes=(('JPG files', '*.jpg'), ('PNG files', '*.png'), ('JPEG files', '*.jpeg')))

    # open image file
    img = Image.open(path)

    # read lena RGB image and convert to grayscale
    im = rgb2gray(img)

    imF = dct2(im)
    im1 = idct2(imF)

    # check if the reconstructed image is nearly equal to the original image
    np.allclose(im, im1)
    # True

    # plot original and reconstructed images with matplotlib.pylab
    plt.gray()
    plt.subplot(131), plt.imshow(img), plt.axis('off'), plt.title(f'Original\n'
                                                                  f'color image', size=12)
    plt.subplot(132), plt.imshow(im), plt.axis('off'), plt.title(f'Original\n'
                                                                 f'gray image', size=12)
    plt.subplot(133), plt.imshow(im1), plt.axis('off'), plt.title(f'Reconstructed image\n'
                                                                  f'(DCT+IDCT)', size=12)
    plt.show()

def quit():
    sys.exit()

# graphic interface
errmsg = 'Error!'
root = Tk()  # pointing root to Tk() to use it as Tk() in program.

root.attributes('-topmost', False)


frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="Click to Open an Image File",
                   command=callback)
slogan.pack(side=tk.LEFT)

root.mainloop()
