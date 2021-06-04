import cv2 
import numpy as np

def Translacao(img, dx, dy):
    imgTrans = np.ones((img.shape[0],img.shape[1],1),np.uint8)*255
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            f = round(i - dy)
            g = round(j - dx)
            if f >= img.shape[0] or f <= 0 or g >= img.shape[1] or g <= 0:
                # imgTrans[round(i - dx), round(j - dy)] = 0 
                imgTrans[i, j] = 0
            else:
                # imgTrans[round(i - dx), round(j - dy)] = img[i, j]
                imgTrans[i, j] = img[f, g]
    return imgTrans

def Rotacao(img, angulo):
    imgRot = np.ones((img.shape[0],img.shape[1],1),np.uint8)*255
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            f = round(i*np.cos(angulo) - j*np.sin(angulo))
            g = round(i*np.sin(angulo) + j*np.cos(angulo))
            # print(f, g)
            if f >= img.shape[0] or f <= 0 or g >= img.shape[1] or g <= 0:
                imgRot[i, j] = 0
            else:
                imgRot[i, j] = img[f, g]
    return imgRot

def Escala(img, sx, sy):
    imgEsc = np.ones((img.shape[0],img.shape[1],1),np.uint8)*255
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            f = round(i/sy)
            g = round(j/sx)
            # print(f, g)
            if f >= img.shape[0] or f <= 0 or g >= img.shape[1] or g <= 0:
                imgEsc[i, j] = 0
            else:
                imgEsc[i, j] = img[f, g]
    return imgEsc

def Cisalha(img, cv, ch):
    imgCis = np.ones((img.shape[0],img.shape[1],1),np.uint8)*255
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            f = round(i - j*cv)
            g = round(j - i*ch)
            # print(f, g)
            if f >= img.shape[0] or f <= 0 or g >= img.shape[1] or g <= 0:
                imgCis[i, j] = 0
            else:
                imgCis[i, j] = img[f, g]
    return imgCis

#abrindo imagem
img = cv2.imread("images//all_souls_000003.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Imagem Original", img)
imgTrans = Translacao(img, 100.3, 150.8)
imgRot = Rotacao(img, np.pi/4.)
imgEsc = Escala(img, 0.75, 1.25)
# imgCis = Cisalha(img, 0.25, 0.1)
imgCis = Cisalha(img, 0, 0.25)

cv2.imshow("Resultado Translacao", imgTrans)
cv2.imshow("Resultado Rotacao", imgRot)
cv2.imshow("Resultado Escala", imgEsc)
cv2.imshow("Resultado Cisalhamento", imgCis)

cv2.imwrite("results//ex04Translacao.jpg", imgTrans)
cv2.imwrite("results//ex04Rotacao.jpg", imgRot)
cv2.imwrite("results//ex04Escala.jpg", imgEsc)
cv2.imwrite("results//ex04Cisalhamento.jpg", imgCis)

cv2.waitKey()