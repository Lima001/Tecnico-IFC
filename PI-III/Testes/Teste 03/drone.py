import socket, time

class ConexaoDrone:

    def __init__(self,host,port,tello_address):
        self.locaddr = (host,port)
        self.tello_address = tello_address
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self.locaddr)

    def executar_sequencia_comando(self,comandos):
        for i in comandos:
            try:
                self.sock.sendto(i.encode(encoding="utf-8"),self.tello_address)
                time.sleep(5)
            except Exception as ex:
                self.sock.close()
                return ex
        self.sock.close()

if __name__ == "__main__":
    conexao1 = ConexaoDrone('',9000,("192.168.10.1", 8889))
    comandos = ["command","takeoff","land"]
    conexao1.executar_sequencia_comando(comandos)

