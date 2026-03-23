from socket import *
from constCS import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

print(f"Servidor ouvindo em {HOST}:{PORT}")

while True:
    conn, addr = s.accept()
    print(f"\nConectado por {addr}")

    data = conn.recv(1024)
    if not data:
        conn.close()
        continue

    msg = data.decode().strip()
    print(f"Recebido: {msg}")

    try:
        parts = msg.split(",")

        if len(parts) != 3:
            response = "Erro: use formato operacao,valor1,valor2"
        else:
            operacao = parts[0].lower()
            a = float(parts[1])
            b = float(parts[2])

            print(f"Operacao solicitada: {operacao}")
            print("Processando requisicao...")
            time.sleep(1)

            if operacao == "add":
                print("Somando valores...")
                time.sleep(1)
                resultado = a + b

            elif operacao == "subtract":
                print("Subtraindo valores...")
                time.sleep(1)
                resultado = a - b

            elif operacao == "multiply":
                print("Multiplicando valores...")
                time.sleep(1)
                resultado = a * b

            elif operacao == "divide":
                print("Dividindo valores...")
                time.sleep(1)
                if b == 0:
                    response = "Erro: divisao por zero"
                else:
                    resultado = a / b
                    response = f"Resultado: {resultado}"

            else:
                response = "Erro: operacao invalida"

            if operacao in ["add", "subtract", "multiply"]:
                response = f"Resultado: {resultado}"

    except ValueError:
        response = "Erro: valores devem ser numericos"
    except Exception as e:
        response = f"Erro interno: {str(e)}"

    conn.send(response.encode())
    conn.close()
