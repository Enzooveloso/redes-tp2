import logging
import socket

"""
Cliente TCP que envia uma mensagem ao servidor e exibe a resposta
Discentes: Arthur Abreu, Enzo Veloso, Josiney Junior
"""
logging.basicConfig(
    filename='server_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    host = '127.0.0.1'
    port = 5001

    # Solicita uma mensagem válida do usuário
    while True:
        message = input("Digite a mensagem para enviar ao servidor: ").strip()
        if message:
            break
        logging.info("A mensagem não pode ser vazia. Tente novamente")

    try:
        # Cria o socket e estabelece a conexão
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            # Envia a mensagem
            client_socket.send(message.encode())
            # Recebe a resposta
            response = client_socket.recv(1024).decode()
            logging.info(f"Resposta do servidor: {response}")
    except ConnectionRefusedError:
        logging.info("Não foi possível conectar ao servidor. Verifique se o servidor está ativo")
    except Exception as e:
        logging.info(f"Erro na comunicação com o servidor: {e}")

if __name__ == "__main__":
    main()