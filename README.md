# Chat Room Uygulamas�

Bu uygulama, yerel bir a� �zerinden �oklu kullan�c�lar�n ileti�im kurmas�n� sa�layan bir sohbet odas�d�r. Kullan�c�lar, sunucuya ba�lanarak mesaj g�nderip alabilirler.

## �zellikler

- �oklu kullan�c� deste�i
- Anl�k mesajla�ma
- Kullan�c�lar�n ba�land�klar�nda ho� geldin mesaj�

## Gereksinimler

- Python 3.x
- `socket` ve `threading` k�t�phaneleri (Python ile birlikte gelir)

## Kurulum

1. Bu repo'yu bilgisayar�n�za indirin:
   ```bash
   git clone https://github.com/kullanici_adiniz/repo_adi.git
   cd repo_adi
Sunucu ve istemci dosyalar�n� �al��t�rmadan �nce, a�a��daki ad�mlar� izleyin:
Kullan�m
Sunucu
Sunucuyu ba�latmak i�in terminalde �u komutu �al��t�r�n:

bash
Kodu kopyala
python chat_server.py [IP_adresi] [Port]
�rnek:

bash
Kodu kopyala
python chat_server.py 192.168.1.105 8081
Sunucu, belirtilen IP adresinde ve portta dinlemeye ba�layacakt�r. Terminalde ba�l� kullan�c�lar� g�rebilirsiniz.

�stemci
�stemciyi ba�latmak i�in ayr� bir terminal penceresi a��n ve �u komutu �al��t�r�n:

bash
Kodu kopyala
python client.py [IP_adresi] [Port]
�rnek:

bash
Kodu kopyala
python client.py 192.168.1.105 8081
Ba�land�ktan sonra, mesaj�n�z� yaz�p Enter tu�una basarak g�nderebilirsiniz.

Kullan�m Notlar�
Her istemci, ba�land�klar�nda sunucudan bir "Ho� geldin" mesaj� al�r.
Mesajlar, di�er ba�l� istemciler taraf�ndan g�r�lebilir.
Ba�lant� kesilirse, istemci otomatik olarak kapan�r.
Katk�da Bulunanlar
Ad�n�z
Lisans
Bu proje, MIT Lisans� alt�nda lisanslanm��t�r.

markdown
Kodu kopyala

### A��klamalar:

1. **Ba�l�k ve A��klama**: Projenizin ad� ve k�sa bir a��klamas�.
2. **�zellikler**: Uygulaman�z�n sundu�u �zellikler.
3. **Gereksinimler**: Hangi yaz�l�mlara ihtiya� duyuldu�u.
4. **Kurulum**: Projeyi nas�l indirece�inize dair ad�mlar.
5. **Kullan�m**: Sunucu ve istemci nas�l ba�lat�l�r, �rnek komutlar.
6. **Kullan�m Notlar�**: Kullan�m hakk�nda dikkat edilmesi gereken noktalar.
7. **Katk�da Bulunanlar**: E�er bir ekip ile �al��t�ysan�z, katk�da bulunanlar� belirtebilirsiniz.
8. **Lisans**: Projenizin lisans bilgisi.

