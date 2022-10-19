import cv2
img=cv2.imread("solar-system.jpg")

cv2.putText(img,
"Mercury",
(100,150),
fontFace=cv2.AGAST_FEATURE_DETECTOR_AGAST_7_12S,
fontScale=0.5,
color=(0,200,23))

cv2.putText(img,
"Venus",
(200,300),
fontFace=cv2.AGAST_FEATURE_DETECTOR_AGAST_7_12S,
fontScale=0.5,
color=(0,200,23))

cv2.putText(img,
"Earth",
(300,150),
fontFace=cv2.AGAST_FEATURE_DETECTOR_AGAST_7_12S,
fontScale=0.5,
color=(0,200,23))

cv2.putText(img,
"Mars",
(380,300),
fontFace=cv2.AGAST_FEATURE_DETECTOR_AGAST_7_12S,
fontScale=0.5,
color=(0,200,23))

cv2.putText(img,
"Jupiter",
(600,50),
fontFace=cv2.AGAST_FEATURE_DETECTOR_AGAST_7_12S,
fontScale=0.5,
color=(0,200,23))

cv2.putText(img,
"Saturn",
(780,350),
fontFace=cv2.AGAST_FEATURE_DETECTOR_AGAST_7_12S,
fontScale=0.5,
color=(0,200,23))

cv2.putText(img,
"Uranus",
(950,100),
fontFace=cv2.AGAST_FEATURE_DETECTOR_AGAST_7_12S,
fontScale=0.5,
color=(0,200,23))

cv2.putText(img,
"Neptune",
(1100,300),
fontFace=cv2.AGAST_FEATURE_DETECTOR_AGAST_7_12S,
fontScale=0.5,
color=(0,200,23))
cv2.imshow("tuptuo",img)
cv2.waitKey(0)