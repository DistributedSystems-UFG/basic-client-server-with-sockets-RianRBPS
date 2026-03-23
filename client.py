from socket import *
from constCS import *

operacao = input("Operacao (add, subtract, multiply, divide): ")
a = input("Valor 1: ")
b = input("Valor 2: ")

msg = f"{operacao},{a},{b}"

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
s.send(msg.encode())

resp = s.recv(1024)
print("Resposta:", resp.decode())

s.close()
