import socket, time, threading

class ConexaoDrone:

    def __init__(self,host,port,tello_address):
        self.locaddr = (host,port)
        self.tello_address = tello_address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.locaddr)
        self.recvThread = threading.Thread(target=self.receber_resposta)
        self.recvThread.start()
        self.respostas = []

    def executar_sequencia_comando(self,comandos):
        for i in comandos:
            try:
                self.sock.sendto(i.encode(encoding="utf-8"),self.tello_address)
                time.sleep(5)
            except Exception:
                self.finalizar_conexao()
                break
        self.finalizar_conexao()
        return self.respostas

    def receber_resposta(self):
        while True:
            try:
                data, server = self.sock.recvfrom(1518)
                self.respostas.append(data.decode(encoding="utf-8"))
            except Exception:
                break

    def finalizar_conexao(self):
        self.sock.close()


if __name__ == "__main__":
    conexao1 = ConexaoDrone('',9000,("192.168.10.1", 8889))
    comandos = ["command","takeoff","land"]
    comandos2 = ["battery?"]
    conexao1.executar_sequencia_comando(comandos2)

    trava = input(">>>")
    print(comandos)
    print(conexao1.respostas)