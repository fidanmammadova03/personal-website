1) Install / import
pip install opencv-python
pip install numpy scipy
pip install pillow
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter
import scipy.ndimage
________________________________________
2) Read / open image
img = cv2.imread("image.jpg")
img = cv2.imread("image.jpg", 0)
img = Image.open("image.jpg")
________________________________________
3) Show / save / basic image info
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("out.jpg", img)
plt.imshow(img)
plt.show()
print(img.shape)
print(img.size)
________________________________________
4) Color conversion / grayscale
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
________________________________________
5) Resize / rotate / flip / invert
resized = cv2.resize(img, (new_width, new_height))
rot1 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rot2 = cv2.rotate(img, cv2.ROTATE_180)
rot3 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
flip_v = cv2.flip(img, 0)
flip_h = cv2.flip(img, 1)
invert_img = cv2.bitwise_not(img)
________________________________________
6) OpenCV filtering with kernels
identity
image = cv2.imread("test.jpg")
kernel1 = np.array([[0,0,0],
                    [0,1,0],
                    [0,0,0]])
identity = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
custom blur
kernel2 = np.ones((5,5), np.float32) / 25
blur_kernel = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)
sharpen
kernel3 = np.array([[0,-1,0],
                    [-1,5,-1],
                    [0,-1,0]])
sharp_img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel3)
________________________________________
7) OpenCV blur methods
normal blur
img_blur = cv2.blur(src=image, ksize=(5,5))
gaussian blur
gaussian_blur = cv2.GaussianBlur(src=image, ksize=(5,5), sigmaX=0, sigmaY=0)
median blur
median = cv2.medianBlur(src=image, ksize=5)
________________________________________
8) Pillow filtering
base pattern
img = Image.open("Flower.jpg")
result = img.filter(ImageFilter.BLUR)
result.show()
non-parameterized filters listed
ImageFilter.BLUR
ImageFilter.CONTOUR
ImageFilter.DETAIL
ImageFilter.EDGE_ENHANCE
ImageFilter.EDGE_ENHANCE_MORE
ImageFilter.EMBOSS
ImageFilter.FIND_EDGES
ImageFilter.SHARPEN
ImageFilter.SMOOTH
ImageFilter.SMOOTH_MORE
BoxBlur
blurred_img = img.filter(ImageFilter.BoxBlur(radius=3))
GaussianBlur
gauss_blurr_img = img.filter(ImageFilter.GaussianBlur(radius=2))
gauss_blurr_img = img.filter(ImageFilter.GaussianBlur(radius=3))
Emboss
emboss_img = img.filter(ImageFilter.EMBOSS)
Kernel
edge_detector = np.array([[0,-1,0],
                          [-1,4,-1],
                          [0,-1,0]])
kernel_img = img.filter(ImageFilter.Kernel(size=(3,3),
                                           kernel=edge_detector.flatten(),
                                           scale=0.2))
RankFilter
rank_img = img.filter(ImageFilter.RankFilter(size=3, rank=4))
rank_img = img.filter(ImageFilter.RankFilter(size=3, rank=8))
parameterized filters listed
ImageFilter.UnsharpMask
ImageFilter.Kernel
ImageFilter.RankFilter
ImageFilter.MedianFilter
ImageFilter.MinFilter
ImageFilter.MaxFilter
________________________________________
9) Morphological operations
erosion + dilation
img = cv2.imread("Image.png", 0)
kernel = np.ones((5,5), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)
opening + closing
img = cv2.imread("noisy_image.jpg", 0)
kernel = np.ones((5,5), np.uint8)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
morphology flow from notes
gray/binary image -> thresholding -> erosion/dilation -> opening/closing
________________________________________
10) Edge detection
Canny
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
canny_edges = cv2.Canny(gray_image, 120, 150)
or
edges = cv2.Canny(image, 100, 200)
Laplacian
lap_edges = cv2.Laplacian(gray_image, cv2.CV_64F)
lap_edges = np.uint8(np.absolute(lap_edges))
or
laplacian = cv2.Laplacian(gray, cv2.CV_64F)
Sobel
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0)
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1)

sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))
or with kernel size:
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
________________________________________
11) Feature extraction / Harris corner
Harris corner full code
import numpy as np
import cv2 as cv

filename = "chessboard.png"
img = cv.imread(filename)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv.cornerHarris(gray, 2, 3, 0.04)
dst = cv.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0,0,255]

cv.imshow("dst", img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
Harris arguments
cv.cornerHarris(gray, blockSize, ksize, k)
feature extraction flow from notes
1. grayscale
2. Gaussian filter for noise
3. Sobel x and y gradients
4. compute Harris value
5. threshold + local maxima
6. compute descriptor
________________________________________
12) Very short topic map
read image
-> convert color / gray
-> resize / rotate / flip / invert
-> blur / sharpen / filter
-> threshold if needed
-> erosion / dilation / opening / closing
-> edge detection
-> corner / feature extraction
-> display / save
Based on the uploaded lecture set overall. 
If you want, next I can make it even tighter into exam-night version: only function names + one-line use.

