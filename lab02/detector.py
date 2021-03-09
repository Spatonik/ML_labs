import cv2


class Detector:
    def __init__(self):

        pass

    @staticmethod
    def detect(cont):
        perimeter = cv2.arcLength(cont, True)
        approx = cv2.approxPolyDP(cont, 0.04 * perimeter, True)
        if len(approx) == 3:
            shape = "triangle"
        elif len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            if 0.95 <= w / float(h) <= 1.05:
                shape = "square"
            else:
                shape = "rectangle"
        elif len(approx) == 5:
            shape = "pentagon"
        else:
            shape = "circle"
        return shape
