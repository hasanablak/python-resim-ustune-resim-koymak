OpenCV

Resimleri üst üste getirmek

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.001.png)![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.002.png) +

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.003.png) = 



Teşekkür;

Bana bunu öğrettiği için değerli Mustafa Ünlü’ye teşekkür ederim.

Youtube video linki;

[Tıkla Git](https://www.youtube.com/watch?v=gMpBJ7YBxTY)

Bilmemiz gerekenler;

1) Resimlerde temelde renk kodu olarak; Red, Green ve Blue bulunur
1) Cv2 resimleri Green, Blue, Red olarak okur
1) Matplotlib.pyplot ise Red, Green, Blue olacak şekilde okur
1) Resimler matrislerden oluşur her piksel 3 indisli bir matristir yani her pikselde R G B kanalları bulunur bu kanallardan baskın olma durumunu 0’dan 255’e kadar olan sayılarla belirleriz

Yani; bir pikselin sadece kırmızı olmasını istersek renk kodu olarak; 255 000 000 vermemiz gerekir, sadece mavi olmasını istiyorsak, 000 000 255 vermemiz gerekir.

1) Bilgisayarda bitler arasında çarpma ve toplama işlemi aşağıdaki gibidir

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.004.png)


# Kütüphaneleri dahil edelim

Öncelikle kullanacağımız kütüphaneleri projeye dahil edelim

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.005.png)
# Görselleri dahil edelim
Kullanacağımız görselleri projeye dahil edelim

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.006.png)

Göstermek gerekirse

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.007.png)


# Tanımları oturtalım
Üzerine koyacağımız resim: imageOfCaption

Üzerine koyulacak resim: imageOfCv2


# Kesme/Kırpma İşlemi
![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.008.png)

Kız kulesi resmini(caption.jpg | imageOfCaption ), 

OpenCV logosu(cv2.png | imageOfCv2) alanı kadar kırpalım

imageOfCv2.shape diyerek imageOfCv2’nin yükseklik ve genişlik değerlerini aldık.

croppedAreaOfCaption içerisine ise, 

imageOfCaption resminin X düzleminden 0. Koordinattan, imageOfCv2’nin genişliği kadar ve imageOfCaption resminin Y düzleminden 0. Koordinattan, imageOfCv2’nin yüksekliği kadar kesilmiş hali bulunuyor.

Yani; kırmızı ile gösterilmiş alan kadar kesilecek

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.009.png)![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.010.png)

Göstermek gerekirse:


# Griye Çevirmek
![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.011.png)

Cv2(imageOfCv2) logomuzu gri tonlamaya çevireceğiz, bunu yapma sebebimiz, threshold uygulayarak arkaplandaki siyah alandan komple kurtulmak

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.012.png)


# Maskeleme işlemi Threshold
En önemli adımlardan bir tanesi olan bu adımda; cv2 içerisindeki threshold metodunu, belirli bir renk tonunun üstündeki tonları başka bir renk tonuna çevirmek için kullanacağız.

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.013.png)

grayOfCv2 resmindeki 28 tonunun üstündeki bütün renk tonlarını 255’e çevir dedik.

![C:\Users\sayem\Desktop\Resimleri üst üste getirme\font bulma.png](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.014.png)Bunu neden yaptık?

` `Yan tarafta gözükeceği gibi 

Cv2 logosu içerisindeki en çok siyaha yakın olan rengimiz ok ile işaret ettiğim şekilde bulunuyor bu renk tonunu da sağ üst tarafta görebiliriz.

Bu durumda 28 renk tonunun üstündeki bütün renkleri beyaza çevirirsek aşağıdaki görseli elde edebilriz

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.015.png)
# Rengi tersine çevirmek
![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.016.png)

Göstermek gerekirse;

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.017.png)Bu işlemi neden yaptık?

Beyaz, renk kodu olarak 255 tekabul eder.

