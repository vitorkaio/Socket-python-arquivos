# coding: utf-8

import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.0.106', 8085))

# Abrindo o arquvio
arquivo = open('Capa.jpg','rb')
s.send('Capa.jpg')

# Pega cada linha do arquivo
data = arquivo.readlines()
# Pega cada linha do arquivo, pois só pode enviar 1024 bytes.
for line in data:
   print 'Enviando...'
   s.send(line)

arquivo.close()

'''arquivo = open('Inacio.jpg', 'w')
arquivo.write(conteudo)
arquivo.close()'''

print '\nEnviado\n'    
s.close()
# Colocar em loop.

