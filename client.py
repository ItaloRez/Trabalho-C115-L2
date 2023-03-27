import socket

# Define o host e a porta do servidor
HOST = '127.0.0.1'
PORT = 12345

# Cria um socket para o cliente
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta-se ao servidor
s.connect((HOST, PORT))
print(f'Conectado ao servidor {HOST}:{PORT}')

# Loop principal do cliente
while True:
    # Solicita o nome do arquivo ao usuário
    filename = input('Digite o nome do arquivo que deseja baixar: ')

    # Envia o nome do arquivo para o servidor
    s.send(filename.encode())

    # Recebe o conteúdo do arquivo do servidor
    data = s.recv(1024)

    # Verifica se o arquivo foi encontrado pelo servidor
    if data == 'Arquivo não encontrado'.encode('utf-8'):
        print(f'Arquivo {filename} não encontrado no servidor')
    else:
        # Grava o conteúdo do arquivo em um novo arquivo local
        with open(f'novo_{filename}', 'wb') as file:
            file.write(data)
            print(f'{filename} baixado com sucesso')