# Chat Room Uygulaması

Bu uygulama, yerel bir ağ üzerinden çoklu kullanıcıların iletişim kurmasını sağlayan bir sohbet odasıdır. Kullanıcılar, sunucuya bağlanarak mesaj gönderip alabilirler.

## Özellikler

- Çoklu kullanıcı desteği
- Anlık mesajlaşma
- Kullanıcıların bağlandıklarında hoş geldin mesajı

## Gereksinimler

- Python 3.x
- `socket` ve `threading` kütüphaneleri (Python ile birlikte gelir)

## Kurulum

1. Bu repo'yu bilgisayarınıza indirin:
   ```bash
   git clone https://github.com/hamz011/chat-room.git
   cd chat-room
   ```

2. Sunucu ve istemci dosyalarını çalıştırmadan önce, aşağıdaki adımları izleyin:

## Kullanım

### Sunucu

1. Sunucuyu başlatmak için terminalde şu komutu çalıştırın:
   ```bash
   python chat_server.py [IP_adresi] [Port]
   ```
   Örnek:
   ```bash
   python chat_server.py 192.168.1.105 8081
   ```

2. Sunucu, belirtilen IP adresinde ve portta dinlemeye başlayacaktır. Terminalde bağlı kullanıcıları görebilirsiniz.

### İstemci

1. İstemciyi başlatmak için ayrı bir terminal penceresi açın ve şu komutu çalıştırın:
   ```bash
   python client.py [IP_adresi] [Port]
   ```
   Örnek:
   ```bash
   python client.py 192.168.1.105 8081
   ```

2. Bağlandıktan sonra, mesajınızı yazıp Enter tuşuna basarak gönderebilirsiniz.

## Kullanım Notları

- Her istemci, bağlandıklarında sunucudan bir "Hoş geldin" mesajı alır.
- Mesajlar, diğer bağlı istemciler tarafından görülebilir.
- Bağlantı kesilirse, istemci otomatik olarak kapanır.
  
## Kullanım Örnekleri

Aşağıdaki örnek, istemci uygulamasının nasıl çalıştığını göstermektedir:

![İstemci Örneği](https://github.com/hamz011/chat-room/blob/main/example.jpg)

## Katkıda Bulunanlar

- [Hamza](https://github.com/hamz011)

## Lisans

Bu proje, [MIT Lisansı](LICENSE) altında lisanslanmıştır.