Siyah ise 0’a. Beyaz’ın 1, Siyahın ise 0 olduğunu düşünecek olursak, ilk başta bilinmesi gerekenler klavuzunda 1 ile 0’u çarptığımızda 0 sonucunu elde edeceğiz. Yani yan taraftaki görüntü ile başka bir görüntüyü bit çarpımı yaparsak, arkaplandaki görüntü beyaz yani 1 olacağından; diğer görüntüdeki aynı alandaki piksellerin renklerini alacaktır.

Bunu şu şekilde de anlatmak mümkün;

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.018.png)Beyaz olan kısmın heryerinde 1 olduğunu ( 1 = 255,255,255 varsayarsak) düşünelim.

Bu 1 ile 0’ı çarptığımızda 0 sonucunu elde ederiz.

255 ile başka bir renk tonunu çarparsak

Diğer renk tonuna eşit olur

255 \* 120 = 30600;

30600 MOD 255 = 120;

Bu durumda da 1 olan kısımlar (yani arkaplanı beyaz olan kısımlar) çarpıldığı piksellerin rengini alacaktır.


# Pikselleri çarpma

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.019.png)

**Kırpma işlemi** adımında caption üzerinden bi kısım kırpma işlemi yapmıştık şimdi kırptığımız resimdeki pikseller ile elimizde tersini aldığımız görseli çarpacağız

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.020.png)![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.021.png)\*

ÇARP



Açıklama: 1. Resim ile 2. Resmi bit çarpımı yaptık, 2.resimde beyaz olan yerlerin 1(255) olarak ifade etmiştik, 1. Resimde de, 2. Resimdeki beyaz piksellerin denk geldiği piksellerin farklı renk tonlarında olması ile birlikte çarpma işleminde 1 ile neyi çarparsak çarpıldığı değer’e eşit olacağından arkplanın piksellerinin reklerini(RGB) almış oldu.

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.022.png)
# Pikselleri toplama işlemi
Yine önemli adımlardan bir tanesi olan bu adımımızda **Pikselleri Çarpma Başlığında** oluşturuduğumuz pikseller ile, orjinal open cv logosunun piksellerini TOPLAMA işlemi yapacağız.

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.023.png)![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.024.png)

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.025.png) 							+

`						`TOPLA




![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.026.png)Toplama işlemi sonucunda yan taraftaki görüntüyü elde ederiz.

Açıklama;

6.adımdaki yaptığımız işlemde open cv logosunun siyah olan kısımlarının(piksellerini) 0 olarak ifade edelim (0,0,0). Orjinal open cv logosunda ise siyah olan kısımlar yine 0, renkli olan kısımlar ise 1 olduğunu düşünelim. En başta bit işlem toplama tablosunda toplama işleminde 0 ile 1 toplam sonucu 1’e eşit olacağından, siyah olan kısımlar renklendirilmiş oldu.

Bunu şu şekilde de anlatalım;

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.027.png)Orjinal open cv resmini şu şekilde düşünebiliriz;

Siyah kısımlar 0, renkli kısımlar ise 1 olacak şekilde.

Tabiki renkli kısımların kendine ait renk kodları var ama biz kolay anlaşılsın diye 1 olarak ifade ediyoruz. Siyah kısımlar ise gerçekten de renk kodu olarak 0, 0, 0’a rekabul etmektedir.




![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.028.png)

**Pikselleri çarpma başlığında** elde ettiğimiz görüntünün yine yukarıda anlattığımız gibi düşünecek olursak, yani siyah kısımlarının 0, renkli kısımlarının ise 1 olduğunu varsayar isek. Şu şekilde düşünebiliriz.


![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.029.png)


**Renkli bir bit ile renksiz bir bitin toplamı Renkli bite eşit olur(bitler arasında toplama işlemi)** bu durumda da yandaki görüntüyü elde ederiz.


# Yerleştirme
**Pikselleri toplama** başlığında ettiğimiz görüntüyü(pikselleri), **kırpma adımında** kestiğimiz kısma yerleştireceğiz

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.030.png)

![](Aspose.Words.eb91cce8-9e01-4255-920a-b0ffc8ed1cdd.031.png)
