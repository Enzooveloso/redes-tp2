import socket
import threading
import logging

"""
Servidor TCP que aceita múltiplas conexões de clientes e responde com confirmação
Discentes: Arthur Abreu, Enzo Veloso, Josiney Junior
"""
logging.basicConfig(
    filename='server_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def handle_client(client_socket, addr):
    """
    Lida com a comunicação de um cliente conectado
    """
    try:
        logging.info(f"Conexão estabelecida com {addr}")
        # Recebe dados do cliente
        data = client_socket.recv(1024).decode()
        
        # Valida se a mensagem não está vazia
        if not data.strip():
            logging.info(f"Cliente {addr} enviou uma mensagem vazia")
            response = "Erro: Mensagem não pode ser vazia"
        else:
            logging.info(f"Recebido de {addr}: {data}")
            response = "Mensagem recebida"
        
        # Envia resposta e fecha a conexão
        client_socket.send(response.encode())
    except Exception as e:
        logging.info(f"Erro ao lidar com cliente {addr}: {e}")
    finally:
        client_socket.close()
        logging.info(f"Conexão com {addr} fechada")

def main():
    host = '127.0.0.1'
    port = 5001

    # Configura o socket do servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    logging.info(f"Servidor ouvindo na porta {port}...")

    try:
        while True:
            # Aceita nova conexão
            client_socket, addr = server_socket.accept()
            # Inicia uma nova thread para o cliente
            client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_thread.start()
    except KeyboardInterrupt:
        logging.info("\nServidor encerrando...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()