import logging
import socket
import threading

"""
Cliente de chat TCP que permite envio e recebimento de mensagens simultâneas
Discentes: Arthur Abreu, Enzo Veloso, Josiney Junior
"""

logging.basicConfig(
    filename='server_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def receive_messages(sock):
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                break
            logging.info(
                f"\nMensagem recebida: {data.decode()}\nDigite sua mensagem: ", end='')
    except Exception as e:
        logging.info(f"\nErro ao receber mensagens: {e}")
    except KeyboardInterrupt:
        logging.info("\nCliente encerrando...")
    finally:
        sock.close()


def send_messages(sock):
    try:
        while True:
            message = input("Digite sua mensagem (ou 'sair' para encerrar): ")
            if message.lower() == 'sair':
                sock.send(message.encode())
                break
            sock.send(message.encode())
    except Exception as e:
        logging.info(f"Erro ao enviar mensagem: {e}")
    except KeyboardInterrupt:
        logging.info("\nCliente encerrando...")
    finally:
        sock.close()


def main():
    host = '127.0.0.1'
    port = 7001

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
    except Exception as e:
        logging.info(f"Não foi possível conectar ao servidor: {e}")
        return

    try:
        # Inicia as threads de envio e recebimento
        receive_thread = threading.Thread(
            target=receive_messages, args=(sock,))
        send_thread = threading.Thread(target=send_messages, args=(sock,))

        receive_thread.start()
        send_thread.start()

        receive_thread.join()
        send_thread.join()
    except KeyboardInterrupt:
        logging.info("\nEncerrando conexão...")
    finally:
        receive_messages



if __name__ == "__main__":
    main()
