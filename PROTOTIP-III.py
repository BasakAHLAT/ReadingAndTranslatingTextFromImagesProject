# coding=utf8
import cv2
from langdetect import detect
import pytesseract
from deep_translator import GoogleTranslator
import os

# Pytesseract yolunu belirt
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
os.environ['TESSDATA_PREFIX'] = r"C:\\Program Files\\Tesseract-OCR\\tessdata"

# Görseli al
img = cv2.imread('Images/4.jfif')

# Görseli iyileştir
duzenleme = cv2.fastNlMeansDenoisingColored(img, None, 21, 21, 7, 21)

print("Görsel iyileştirilmesi tamamlandı. Görseli görmek için 1'e, devam etmek için 2'ye basınız!")
secim = int(input("Secim: "))

if secim == 1:
    cv2.imshow('iyileştirilmiş', duzenleme)
    cv2.waitKey()
    secim = 2  # Devam etmesi için artır

if secim == 2:
    print("Okuma yapılıyor..")
    
    # Görselden metin oku
    sonuc = pytesseract.image_to_string(duzenleme, lang="tur")

    # Dil tespiti
    dil = detect(sonuc)
    print("Metnin dili {}'dir.".format(dil))
    print("Tespit edilen metin:\n", sonuc)

    print("\nMetni Türkçeye çevirmek için '1', İngilizceye çevirmek için '2', Fransızcaya çevirmek için '3' yazınız:")
    ceviri = int(input("Seçim: "))

    # Hedef dili belirle
    hedef_dil = ""
    if ceviri == 1:
        hedef_dil = "tr"
    elif ceviri == 2:
        hedef_dil = "en"
    elif ceviri == 3:
        hedef_dil = "fr"
    else:
        print("Geçersiz seçim.")
        exit()

    # Çeviri işlemi
    try:
        translated = GoogleTranslator(source='auto', target=hedef_dil).translate(sonuc)
        print(f"\nÇevrilen metin ({hedef_dil}):\n", translated)
    except Exception as e:
        print("Çeviri sırasında bir hata oluştu:", e)

