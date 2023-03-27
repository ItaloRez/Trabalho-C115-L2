import socket

# Define o host e a porta para o servidor
HOST = '127.0.0.1'
PORT = 12345

# Cria um socket para o servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao host e porta especificados
s.bind((HOST, PORT))

# Espera por uma conexão do cliente
s.listen(1)
print(f'Esperando por conexão na porta {PORT}...')

# Aceita a conexão do cliente e obtém o socket e endereço do cliente
conn, addr = s.accept()
print(f'Conectado por {addr}')

# Loop principal do servidor
while True:
    # Recebe o nome do arquivo do cliente
    filename = conn.recv(1024).decode()

    # Abre o arquivo solicitado pelo cliente e envia o seu conteúdo
    try:
        with open(filename, 'rb') as file:
            data = file.read()
            conn.send(data)
            print(f'{filename} enviado para o cliente')
    except FileNotFoundError:
        conn.send('Arquivo não encontrado'.encode('utf-8'))
        print(f'Arquivo {filename} não encontrado')