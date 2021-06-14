# Program To Read video
# and Extract Frames
import cv2
import os
import glob






# Function to extract frames
def FrameCapture(path):
	path2 = "A:\\project\\images\\"
	
	# Path to video file
	vidObj = cv2.VideoCapture(path)

	# Used as counter variable
	count = 0

	# checks whether frames were extracted
	success = 1

	while success:

		# vidObj object calls read
		# function extract frames
		success, image = vidObj.read()

		# Saves the frames with frame-count
		cv2.imwrite(os.path.join(path2 , "frame%d.jpg" % count), image)
		
		
		

		count += 1

if __name__ == '__main__':
	#LandMark()
	# Calling the function
	FrameCapture("A:\\project\\test.mp4")
