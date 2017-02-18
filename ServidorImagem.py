# coding: utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('192.168.0.106', 8085))
s.listen(1)
print('Aguardando conexão...\n')

con, info_cli = s.accept()
print('Conexão Estabelecida')

titulo = con.recv(1024)
arq = open(titulo, 'wb')

# Recebe dados do cliente até não haver mais.
while 1:

    dados = con.recv(1024)
    # Verifica se os dados foram terminados.
    if not dados:
        break
    arq.write(dados)

print('Conexão fechada')
arq.close()
s.close()
con.close()

