# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 10:47:22 2022

@author: sayem

Amaç Birinci resmin üzerine ikinci resmi koymak

Birinci resim: Caption resmi

İkinci resim cv2.png
"""

import cv2
import matplotlib.pyplot as plt

imageOfCv2 = cv2.imread("cv2.png")
imageOfCaption = cv2.imread("caption.jpg") 
imageOfCaption[0:0, 0:0] = [255, 255, 255]

cv2.imshow("-1 ORJINAL",imageOfCaption)
cv2.imshow("-2 ORJINAL",imageOfCv2)
#plt.imshow( imageOfCaption)
cv2Width, cv2Height, _ = imageOfCv2.shape

croppedAreaOfCaption = imageOfCaption[0:cv2Width, 0:cv2Height]
#print(cv2Width, cv2Height)

cv2.imshow("1 USTE GETIRILECEK RESIM KADAR, ISLEM YAPILACAK ALANI KES", croppedAreaOfCaption)


grayOfCv2 = cv2.cvtColor(imageOfCv2, cv2.COLOR_BGR2GRAY)

cv2.imshow("2 USTE GETIRILECEK RESMI GRIYE CEVIR", grayOfCv2)


#plt.imshow( imageOfCaption)

ret, maskOfGrayCv2 = cv2.threshold(grayOfCv2, 28, 255, cv2.THRESH_BINARY)

cv2.imshow("3 THRESHOLD UYGULA YANI 28 TONUNDAN BUYUKLERI 255-BEYAZ YAP", maskOfGrayCv2)


"""
threshold ile belirli bir renk tonunun üzerindekileri belirli bir renk tonuna çevir diyebiliyoruz
cv2.threshold(a, b, c, d)

a: hedef resim
b: bul (yüksek) renk tonu
c çevrilecek renk tonu
d tip
"""


invOfMaskedCv2 = cv2.bitwise_not(maskOfGrayCv2) # TERSİNİ AL


cv2.imshow("4 TERSINI AL ",invOfMaskedCv2)

#test = cv2.bitwise_not(invOfMaskedCv2, invOfMaskedCv2, mask = imageOfCv2)




cross = cv2.bitwise_and(croppedAreaOfCaption, croppedAreaOfCaption, mask = invOfMaskedCv2) # ÇARP
 
cv2.imshow("5", cross) # SİYAH OPEN CV LOGOSUNU CAPTION ÜSTÜNE GETİRDİK

#imageOfCaption[0:cv2Width,0:cv2Height] = cross

#cv2.imshow("5 imageOfCaption",imageOfCaption)

#cross2 = cv2.bitwise_and(imageOfCv2, imageOfCv2, mask = maskOfGrayCv2)
#cv2.imshow("bu ne ", cross2);
toplam = cv2.add(cross, imageOfCv2) # TOPLA

cv2.imshow("6 TOPLAM",toplam)

imageOfCaption[0:cv2Width, 0:cv2Height] = toplam
cv2.imshow("7 SONUC", imageOfCaption)


cv2.waitKey(0)
cv2.destroyAllWindows()
plt.close('all')