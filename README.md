# 📄 ReadingAndTranslatingTextFromImagesProject

Bu proje, görsel içeriklerden metin tanıma (OCR) ve tanınan metinlerin farklı dillere çevrilmesini sağlayan Python tabanlı bir uygulamadır. Uygulama, 2022 yılında Yazılım Mühendisliği Lisans Programı kapsamında, **Mühendislik Projesi II** dersi için geliştirilmiştir.

---

## 🎓 Proje Bilgileri

- **Proje Adı:** ReadingAndTranslatingTextFromImagesProject  
- **Proje Türü:** Lisans Dönem Projesi (Mühendislik Projesi II)  
- **Dönem:** 2021–2022 Bahar Dönemi  
- **Proje Sahibi:** Başak AHLAT  

---

## 🎯 Amaç

Bu projenin amacı, kullanıcıdan alınan görseldeki metni otomatik olarak tanıyıp dilini tespit etmek ve ardından kullanıcı tercihine göre farklı dillere çevirmektir. Uygulama, afet anında veya dil engelinin sorun oluşturduğu durumlarda hızlı bilgi erişimi sağlamayı hedefler.

---

## 🛠 Kullanılan Araçlar

- 💻 Python 3.13  
- 🧠 `pytesseract` – Görselden metin tanıma  
- 🌍 `langdetect` – Metin dili tespiti  
- 🔤 `deep-translator` – Çok dilli çeviri desteği  
- 📷 `OpenCV` – Görsel işleme ve iyileştirme  
- 🖼️ `Tesseract OCR` – OCR motoru (dış bağımlılık)  

---

## 🚀 Proje Özellikleri

- Görsel iyileştirme (gürültü giderme, netleştirme)  
- Türkçe metin tanıma (Tesseract ile OCR)  
- Otomatik dil algılama  
- İngilizce, Türkçe ve Fransızca'ya çeviri seçeneği  
- Komut satırı etkileşimli arayüz

---

## 🧪 Çıktılar

- 📄 Görselden çıkarılan düz metin  
- 🌐 Seçilen dile çevrilmiş metin  
- 🧭 Hangi dilde tanındığı bilgisi  
- 👤 Kullanıcıdan seçim alabilen terminal arayüzü

---

## 💡 Geliştirme Potansiyeli

- 📱 Mobil arayüz ile bütünleştirme  
- 🎙️ Sesli okuma (TTS) entegrasyonu  
- 📂 Toplu görsel işleme desteği  
- ☁️ Bulut tabanlı API ile web entegrasyonu

---

## 📎 Not

Bu proje, **2022 yılında Mühendislik Projesi II** dersi kapsamında, eğitim amacıyla geliştirilmiştir.

🔧 Projeyi çalıştırmadan önce bilgisayarınıza **Tesseract OCR** kurulumunun yapılmış olması ve `"tur.traineddata"` gibi dil dosyalarının Tesseract `tessdata` klasöründe bulunması gerekmektedir.

🧭 Windows kullanıcıları için `TESSDATA_PREFIX` ortam değişkeni doğru şekilde ayarlanmalıdır.
