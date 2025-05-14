import socket
import threading

"""
Servidor de chat TCP que conecta dois clientes e encaminha mensagens entre eles
Discentes: Arthur Abreu, Enzo Veloso, Josiney Junior
"""

def handle_client(receiver, sender):
    """
    Encaminha mensagens de um cliente para o outro
    """
    try:
        while True:
            data = receiver.recv(1024)
            if not data:
                break
            message = data.decode().strip()
            if message.lower() == 'sair':
                break
            sender.send(data)
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        receiver.close()
        sender.close()
        print("Conexões encerradas")

def main():
    host = '127.0.0.1'
    port = 7001  # Porta específica para o chat

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(2)  # Aceita até duas conexões
    print(f"Servidor de chat ouvindo na porta {port}...")

    try:
      # Aceita o primeiro cliente
      client1, addr1 = server_socket.accept()
      print(f"Cliente 1 conectado: {addr1}")

      # Aceita o segundo cliente
      client2, addr2 = server_socket.accept()
      print(f"Cliente 2 conectado: {addr2}")

      # Inicia as threads para encaminhamento
      thread1 = threading.Thread(target=handle_client, args=(client1, client2))
      thread2 = threading.Thread(target=handle_client, args=(client2, client1))

      thread1.start()
      thread2.start()

      thread1.join()
      thread2.join()
    except KeyboardInterrupt:
        print("\nServidor encerrando...")
    finally:
      server_socket.close()
      print("Servidor encerrado")

if __name__ == "__main__":
    main()