import cv2 
import numpy as np

#carregando a imagem
img = cv2.imread("images//all_souls_000003.jpg", cv2.IMREAD_GRAYSCALE)
#mostrando imagem
cv2.imshow("Imagem Original", img)

#gerando a I'
imgGeradaX = np.ones((img.shape[0],img.shape[1],1),np.uint8)*255
for i in range(imgGeradaX.shape[0]):
    for j in range(imgGeradaX.shape[1]):
        if j <= 255:
            imgGeradaX[i, j, 0] = j
        else:
            imgGeradaX[i, j, 0] = 255
cv2.imshow("Imagem Gerada X",imgGeradaX)

#gerando a I''
imgGeradaY = np.ones((img.shape[0],img.shape[1],1),np.uint8)*255
for i in range(imgGeradaY.shape[0]):
    for j in range(imgGeradaY.shape[1]):
        if i <= 255:
            imgGeradaY[i, j, 0] = i
        else:
            imgGeradaY[i, j, 0] = 255
cv2.imshow("Imagem Gerada Y",imgGeradaY)

#somando imagens
imgFinal = cv2.add(img, imgGeradaX)
imgFinal = cv2.add(imgFinal, imgGeradaY)

#mostrando imagem final
cv2.imshow("Imagem Final", imgFinal)
cv2.waitKey()

cv2.imwrite("results//ex03.jpg", imgFinal)