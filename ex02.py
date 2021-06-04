import cv2 
import numpy as np

#carregando a imagem
img = cv2.imread("images//all_souls_000003.jpg", cv2.IMREAD_GRAYSCALE)
#mostrando imagem
cv2.imshow("Imagem Original", img)

#gerando a I''
imgGerada = np.ones((img.shape[0],img.shape[1],1),np.uint8)*255
for i in range(imgGerada.shape[0]):
    for j in range(imgGerada.shape[1]):
        if i <= 255:
            imgGerada[i, j, 0] = i
        else:
            imgGerada[i, j, 0] = 255
cv2.imshow("Imagem Gerada",imgGerada)

#somando imagens
imgFinal = cv2.add(img, imgGerada)

#mostrando imagem final
cv2.imshow("Imagem Final", imgFinal)
cv2.waitKey()

cv2.imwrite("results//ex02.jpg", imgFinal)