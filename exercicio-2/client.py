import logging
import socket

"""
Cliente UDP que envia mensagens para o servidor e exibe o eco
Discentes: Arthur Abreu, Enzo Veloso, Josiney Junior
"""

logging.basicConfig(
    filename='server_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    host = '127.0.0.1'  
    port = 6000
    max_size = 64*1024  # Tamanho máximo permitido (64 KB - overhead)

    # Configura o socket UDP com timeout
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5)  # Timeout de 5 segundos para resposta

    try:
        while True:
            msg = input("Digite a mensagem (ou 'sair' para encerrar): ").strip()
            if msg.lower() == "sair":
                break

            # Valida o tamanho da mensagem
            msg_bytes = msg.encode()
            if len(msg_bytes) > max_size:
                logging.info(f"Erro: Mensagem excede {max_size} bytes")
                continue

            try:
                # Envia a mensagem para o servidor
                client_socket.sendto(msg_bytes, (host, port))
                # Recebe a resposta do servidor
                data, server = client_socket.recvfrom(max_size)
                logging.info(f"Eco recebido: {data.decode()}")
            except socket.timeout:
                logging.info("Erro: Tempo excedido. Possível perda de pacote")
            except Exception as e:
                logging.info(f"Erro na comunicação: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()