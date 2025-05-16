import socket
import logging
"""
Servidor UDP que ecoa mensagens de volta para o cliente
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

    # Configura o socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    logging.info(f"Servidor UDP ouvindo na porta {port}...")

    try:
        while True:
            # Recebe dados e endereço do cliente
            data, addr = server_socket.recvfrom(max_size)  
            logging.info(f"Recebido de {addr}: {data.decode()}")
            
            # Envia os dados de volta (eco)
            server_socket.sendto(data, addr)
    except KeyboardInterrupt:
        logging.info("\nServidor encerrando...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()