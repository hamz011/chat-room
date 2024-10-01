import socket
import sys
import threading

def receive_messages(server_socket):
    while True:
        try:
            message = server_socket.recv(2048).decode('utf-8')  
            if not message:
                print("Bağlantı kesildi!")
                server_socket.close()
                sys.exit()
            print(message) 
        except Exception as e:
            print("Bağlantı sırasında bir hata oluştu:", e)
            server_socket.close()
            sys.exit()

def send_messages(server_socket):
    while True:
        message = sys.stdin.readline()
        if message:
            try:
                server_socket.send(message.encode('utf-8')) 
                sys.stdout.write("<You> " + message)  
                sys.stdout.flush()
            except Exception as e:
                print("Mesaj gönderilirken bir hata oluştu:", e)
                server_socket.close()
                sys.exit()

def main():
    if len(sys.argv) != 3:
        print("Doğru kullanım: python client.py IP_adresi Port")
        sys.exit()

    IP_address = str(sys.argv[1])
    Port = int(sys.argv[2])

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect((IP_address, Port))
        print("Sunucuya başarıyla bağlanıldı.")
    except socket.error as e:
        print(f"Bağlantı hatası: {e}")
        sys.exit()

    receive_thread = threading.Thread(target=receive_messages, args=(server,))
    receive_thread.daemon = True
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(server,))
    send_thread.daemon = True
    send_thread.start()

    receive_thread.join()
    send_thread.join()

if __name__ == "__main__":
    main()
