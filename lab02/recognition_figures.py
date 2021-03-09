from create_figures import random_images
import os
from detector import Detector
import imutils
import cv2

if not os.path.exists("create"):
	os.mkdir("create")
if not os.path.exists("recognition"):
	os.mkdir("recognition")

if __name__ == '__main__':
	number = int(input("Quantity images: "))
	random_images(number)
	for i in range(number):
		image = cv2.imread(f"create/image{i}.jpg")
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		blurred = cv2.GaussianBlur(gray, (5, 5), 0)
		thresh = cv2.threshold(blurred, 50, 255, cv2.THRESH_BINARY)[1]
		contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		contours = imutils.grab_contours(contours)
		detector = Detector()
		for j in contours:
			M = cv2.moments(j)
			X = int(M["m10"] / M["m00"])
			Y = int(M["m01"] / M["m00"])
			cv2.drawContours(image, [j], -1, (0, 130, 255), 3)
			cv2.putText(image, detector.detect(j), (X, Y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 130, 255), 2)
		cv2.imwrite(f"recognition/image{i}.jpg", image)
