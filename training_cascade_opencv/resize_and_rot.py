import cv2
from PIL import Image
import glob

angle90 = 90
angle180 = 180
n = 1


#for filename in glob.glob('/home/kyle/Desktop/450_tute/training_cascade_opencv/images/*.jpg'):
	#image = cv2.imread(filename,0)


image = cv2.imread('/home/kyle/Desktop/450_tute/training_cascade_opencv/pos.png')
# we need to keep in mind aspect ratio so the image does
# not look skewed or distorted -- therefore, we calculate
# the ratio of the new image to the old image
r = 300.0 / image.shape[1]
dim = (300, int(image.shape[0] * r))

# perform the actual resizing of the image and show it
resized = cv2.resize(image, (50, 50))

	#(h,w) = resized.shape[:2]

	#center = (w/2,h/2)
	#scale = 1.0

	#M = cv2.getRotationMatrix2D(center, angle90, scale)
	#rotated90 = cv2.warpAffine(resized, M, (w,h))

	#M = cv2.getRotationMatrix2D(center, angle180, scale)
	#rotated180 = cv2.warpAffine(resized, M, (w,h))

# write the cropped image to disk in PNG format#
cv2.imwrite("/home/kyle/Desktop/450_tute/training_cascade_opencv/re_pos.png", resized)
	#n+=1
	#cv2.imwrite("/home/kyle/Desktop/450_tute/training_cascade_opencv/neg/neg%s.png" % n, rotated90)
	#n+=1
	#cv2.imwrite("/home/kyle/Desktop/450_tute/training_cascade_opencv/neg/neg%s.png" % n, rotated180)
	#n+=1