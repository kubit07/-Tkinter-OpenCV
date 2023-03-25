import cv2

# Chargement de l'image
img = cv2.imread("G:\M2\INFO0803\ProjetOpenCV\Project\Tkinter_OpenCV\icon.png")

# Augmentation de la luminosité
brightness = 100
adjusted = cv2.convertScaleAbs(img, beta=brightness)

# Affichage de l'image originale et de l'image ajustée
cv2.imshow("Original", img)
cv2.imshow("Adjusted", adjusted)
cv2.waitKey(0)