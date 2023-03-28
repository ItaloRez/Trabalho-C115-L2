# Transferência de arquivos com Python
Este é um exemplo simples de transferência de arquivos entre um servidor e um cliente usando Python.

O programa consiste em dois arquivos:

- server.py: o código que executa no servidor, que escuta as requisições dos clientes e envia o conteúdo dos arquivos solicitados.
- client.py: o código que executa no cliente, que envia as solicitações de arquivo para o servidor e grava o conteúdo recebido em um novo arquivo local.

## Como executar o programa
1. Abra dois terminais: um para o servidor e outro para o cliente.
2. No terminal do servidor, execute o comando python server.py.
3. No terminal do cliente, execute o comando python client.py.
4. Siga as instruções para enviar solicitações de arquivos e receber os arquivos do servidor.

## Requisitos
Python 3.x
Biblioteca padrão do Python: socket

## Como funciona o programa
O programa usa sockets para criar uma conexão entre o cliente e o servidor. O cliente envia o nome do arquivo que deseja receber e o servidor verifica se o arquivo existe. Se o arquivo existe, o servidor envia o conteúdo do arquivo para o cliente, que grava o conteúdo em um novo arquivo local.
