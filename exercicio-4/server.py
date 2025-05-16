import socket
import threading
import logging
from datetime import datetime

"""
Servidor de hora TCP multithread que fornece a hora atual para múltiplos clientes simultaneamente.
Discentes: Arthur Abreu, Enzo Veloso, Josiney Junior
"""

logging.basicConfig(
    filename='server_time_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

HOST = '127.0.0.1'  # Endereço IP local (localhost)
PORT = 7000         # Porta usada pelo servidor


def handle_client(conn, addr):
    """
    Função executada por uma thread para atender um cliente específico.
    Recebe a solicitação do cliente e envia a hora atual.
    """
    try:
        logging.info(f"[LOG] Conexão recebida de {addr}")

        # Recebe a mensagem enviada pelo cliente
        data = conn.recv(1024).decode()

        # Verifica se a mensagem é o comando correto
        if data.strip().lower() == "hora":
            # Gera a hora atual no formato HH:MM:SS
            current_time = datetime.now().strftime("%H:%M:%S")
            conn.send(current_time.encode())  # Envia hora ao cliente
            logging.info(f"[LOG] Hora enviada para {addr}: {current_time}")
        else:
            # Caso o comando não seja reconhecido
            conn.send("Comando inválido.".encode())
    except Exception as e:
        logging.info(f"[ERRO] Falha ao atender {addr}: {e}")
    finally:
        conn.close()  # Fecha a conexão com o cliente


def start_server():
    """
    Função principal que inicializa o servidor TCP.
    Escuta em uma porta e cria uma nova thread para cada cliente.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    logging.info(f"[INFO] Servidor ouvindo em {HOST}:{PORT}")

    while True:
        try:
            conn, addr = server.accept()  # Aceita nova conexão
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()  # Inicia uma nova thread para o cliente
        except KeyboardInterrupt:
            logging.info("\n[INFO] Encerrando o servidor.")
            break
        except Exception as e:
            logging.info(f"[ERRO] Erro inesperado: {e}")
            continue


start_server()
