# Chat Room Uygulamasý

Bu uygulama, yerel bir að üzerinden çoklu kullanýcýlarýn iletiþim kurmasýný saðlayan bir sohbet odasýdýr. Kullanýcýlar, sunucuya baðlanarak mesaj gönderip alabilirler.

## Özellikler

- Çoklu kullanýcý desteði
- Anlýk mesajlaþma
- Kullanýcýlarýn baðlandýklarýnda hoþ geldin mesajý

## Gereksinimler

- Python 3.x
- `socket` ve `threading` kütüphaneleri (Python ile birlikte gelir)

## Kurulum

1. Bu repo'yu bilgisayarýnýza indirin:
   ```bash
   git clone https://github.com/kullanici_adiniz/repo_adi.git
   cd repo_adi
Sunucu ve istemci dosyalarýný çalýþtýrmadan önce, aþaðýdaki adýmlarý izleyin:
Kullaným
Sunucu
Sunucuyu baþlatmak için terminalde þu komutu çalýþtýrýn:

bash
Kodu kopyala
python chat_server.py [IP_adresi] [Port]
Örnek:

bash
Kodu kopyala
python chat_server.py 192.168.1.105 8081
Sunucu, belirtilen IP adresinde ve portta dinlemeye baþlayacaktýr. Terminalde baðlý kullanýcýlarý görebilirsiniz.

Ýstemci
Ýstemciyi baþlatmak için ayrý bir terminal penceresi açýn ve þu komutu çalýþtýrýn:

bash
Kodu kopyala
python client.py [IP_adresi] [Port]
Örnek:

bash
Kodu kopyala
python client.py 192.168.1.105 8081
Baðlandýktan sonra, mesajýnýzý yazýp Enter tuþuna basarak gönderebilirsiniz.

Kullaným Notlarý
Her istemci, baðlandýklarýnda sunucudan bir "Hoþ geldin" mesajý alýr.
Mesajlar, diðer baðlý istemciler tarafýndan görülebilir.
Baðlantý kesilirse, istemci otomatik olarak kapanýr.
Katkýda Bulunanlar
Adýnýz
Lisans
Bu proje, MIT Lisansý altýnda lisanslanmýþtýr.

markdown
Kodu kopyala

### Açýklamalar:

1. **Baþlýk ve Açýklama**: Projenizin adý ve kýsa bir açýklamasý.
2. **Özellikler**: Uygulamanýzýn sunduðu özellikler.
3. **Gereksinimler**: Hangi yazýlýmlara ihtiyaç duyulduðu.
4. **Kurulum**: Projeyi nasýl indireceðinize dair adýmlar.
5. **Kullaným**: Sunucu ve istemci nasýl baþlatýlýr, örnek komutlar.
6. **Kullaným Notlarý**: Kullaným hakkýnda dikkat edilmesi gereken noktalar.
7. **Katkýda Bulunanlar**: Eðer bir ekip ile çalýþtýysanýz, katkýda bulunanlarý belirtebilirsiniz.
8. **Lisans**: Projenizin lisans bilgisi.

