# Calisma Kurallari

Bu dosyanin amaci Python ogrenme surecinde neye dikkat edilecegini unutmamaktir.

## Genel Yaklasim

- Once kendin dene, sonra yapay zekadan yardim iste.
- Yapay zekadan direkt cevap almak yerine once ipucu iste.
- Calisan kodu anlamadan bir sonraki konuya gecme.
- Her yeni konudan sonra en az 3 kucuk alistirma yap.
- Hata almaktan cekinme; hata mesajini okumayi ogren.
- Kod yazarken acele etme, once problemi kucuk parcalara ayir.
- Ezberlemek yerine "bu kod neden boyle calisiyor?" sorusunu sor.

## Kod Yazarken Dikkat Edilecekler

- Dosya ve klasör isimleri küçük harfli, İngilizce ve açık olsun.
- Dosya isimlerinde boşluk kullanma; gerekirse alt çizgi kullan.
- Tüm kod İngilizce yazılır: değişken isimleri, fonksiyon isimleri, dictionary anahtarları, dosya ve klasör isimleri İngilizce olmalı. Yorum satırları Türkçe yazılabilir.
- Değişken isimleri anlamlı olsun: `x` yerine `number`, `text`, `total` gibi.
- Aynı kodu tekrar tekrar yazıyorsan fonksiyon kullanmayı düşün.
- `print()` ile ekrana yazdırmak ve `return` ile değer döndürmek farklı şeylerdir.
- Kullanıcıdan gelen `input()` verisinin her zaman string olduğunu unutma.
- Sonsuz döngü yazarken çıkış koşulunu mutlaka düşün.
- Kodun çalışması yetmez; ne yaptığını okuyunca anlayabilmelisin.

## Ogrenme Yontemi

Her konu icin su sirayi takip et:

1. Konuyu oku veya izle.
2. Mevcut ornegi calistir.
3. Ornegi kapatip sifirdan tekrar yaz.
4. Kucuk bir degisiklik yap.
5. Hata alirsan hata mesajini oku.
6. Yapay zekadan sadece ipucu iste.
7. Cozumu bulunca kendi notunu yaz.

## Yapay Zeka Kullanma Kurallari

- "Bana cevabi ver" yerine "bana ipucu ver" de.
- "Kodumu incele ama cozumu hemen yazma" seklinde istekte bulun.
- Anlamadigin satiri tek tek sor.
- Yapay zekanin yazdigi kodu calistirmadan kabul etme.
- Yapay zekadan gelen cevabi kendi cumlelerinle aciklayabiliyorsan konu oturmaya baslamistir.
- Farkli yapay zekaya gecersen once `README.md`, `RULES.md` ve `PROGRESS.md` dosyalarini okut.

## Git ve Dosya Duzeni

- Her konu ve alistirma mumkunse ayri dosyada dursun.
- Ders dosyalari `lessons/` icinde tutulur.
- Alistirmalar `exercises/` icinde tutulur.
- Mini projeler `projects/` icinde tutulur.
- Kisisel notlar `notes/` icinde tutulur.
- Gereksiz IDE veya sistem dosyalarini projeye dahil etmemeye dikkat et.

## Kendini Kontrol Sorulari

- Bu kod hangi problemi cozuyor?
- Bu kodu satir satir aciklayabilir miyim?
- Bu kodda degiskenlerin tipi ne?
- Hangi kisim tekrar ediyor?
- Hangi kisim fonksiyon olabilir?
- Bu kod hatali veri girilirse ne yapar?
- Benzer bir soruyu yardimsiz cozebilir miyim?

## Egzersiz Dosyası Taslağı

Egzersiz dosyaları aşağıdaki formatta yazılır:

- Yorum satırları Türkçe, Türkçe harflerle yazılır
- Kodlar İngilizce değişken/fonksiyon isimleri kullanır
- Referans kod tamamen yorum satırı olarak durur
- "Anlamı:" kısmı kısa olur, açıklama kodla yapılır
- Çizgi (---), "kodunu buraya yaz" gibi ifadeler kullanılmaz

```
# Alıştırma N: Konu başlığı
# Anlamı:
#   variable = value       → ne olduğu
#   variable.method()      → ne yapar
#   print(variable)        → sonucu gösterir
```
