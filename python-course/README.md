# Python Course

Bu proje Python ogrenme surecini duzenli, takip edilebilir ve yapay zeka ile devam ettirilebilir hale getirmek icin tutulur.

Baslangictaki kodlar bir YouTube egitim videosu takip edilerek yazilmistir. Bundan sonraki amac sadece video izlemek degil, konulari anlayarak tekrar etmek, alistirma cozmek, hata ayiklamak ve zamanla kucuk projeler gelistirmektir.

## Bu Projede Ne Yapmaya Calisiyoruz?

- Python temellerini saglamlastirmak.
- Derslerde yazilan kodlari konu basliklarina gore duzenlemek.
- Her konu icin alistirma ve tekrar alani olusturmak.
- Yapay zekayi dogru sekilde kullanarak ogrenmeyi hizlandirmak.
- Sadece cevabi almak yerine problemi anlamayi ogrenmek.
- Zamanla kucuk projeler yaparak bilgiyi uygulamaya cevirmek.

## Klasor Yapisi

```text
lessons/
  01_basics/
  02_control_flow/
  03_collections/
  04_functions/
  05_modules/

exercises/
projects/
notes/

RULES.md
PROGRESS.md
README.md
```

## Klasorlerin Amaci

`lessons/` derslerde yazilan ornek kodlari tutar.

`exercises/` konu alistirmalari icin kullanilir. Buradaki dosyalar daha cok "kendin cozmeyi dene" mantigindadir.

`projects/` kucuk ama calisan uygulamalar icindir. Ornek: hesap makinesi, sayi tahmin oyunu, todo uygulamasi.

`notes/` kisisel notlar, tekrarlar ve ogrenme gunlukleri icindir.

`RULES.md` calisirken dikkat edilmesi gereken kurallari tutar.

`PROGRESS.md` temel, orta ve ileri seviye konu takibini tutar.

## Yapay Zeka Icin Baglam

Bu projeye bakan bir yapay zeka once su dosyalari okumalidir:

1. `README.md`
2. `RULES.md`
3. `PROGRESS.md`

Bu dosyalar okunduktan sonra yapay zeka su yaklasimi takip etmelidir:

- Ogrenci baslangic seviyesindedir.
- Cevaplar detayli ama sade anlatilmalidir.
- Kod direkt verilmeden once mantik anlatilmalidir.
- Mumkunse once ipucu verilmeli, sonra cozum gosterilmelidir.
- Ogrencinin kendi kodu incelenmeli, hatalar satir satir aciklanmalidir.
- Kisa vadeli hedef temel Python konularini saglamlastirmaktir.
- Uzun vadeli hedef kucuk projeler gelistirebilecek seviyeye gelmektir.

## Calisma Sekli

Bir konu calisilirken onerilen sira:

1. Ilgili ders dosyasini oku.
2. Kodu calistir.
3. Kodun ne yaptigini kendi cumlelerinle acikla.
4. Ayni ornegi kapatip yeniden yaz.
5. `exercises/` klasorunde benzer alistirmalar coz.
6. Hata alirsan hata mesajini incele.
7. Takildigin yerde yapay zekadan ipucu iste.
8. Konu tamamlaninca `PROGRESS.md` dosyasinda ilgili kutuyu isaretle.

## Mevcut Ders Dosyalari

```text
lessons/01_basics/01_hello_world.py
lessons/01_basics/02_numbers.py
lessons/01_basics/03_strings.py

lessons/02_control_flow/01_if_else.py
lessons/02_control_flow/02_for_while.py

lessons/03_collections/01_lists.py
lessons/03_collections/02_tuples_sets.py
lessons/03_collections/03_dictionaries.py

lessons/04_functions/01_functions.py
lessons/04_functions/02_input_exercises.py

lessons/05_modules/01_modules.py
lessons/05_modules/02_random_module.py
lessons/05_modules/03_time_module.py
lessons/05_modules/04_datetime_module.py
lessons/05_modules/05_os_module.py

notes/general_repetition.py
```

## Onemli Not

Bu projede amac hizli ilerlemek degil, temeli oturtmaktir. Bir konuyu anlamadan gecmek daha sonra daha fazla zorlanmaya neden olur. Bu yuzden kucuk alistirmalar, tekrar ve hata ayiklama bu projenin ana parcasidir.
