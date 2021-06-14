# import the necessary packages
from imutils import face_utils
import dlib
import cv2
import os
# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)


 

count =0
path2 = "A:\\project\\images"
for image_path in os.listdir(path2):
	input_path = os.path.join(path2, image_path)
	img = cv2.imread(input_path)
	gray = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
	rects = detector(gray, 0)
	for (i, rect) in enumerate(rects):
			shape = predictor(gray, rect)
			shape = face_utils.shape_to_np(shape)
		
			# loop over the (x, y)-coordinates for the facial landmarks
			# and draw them on the image
			for (x, y) in shape:
				cv2.circle(img, (x, y), 2, (0, 255, 0), -1)
			
	path1 = "A:\\project\\output"
	cv2.imwrite(os.path.join(path1 , "frame%d.jpg" % count), img)
	count +=1

