[README.md](https://github.com/user-attachments/files/26186266/README.md)
# Sentetik Sağlık Verisi Üretimi ve Görselleştirme Projesi

Bu proje, Python kullanılarak belirli istatistiksel özelliklere sahip sentetik bir sağlık veri setinin oluşturulması ve ardından bu verilerin dağılımlarının görselleştirilmesi amacıyla hazırlanmıştır.

## Proje İçeriği

Proje iki temel Python dosyasından ve üretilen bir veri kümesinden oluşmaktadır:

1.  **`data_generate.py`**: Sentetik veri üretimi işlemlerini gerçekleştiren Python kodudur.
2.  **`visualize.py`**: Üretilen veri setini okuyarak, değişkenlerin histogram grafiklerini çizen Python kodudur.
3.  **`veri.csv`**: `data_generate.py` çalıştırıldıktan sonra oluşan veri setidir.

## Veri Setinin Özellikleri

Veri seti (`veri.csv`), **500 satırdan (gözlem)** ve aşağıdaki **2 değişkenden** oluşmaktadır:

*   **KanSekeri (Kan Şekeri):** Normal dağılıma sahip olup, ortalaması ($\mu$) 100 ve standart sapması ($\sigma$) 15 olacak şekilde rastgele üretilmiştir.
*   **Tansiyon:** Normal dağılıma sahip olup, ortalaması ($\mu$) 120 ve standart sapması ($\sigma$) 10 olacak şekilde rastgele üretilmiştir.

Daha gerçekçi bir görünüm elde etmek amacıyla değerler, ondalıklı sayıların virgülden sonraki ilk hanesine göre yuvarlanmıştır.

## Kullanılan Teknolojiler ve Kütüphaneler

*   **Python 3.x**
*   **NumPy (`numpy`)**: Normal dağılıma sahip sentetik verilerin matematiksel olarak üretilmesi için.
*   **Pandas (`pandas`)**: Üretilen verilerin tablo yapısına (DataFrame) dönüştürülmesi ve CSV formatında dışa aktarılması ile CSV dosyasının okunması için.
*   **Matplotlib (`matplotlib.pyplot`)**: Kan Şekeri ve Tansiyon verilerinin histogram grafiklerinin çizilmesi için.

## Kurulum ve Çalıştırma Talimatları

Projeyi çalıştırmak için öncelikle gerekli kütüphanelerin yüklü olduğundan emin olunuz:
```bash
pip install pandas numpy matplotlib
```

### 1. Veri Üretimi
İlk adım olarak sentetik veri setini oluşturmak için terminal veya komut satırınızda aşağıdaki komutu çalıştırınız:
```bash
python data_generate.py
```
Bu işlem sonucunda aynı dizin içerisinde `veri.csv` adlı dosya oluşturulacaktır. Komut satırında verilerin kısa bir özeti (veri sayısı ve ilk 5 satır) görüntülenecektir.

### 2. Veri Görselleştirme
`veri.csv` dosyası oluşturulduktan sonra, verilerin dağılımını grafik üzerinde incelemek için aşağıdaki komutu çalıştırınız:
```bash
python visualize.py
```
Bu script, her iki değişkenin ortalama ve standart sapma değerlerini teyit edebileceğiniz iki farklı histogram grafiğini ekranda açacaktır.

## Not
Görselleştirme scriptinin (`visualize.py`) düzgün çalışabilmesi için önce veri üretim scriptinin (`data_generate.py`) çalıştırılarak `veri.csv` dosyasının yaratılmış olması zorunludur.
