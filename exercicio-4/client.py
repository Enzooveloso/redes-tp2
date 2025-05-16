import logging
import socket

"""
Cliente TCP que se conecta a um servidor de hora e solicita a hora atual.
Discentes: Arthur Abreu, Enzo Veloso, Josiney Junior
"""

logging.basicConfig(
    filename='server_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

HOST = '127.0.0.1'  # IP do servidor
PORT = 7000         # Porta usada pelo servidor


def client_request_time():
    """
    Cliente TCP que se conecta ao servidor de hora,
    envia uma solicitação e imprime a resposta recebida.
    """
    try:
        # Cria o socket TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((HOST, PORT))  # Conecta ao servidor
            client.sendall("hora".encode())  # Envia o comando "hora"

            # Recebe e exibe a hora retornada pelo servidor
            response = client.recv(1024).decode()
            logging.info(f"[CLIENTE] Hora recebida do servidor: {response}")
    except Exception as e:
        logging.info(f"[CLIENTE ERRO] Falha ao conectar ao servidor: {e}")


client_request_time()
